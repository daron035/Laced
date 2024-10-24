from pathlib import Path

from proxy import Proxy

from scrapper import Selenium


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
