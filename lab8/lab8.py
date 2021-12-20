import requests as re
import re as r
import argparse
import os
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image
from io import BytesIO
import multiprocessing.dummy
import multiprocessing

def initParser():
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument('--url', help="Url of website", type=str, required=True)
    optional.add_argument('--out', help="Name of out file", type=str, default='out')

    return parser

def get_images(url):
    try:
        conn = re.get(url)
        conn.raise_for_status()
    except re.exceptions.HTTPError as E:
        print(E)
    except ConnectionError:
        print("Website not found...")
    else:
        soup = BeautifulSoup(conn.text, 'html.parser')
        links = soup.find_all('a', href=r.compile('.*?(?=png|jpg|jpeg|gif)'))
        return [img['href'] for img in links]

def download_images(url, out, images):
    path = os.getcwd()+f"\\{out}"
    Path(path).mkdir(parents=True, exist_ok=True)  

    num_threads = len(images) * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)

    def convert_and_download(img):
        data = Image.open(BytesIO(re.get(url+img).content)).convert("L")
        data.save(f"{path}\\{img}")

    p.map(convert_and_download, [img for img in images])
        

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()

    images = get_images(args.url)
    download_images(args.url, args.out, images)