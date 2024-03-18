import json
import multiprocessing
import argparse
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from proxy import Proxy

from scrapper import Selenium, worker


BASE_DIR = Path(__file__).resolve().parent
proxy_file_path = BASE_DIR.joinpath("proxy_list.json")


# def process_page():
#     worker()
#
#
# def th():
#     with ThreadPoolExecutor(
#         max_workers=5
#     ) as executor:  # Указать желаемое количество потоков (max_workers)
#         executor.map(process_page, range(20))


if __name__ == "__main__":
    print("Start...")

    Selenium(Proxy.get(proxy_file_path)).get_data()
    # worker()

    print("Finish")
