import json
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

def initParser():
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()

    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('--out', help="Name of out file", type=str, default='out')

    return parser

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()

    try:
        options = webdriver.ChromeOptions();
        options.add_argument('headless');
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get("https://tipeo.pl/multisquad/lista-wpisow")
    except Exception as E:
        print(f"Error occurred:\n{E}")
    else:
        try:
            data = []
            for i in range(1, 21):
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="super_tabela"]/tbody/tr[{i}]/td'))
                )
                title, time, desc = element.text.split('\n')
                data.append({
                    "title": title,
                    "time": time,
                    "desc": desc
                })
        finally:
            driver.quit()
            with open(f"{args.out}.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)