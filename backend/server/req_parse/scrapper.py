import json
import random
import sys
import time
from pathlib import Path
from pprint import pprint

from bs4 import BeautifulSoup
from proxy import Proxy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


BASE_DIR = Path(__file__).resolve().parent
proxy_file_path = BASE_DIR.joinpath("proxy_list.json")


class Selenium:
    """For Chrome."""

    def __init__(self, ip: str) -> None:
        options = Options()
        # options.add_argument("--headless=new")
        options.page_load_strategy = "eager"

        PROXY_IP = ip

        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        webdriver.DesiredCapabilities.CHROME["proxy"] = {
            "httpProxy": PROXY_IP,
            "ftpProxy": PROXY_IP,
            "sslProxy": PROXY_IP,
            "proxyType": "MANUAL",
        }
        webdriver.DesiredCapabilities.CHROME["acceptSslCerts"] = True
        options.add_argument("user-agent=" + user_agent)

        self.driver = webdriver.Chrome(
            options=options, service=ChromeService(ChromeDriverManager().install()),
        )
        self.driver.set_window_size(1340, 1800)

    def _time(self):
        time.sleep(random.uniform(2, 4))

    def close_modals(self, url):
        self.driver.get(url)
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn--primary")),
            )
            element.click()
            self._time()

            # self._time()
            # self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn--primary").click()
            # self._time()
        except Exception:
            # print(f"An error occurred: {e}")
            print("Modal windows were not detected")

    def get_data(self):
        with open("links/all_product_links.json") as link_file:
            links = json.load(link_file)

        with open("products/product.json", "a+") as prod_file, open(
            "products/image.json", "a+",
        ) as img_file:
            try:
                glob_id = len(json.load(prod_file))
            except:
                glob_id = 1

            for l_id, l in enumerate(links, start=glob_id):
                try:
                    self.close_modals(l)
                    soup = BeautifulSoup(self.driver.page_source, "html.parser")
                    images_block = soup.select_one("div.product-image_grid")
                    print(images_block)
                except:
                    pass


def worker():
    with open("links/all_product_links.json") as link_file:
        links = json.load(link_file)

    with open("products/product.json", "a+") as prod_file, open(
        "products/image.json", "a+",
    ) as img_file:
        try:
            glob_id = len(json.load(prod_file))
        except:
            glob_id = 1

        for l_id, l in enumerate(links, start=glob_id):
            try:
                sl = sel_init()
                sl.close_modals(l)
                soup = BeautifulSoup(sl.driver.page_source, "html.parser")
                images_block = soup.select_one("div.product-image_grid")
                pprint(images_block)
                sl.driver.quit()
            except:
                sys.exit(1)


def sel_init():
    return Selenium(Proxy.get(proxy_file_path))
