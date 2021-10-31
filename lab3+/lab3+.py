import requests as re
import json
import argparse
from bs4 import BeautifulSoup

def initParser():
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('--out', help="Name of out file", type=str, default='out')
    # required.add_argument('--out', help="Name of out file", type=str, required=True)

    return parser

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()

    max_index = 5
    all_videos = dict()

    for index in range(max_index):
        try:
            conn = re.get(f"https://profmrow.fans/pwzn/toc{index+1}/")
            conn.raise_for_status()
        except re.exceptions.HTTPError as E:
            print(E)
        except ConnectionError:
            print("Website not found...")
        else:
            if conn.status_code == 200:
                soup = BeautifulSoup(conn.content.decode(conn.apparent_encoding), "html.parser")
                elements = [val.text for val in soup.findAll("option")]
                if elements is None:
                    continue

                for element in elements:
                    try:
                        page = re.get(f"https://profmrow.fans/pwzn/toc1/?year={element}")
                        page.raise_for_status()
                    except re.exceptions.HTTPError as E:
                        print(E)
                    except ConnectionError:
                        print(f"Website not found (for value {element})...")
                    
                    soup = BeautifulSoup(page.content.decode(page.apparent_encoding), "html.parser")
                    videos = [val.text for val in soup.findAll("div", class_="text-center mb-2")]
                    if videos is None:
                        continue
                    for video in videos:
                        if element not in all_videos:
                            all_videos[element] = []
                        if video not in all_videos[element]:
                            all_videos[element].append(video)

    with open(f"{args.out}.json", "w", encoding="utf-8") as file:
        json.dump(all_videos, file, indent=4, sort_keys=True)