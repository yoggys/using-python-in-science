import requests as re
import json
import argparse
from bs4 import BeautifulSoup

def initParser():
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument('--url', help="Url of website", type=str, required=True)
    optional.add_argument('--out', help="Name of out file", type=str, default='out')

    return parser

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()

    try:
        conn = re.get(args.url)
        conn.raise_for_status()
    except re.exceptions.HTTPError as E:
        print(E)
    except ConnectionError:
        print("Website not found!")
    else:
        if conn.status_code == 200:
            soup = BeautifulSoup(conn.text, "html.parser")
            decoded = soup.decode(True, "utf-8")
            
            with open(f"{args.out}.json", "w", encoding="utf-8") as file:
                json.dump(decoded, file, indent=4, sort_keys=True)
