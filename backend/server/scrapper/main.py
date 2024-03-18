import json
import multiprocessing
import argparse
import re
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from proxy import Proxy

# from scrapper import Selenium, Product
from scrapper import Selenium
from set_list import sort_files


BASE_DIR = Path(__file__).resolve().parent
proxy_file_path = BASE_DIR.joinpath("Free_Proxy_List-0.json")


nike = "https://www.laced.com/nike"
yeezy = "https://www.laced.com/yeezy"
air_jordan = "https://www.laced.com/air-jordan"
adidas = "https://www.laced.com/adidas"
new_balance = "https://www.laced.com/new-balance"

air_jordan = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=2"
adidas = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=3"
new_balance = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=7"
nike = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=4"
asics = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=9"
crocs = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=10"
ugg = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=14"
converse = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=11"
on_running = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=15"
yeezy = "https://www.laced.com/search?search%5Bbrands%5D%5B%5D=1"


def get_list_wrapper(proxy, brand, filename, process_id):
    Selenium(proxy).get_list(brand, filename, process_id)


def get_list():
    """Multiprocessing"""

    processes = []

    # instantiating process with arguments
    brands = [
        (Proxy.get(proxy_file_path), asics, "asics"),
        (Proxy.get(proxy_file_path), crocs, "crocs"),
        (Proxy.get(proxy_file_path), converse, "converse"),
    ]

    for process_id, (proxy, brand, filename) in enumerate(brands):
        process = multiprocessing.Process(
            target=get_list_wrapper, args=(proxy, brand, filename, process_id + 1)
        )
        processes.append(process)
        process.start()

    # complete the processes
    for process in processes:
        process.join()

    print("All processes have finished.")


if __name__ == "__main__":
    print("Start...")

    # get_list()

    # Selenium(Proxy.get(proxy_file_path)).get_products()

    # scrap.get_list(nike)
    # scrap.get_products("adidas")

    # Selenium(Proxy.get(proxy_file_path)).get_all_details()
    # Selenium(Proxy.get(proxy_file_path)).entry()
    # Selenium(Proxy.get(proxy_file_path)).tr()
    # Selenium(Proxy.get(proxy_file_path)).dl_tr()
    # Selenium(Proxy.get(proxy_file_path)).dl()
    # Selenium(Proxy.get(proxy_file_path)).get_available_sizes(id=1, pk=1)
    Selenium(Proxy.get(proxy_file_path)).get_available_sizes()
    # Selenium(Proxy.get(proxy_file_path)).get_available_sizes(12)

    # Product()
    print("Finish")
