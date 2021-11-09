import requests as req
import re
import json
import argparse
from bs4 import BeautifulSoup

def initParser():
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()

    required = parser.add_argument_group('required arguments')
    required.add_argument('--out', help="Name of out file", type=str, required=True)

    return parser

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()

    max_index = 5
    all_videos = dict()

    for index in range(max_index):
        try:
            if index < 3:
                conn = req.get(f"https://profmrow.fans/pwzn/toc{index+1}/")
            else:
                conn = req.get(f"https://profmrow.fans/pwzn/chuck_service/?mode=years")

            conn.raise_for_status()
        except req.exceptions.HTTPError as E:
            print(E)
        except ConnectionError:
            print("Website not found...")
        else:
            if conn.status_code == 200:
                if index < 3:
                    soup = BeautifulSoup(conn.content.decode(conn.apparent_encoding), "html.parser")
                    elements = [val.text for val in soup.findAll("option")]
                elif index == 3:
                    soup = BeautifulSoup(conn.content.decode(conn.apparent_encoding), "html.parser").contents
                    elements = re.findall(r"\d+", conn.content.decode(conn.apparent_encoding))
                else:
                    elements = re.findall(r"\d+", conn.content.decode(conn.apparent_encoding))

                if elements is None:
                    continue

                for element in elements:
                    try:
                        if index == 0:
                            page = req.get(f"https://profmrow.fans/pwzn/toc{index+1}/?year={element}")
                            soup = BeautifulSoup(page.content.decode(page.apparent_encoding), "html.parser")
                            videos = [val.text for val in soup.findAll("div", class_="text-center mb-2")]
                        elif index == 1:
                            page = req.post(f"https://profmrow.fans/pwzn/toc{index+1}/", data={"year": element})
                            soup = BeautifulSoup(page.content.decode(page.apparent_encoding), "html.parser")
                            videos = [val.text for val in soup.findAll("div", class_="text-center mb-2")]
                        elif index == 2:
                            page = req.session()
                            page = page.get(f"https://profmrow.fans/pwzn/toc{index+1}/?year={element}", headers={"cookie": "Motto=Praise%20the%20Chuck"})
                            soup = BeautifulSoup(page.content.decode(conn.apparent_encoding), "html.parser")
                            videos = [val.text for val in soup.findAll("div", class_="text-center mb-2")]

                        elif index == 3:
                            headers = {
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
                            }
                            
                            page = req.post(f"https://profmrow.fans/pwzn/toc{index+1}/", data={"year": element}, headers=headers)
                            soup = BeautifulSoup(page.content, "html.parser")
                            videos = [val.text for val in soup.findAll("div", class_="text-center mb-2")]

                        elif index == 4:
                            page = req.get(f"https://profmrow.fans/pwzn/chuck_service/?mode=year&year={element}")
                            videos = [val['title'] for val in page.json()]       

                        page.raise_for_status()
                    except req.exceptions.HTTPError as E:
                        print(E)
                    except ConnectionError:
                        print(f"Website not found (for value {element})...")
                    
                    if videos is None:
                        continue
                    for video in videos:
                        if element not in all_videos:
                            all_videos[element] = []
                        if video not in all_videos[element]:
                            all_videos[element].append(video)

    with open(f"{args.out}.json", "w", encoding="utf-8") as file:
        json.dump(all_videos, file, indent=4, sort_keys=True)