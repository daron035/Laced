import json
from pprint import pprint
import base64
import requests
import re
import os
import sys
import time
import requests
from PIL import Image
import random
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from proxy import Proxy


BASE_DIR = Path(__file__).resolve().parent
# proxy_file_path = BASE_DIR.joinpath("proxy_list.json")


class Selenium:
    """For Chrome"""

    def __init__(self, ip: str) -> None:
        options = Options()
        options.add_argument("--headless=new")
        # Both option for disabling image loading in Selenium should work, however, if it isn't working then you
        # can try using the other option or both options at the same time:
        options.add_argument("--blink-settings=imagesEnabled=false")
        options.add_experimental_option(
            "prefs",
            {
                # block image loading
                "profile.managed_default_content_settings.images": 2
            },
        )

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
            options=options, service=ChromeService(ChromeDriverManager().install())
        )
        self.driver.set_window_size(1340, 1800)

    def _time(self):
        time.sleep(random.uniform(4, 8))

    def close_modals(self, url):
        self.driver.get(url)
        try:
            time.sleep(random.uniform(0.2, 1.2))
            element = WebDriverWait(self.driver, 3).until(
                # EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/aside/footer/button[1]"))
                EC.element_to_be_clickable((By.CSS_SELECTOR, "footer button.btn.btn--primary"))
                # EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn--primary"))
            )
            element.click()
            element1 = WebDriverWait(self.driver, 3).until(
                # EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/button"))
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.css-1qm4p5l"))
            )
            element1.click()
            self._time()

            # self._time()
            # self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn--primary").click()
            # self._time()
        except Exception as e:
            # print(f"An error occurred: {e}")
            print("Modal windows were not detected")
            pass

    def get_list(self, url: str, brand_name: str, process_id: int):
        """Links"""
        self.close_modals(url)

        grid_items = []
        item_quantity = len(grid_items)

        while True:
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            self._time()

            grid_items = self.driver.find_elements(
                By.CSS_SELECTOR, "li.product-grid__item"
            )
            # print(len(grid_items))
            print(f"Process {process_id} {len(grid_items)}")

            if len(grid_items) == item_quantity:
                break

            item_quantity = len(grid_items)

        item_links = self.driver.find_elements(
            By.CSS_SELECTOR, "ul.product-items.product-grid.category-grid li a"
        )

        # brand_name = (
        #     self.driver.find_element(By.CSS_SELECTOR, "h1.css-1rprnz9").text
        # ).lower()
        with open(f"links/{brand_name}.json", "w") as f:
            json.dump([i.get_attribute("href") for i in item_links], f)

        print(f"Process {process_id} final item quantity:", len(item_links))
        print(f"Process {process_id} FINISH")

    def get_products(self):
        """Categories"""
        url = "https://www.laced.com/yeezy"
        self.close_modals(url)
        time.sleep(3)
        option_element = self.driver.find_element(By.NAME, "category")
        options = Select(option_element)

        with open("db/on_running_categories.json", "w") as f:
            json.dump([i.text for i in options.options], f, indent=2)

    def change_ip(self):
        old_ip = webdriver.DesiredCapabilities.CHROME["proxy"]["httpProxy"]
        # print("Change ip from", old_ip)
        BASE = Path(__file__).resolve().parent
        u = [
            "Free_Proxy_List-0.json",
            "Free_Proxy_List-1.json",
            "Free_Proxy_List-2.json",
            "Free_Proxy_List-3.json",
            "Free_Proxy_List-4.json",
            "Free_Proxy_List-5.json",
            "Free_Proxy_List-6.json",
            "Free_Proxy_List-7.json",
        ]
        proxy_path = BASE.joinpath(random.choice(u))
        ip = Proxy.get(proxy_path)
        webdriver.DesiredCapabilities.CHROME["proxy"] = {
            "httpProxy": ip,
            "ftpProxy": ip,
            "sslProxy": ip,
            "proxyType": "MANUAL",
        }
        # print(
        #     "to",
        #     webdriver.DesiredCapabilities.CHROME["proxy"]["httpProxy"],
        # )
        return ip

    # def save_images(self, thumbs, orig, brand, name):
    #     with open("products/image.json", "a") as img_file:
    #         images_dir = self.check_dir(brand, "orig")
    #         time.sleep(random.uniform(4, 6))
    #         for img_id, t in enumerate(thumbs, start=1):
    #             t.click()
    #             time.sleep(random.uniform(4, 6))
    #             src = orig.get_attribute("src")
    #
    #             name = "_".join(name.lower().split())
    #
    #             try:
    #                 response = requests.get(src, stream=True)
    #                 # if response.status_code == 200:
    #                 #     image_extension = re.search(r".(\w+)\?", src)
    #                 #     image_extension = image_extension.group(1)
    #                 #     image_filename = f"{name}_{img_id}.{image_extension}"
    #                 #     image_path = Path.joinpath(images_dir, image_filename)
    #                 #     with open(image_path, "wb") as image_file:
    #                 #         image_file.write(response.content)
    #                 #
    #                 #     print(f"Image {img_id} downloaded: {image_filename}")
    #                 #
    #                 #     # return image_filename
    #                 #     return (img_id, image_path)
    #                 image_extension = re.search(r".(\w+)\?", src)
    #                 image_extension = image_extension.group(1)
    #                 image_filename = f"{name}_{img_id}.{image_extension}"
    #                 image_path = Path.joinpath(images_dir, image_filename)
    #                 with open(image_path, "wb") as image_file:
    #                     image_file.write(response.content)
    #
    #                 print(f"Image {img_id} downloaded: {image_filename}")
    #
    #                 # return image_filename
    #                 # else:
    #                 #     print(f"Failed to download image {img_id} from {name}")
    #             except Exception as e:
    #                 # print("Error IMAGE", e)
    #                 print(f"ERROR get image {img_id}")
    #                 src = src.replace("\ufeff", "")
    #                 base64_data = src.split(",")[1]
    #                 image_data = base64.b64decode(base64_data)
    #                 # image_filename = f"loading_{img_id}.png"
    #                 # image_filename = f"loading_{img_id}.png"
    #
    #                 image_extension = re.search(r".(\w+)\?", src)
    #                 image_extension = image_extension.group(1)
    #                 image_filename = f"{name}_{img_id}.{image_extension}"
    #                 image_path = Path.joinpath(images_dir, image_filename)
    #
    #                 with open(image_path, "wb") as image_file:
    #                     image_file.write(image_data)
    #
    #                 print(f"Image {img_id} not founded: {image_filename}")
    #
    #                 # return image_filename
    #                 # return (img_id, image_path)
    #             finally:
    #                 f_img = {
    #                     "model": "products.image",
    #                     "pk": self.global_img_id,
    #                     "fields": {
    #                         "image": image_path,
    #                         "lg_image": None,
    #                         "md_image": None,
    #                         "sm_image": None,
    #                         "tn_image": None,
    #                     },
    #                 }
    #                 json.dump(f_img, img_file, indent=2, ensure_ascii=False)
    #                 img_file.write(",\n")
    def save_img_json(self, thumb_images, brand_id):
        with open("products/image.json", "a") as rr:
            try:
                for et in thumb_images:
                    print(
                        "0000000000000000000000000000000000000000",
                        et.get_attribute("src"),
                    )
                    eee = {
                        "model": "products.image",
                        "pk": 0,
                        "fields": {
                            "product": brand_id,
                            "image": et.get_attribute("src"),
                            "lg_image": None,
                            "md_image": None,
                            "sm_image": None,
                            "tn_image": None,
                        },
                    }
                    json.dump(eee, rr, indent=2, ensure_ascii=False)
                    rr.write(",\n")
            except:
                json.dump({"model": False}, rr)
                rr.write(",\n")

    def get_all_details(self, urls):
        for url in urls[self.global_id - 1 :]:
            try:
                self.close_modals(url)

                images_block = self.driver.find_element(
                    By.CSS_SELECTOR, "div.product-image_grid"
                )
                info_block = self.driver.find_element(
                    By.CSS_SELECTOR,
                    "div[data-testid='product-info']",
                )

                thumb_images = self.driver.find_elements(
                    By.CSS_SELECTOR, "button.product-thumbs__item img"
                )
                # thumb_images = self.driver.find_elements(
                #     By.CSS_SELECTOR, "button.product-thumbs__item"
                # )

                # original_image = self.driver.find_element(
                #     By.XPATH,
                #     # "/html/body/div[3]/div[1]/div/div[2]/div[1]/div[2]/div/img",
                #     "/html/body/div[4]/div[1]/div/div[2]/div[1]/div[2]/div/img",
                # )
                original_image = images_block.find_element(
                    By.CSS_SELECTOR,
                    "div.product-picture img",
                )

                details = info_block.find_elements(
                    By.CSS_SELECTOR, "dl.css-1i5pxrw.e15nynkq0"
                )
                brand_name = details[0].find_element(By.CSS_SELECTOR, "dd a").text
                categories = details[1].find_elements(By.CSS_SELECTOR, "dd a")  # list
                print("categories", categories[0].text)
                year_released = details[2].find_element(By.CSS_SELECTOR, "dd").text
                print("YEAR_RELEASED", year_released)
                colour = details[3].find_element(By.CSS_SELECTOR, "dd").text
                print("COLOUR", colour)
                name = info_block.find_element(
                    By.CSS_SELECTOR, "h1.product-hdr__title"
                ).text.title()

                # self.save_images(thumb_images, original_image, brand_name, name)

                print("NAME", name)
                try:
                    description = info_block.find_element(
                        By.CSS_SELECTOR, "div.css-1j3px7c.e15nynkq2 div.body"
                    ).text
                except:
                    description = ""
                # print("DESCRIPTION", description)
                price = None
                is_active = False
                slug = url.rsplit("/", 1)[-1]
                print("SLUG", slug)
                sku = (
                    info_block.find_element(
                        By.CSS_SELECTOR,
                        "div.product-hdr__captain",
                    )
                    .text.rsplit("/", 1)[-1]
                    .strip()
                )
                print("SKU", sku)

                print("OK")

                self.change_ip()

                x = {
                    "brand_name": brand_name,
                    "brand": self.catch_brand(categories, brand_name),
                    "categories": categories,
                    "name": name,
                    "description": description,
                    "price": price,
                    "is_active": is_active,
                    "slug": slug,
                    "sku": sku,
                    "year_released": year_released,
                    "colour": colour,
                    "thumb_images": thumb_images,
                }

                yield x
            except Exception as e:
                print(e)
                yield url

    def catch_brand(self, categories, brand_name):
        # self.cats
        # for c in categories:
        #     c.text
        target_names = [y.text for y in categories]
        target_names.insert(0, brand_name)
        return [
            i["pk"]
            for i in self.cats
            if i.get("fields", {}).get("name", "").lower()
            in map(str.lower, target_names)
        ]

    def get_global_img_id(self):
        with open("products/image.json", "w+") as count_img_file:
            try:
                count_img = json.load(count_img_file)
                count = len(count_img)
                if count == 0:
                    self.global_img_id = 1
                else:
                    self.global_img_id = count + 1
            except:
                count_img_file.write("[\n")
                self.global_img_id = 1

    def close_img_json(self):
        with open("products/image.json", "a") as close_img:
            close_img.write("\n]")

    def entry(self):
        with open("products/product.json", "r+") as prod_f, open(
            "products/image.json", "r"
        ) as img_f, open("products/new_prod.json", "w") as new_prod, open(
            "products/new_img.json", "w"
        ) as new_img:
            # new_prod, new_img
            products = json.load(prod_f)
            images = json.load(img_f)

            for id, item in enumerate(products):
                status = item.get("status", None)
                if status is not None and not status:
                    self.close_modals(item["url"])

                    images_block = self.driver.find_element(
                        By.CSS_SELECTOR, "div.product-image_grid"
                    )
                    info_block = self.driver.find_element(
                        By.CSS_SELECTOR,
                        "div[data-testid='product-info']",
                    )

                    thumb_images = self.driver.find_elements(
                        By.CSS_SELECTOR, "button.product-thumbs__item img"
                    )
                    # thumb_images = self.driver.find_elements(
                    #     By.CSS_SELECTOR, "button.product-thumbs__item"
                    # )

                    # original_image = self.driver.find_element(
                    #     By.XPATH,
                    #     # "/html/body/div[3]/div[1]/div/div[2]/div[1]/div[2]/div/img",
                    #     "/html/body/div[4]/div[1]/div/div[2]/div[1]/div[2]/div/img",
                    # )
                    original_image = images_block.find_element(
                        By.CSS_SELECTOR,
                        "div.product-picture img",
                    )

                    details = info_block.find_elements(
                        By.CSS_SELECTOR, "dl.css-1i5pxrw.e15nynkq0"
                    )
                    brand_name = details[0].find_element(By.CSS_SELECTOR, "dd a").text
                    # categories = details[1].find_elements(By.CSS_SELECTOR, "dd a")  # list
                    if brand_name == "Air Jordan":
                        brand_name = [2]
                    if brand_name == "Nike":
                        brand_name = [3]
                    if brand_name == "New Balance":
                        brand_name = [4]
                    if brand_name == "Adidas":
                        brand_name = [5]
                    if brand_name == "Yeezy":
                        brand_name = [6]
                    if brand_name == "Asics":
                        brand_name = [7]
                    if brand_name == "Crocs":
                        brand_name = [8]
                    if brand_name == "UGG":
                        brand_name = [9]
                    if brand_name == "Converse":
                        brand_name = [10]
                    if brand_name == "On-Running":
                        brand_name = [11]
                    categories = ""
                    # print("categories", categories[0].text)
                    year_released = details[1].find_element(By.CSS_SELECTOR, "dd").text
                    print("YEAR_RELEASED", year_released)
                    colour = details[2].find_element(By.CSS_SELECTOR, "dd").text
                    print("COLOUR", colour)
                    name = info_block.find_element(
                        By.CSS_SELECTOR, "h1.product-hdr__title"
                    ).text.title()

                    # self.save_images(thumb_images, original_image, brand_name, name)

                    print("NAME", name)
                    try:
                        description = info_block.find_element(
                            By.CSS_SELECTOR, "div.css-1j3px7c.e15nynkq2 div.body"
                        ).text
                    except:
                        description = ""
                    # print("DESCRIPTION", description)
                    price = None
                    is_active = False
                    slug = item["url"].rsplit("/", 1)[-1]
                    print("SLUG", slug)
                    sku = (
                        info_block.find_element(
                            By.CSS_SELECTOR,
                            "div.product-hdr__captain",
                        )
                        .text.rsplit("/", 1)[-1]
                        .strip()
                    )
                    print("SKU", sku)

                    print("OK")

                    self.change_ip()
                    if "fields" not in products[id]:
                        products[id]["fields"] = {}
                    products[id]["model"] = "products.product"
                    products[id]["fields"]["brand"] = brand_name
                    products[id]["fields"]["name"] = name
                    products[id]["fields"]["price"] = None
                    products[id]["fields"]["is_active"] = False
                    products[id]["fields"]["slug"] = slug
                    if "data" not in products[id]["fields"]:
                        products[id]["fields"]["data"] = {}
                    products[id]["fields"]["data"]["description"] = description
                    products[id]["fields"]["data"]["sku"] = sku
                    products[id]["fields"]["data"]["year released"] = year_released
                    products[id]["fields"]["data"]["colour"] = colour

                    json.dump(products[id], new_prod, ensure_ascii=False, indent=2)

                #     n = {
                #         "model": "products.product",
                #         "pk": item['pk'],
                #         "fields": {
                #             # "brand": [2, 17, 18],
                #             "brand": brand_name,
                #             "name": name,
                #             # "description": record["description"],
                #             "price": price,
                #             "is_active": is_active,
                #             "slug": slug,
                #             "data": {
                #                 "description": description,
                #                 "sku": sku,
                #                 "year released": year_released,
                #                 "colour": colour,
                #             },
                #             "countries": [1],
                #         },
                #     }

                #         json.dump(n, prod_file, indent=2, ensure_ascii=False)
                #         if self.global_id > 0:
                #             prod_file.write(",\n")

                #         self.save_img_json(record["thumb_images"], rec_id)

                #         # self.global_img_id += 1
                #     except:
                #         n = {"pk": rec_id, "status": False, "url": record}
                #         json.dump(n, prod_file, indent=2, ensure_ascii=False)
                #         # prod_file.write("\n]")
                #         # self.global_id += 1
                #     # except:
                #     #     n = {"pk": rec_id + 1, "url": record}
                #     #     self.global_id += 1
                #     # finally:
                #     #     json.dump(n, prod_file, indent=2, ensure_ascii=False)
                #     #     self.save_id()
                #     #     if self.global_id > 1:
                #     #         prod_file.write(",\n")
                # prod_file.write("\n]")

    def entry_old_work(self):
        # with open("products/product.json", "r+") as prod_file, open(
        #     "products/category.json", "r"
        # ) as cat_file, open(f"links/air_jordan.json", "r") as links_file, open(
        #     "products/image.json", "r+"
        # ) as img_file:
        with open("products/product.json", "r+") as prod_file, open(
            "products/category.json", "r"
        ) as cat_file, open(f"links/all_links.json", "r") as links_file, open(
            "products/image.json", "a"
        ) as img_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # ) as cat_file, open(f"links/all_links.json", "r") as links_file:
            # self.get_global_img_id()
            urls = json.load(links_file)
            self.cats = json.load(cat_file)

            img_file.write("[\n")
            try:
                data_from_file = json.load(prod_file)
                if len(data_from_file) == 0:
                    prod_file.write("[\n")
                    self.global_id = 1
                else:
                    self.global_id = len(data_from_file) + 1
            except Exception as e:
                print("askdjfahsdfiuhasudfashdfuahsdfuhasufhsafas", e)
                prod_file.write("[\n")
                self.global_id = 1

            # self.global_id = self.load_id()
            # if self.global_id == 1:
            #     prod_file.write("[\n")

            data_generator = self.get_all_details(urls)
            for rec_id, record in enumerate(data_generator, start=self.global_id):
                print("GET_ID", rec_id)
                try:
                    n = {
                        "model": "products.product",
                        "pk": rec_id,
                        "fields": {
                            # "brand": [2, 17, 18],
                            "brand": record["brand"],
                            "name": record["name"],
                            # "description": record["description"],
                            "price": record["price"],
                            "is_active": record["is_active"],
                            "slug": record["slug"],
                            "data": {
                                "description": record["description"],
                                "sku": record["sku"],
                                "year released": record["year_released"],
                                "colour": record["colour"],
                            },
                            "countries": [1],
                        },
                    }
                    json.dump(n, prod_file, indent=2, ensure_ascii=False)
                    if self.global_id > 0:
                        prod_file.write(",\n")

                    self.save_img_json(record["thumb_images"], rec_id)

                    # self.global_img_id += 1
                except:
                    n = {"pk": rec_id, "status": False, "url": record}
                    json.dump(n, prod_file, indent=2, ensure_ascii=False)
                    # prod_file.write("\n]")
                    # self.global_id += 1
                # except:
                #     n = {"pk": rec_id + 1, "url": record}
                #     self.global_id += 1
                # finally:
                #     json.dump(n, prod_file, indent=2, ensure_ascii=False)
                #     self.save_id()
                #     if self.global_id > 1:
                #         prod_file.write(",\n")
            prod_file.write("\n]")

    @staticmethod
    # def check_dir(brand: str, size: str, name: str):
    #     """size: orig | lg | md | sm | tn"""
    #     current_path_directory = Path(__file__).resolve().parent
    #     # print(current_path_directory)
    #     new_directory = current_path_directory / "products" / "product_images"
    #     new_directory = new_directory / brand / size / name
    #     new_directory.mkdir(
    #         parents=True,
    #         exist_ok=True,
    #     )
    #     return new_directory
    def check_dir(brand: str, size: str):
        """size: orig | lg | md | sm | tn"""
        current_path_directory = Path(__file__).resolve().parent
        # print(current_path_directory)
        new_directory = current_path_directory / "products" / "product_images"
        new_directory = new_directory / brand / size
        new_directory.mkdir(
            parents=True,
            exist_ok=True,
        )
        return new_directory

    def load_id(self):
        try:
            # Пытаемся прочитать значение из файла
            with open("id.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            # Если файл не найден или содержит некорректные данные, возвращаем 0
            return 1

    def save_id(self):
        # Сохраняем текущее значение ID в файл
        with open("id.txt", "w") as file:
            file.write(str(self.global_id))

    def tr(self):
        with open("PRODUCT_IMAGES.json", "r+") as link_file:
        # with open("PRODUCT_IMAGES.json", "r") as link_file, open("44.json", "w") as f:
            links = json.load(link_file)

            r = 1
            for id, l in enumerate(links, start=1):
                if l['fields']["url"].startswith("https://www.laced.com"):
                    self.close_modals(l['fields']["url"])
                    print(f"ID: {id} -", r)
                    r += 1
                    thumb_images = self.driver.find_elements(
                        By.CSS_SELECTOR, "button.product-thumbs__item img"
                    )
                    # for i in thumb_images:
                    l["model"] = "products.image"
                    l["pk"] = 0
                    l["fields"] = {
                        "product": l["fields"]['product'],
                        "image": thumb_images[0].get_attribute("src"),
                        "lg_image": None,
                        "md_image": None,
                        "sm_image": None,
                        "tn_image": None,
                    }
                    
            # Перемещаем указатель в начало файла
            link_file.seek(0)

            # Очищаем содержимое файла
            link_file.truncate()
            json.dump(links, link_file, indent=2)
            # json.dump(links, f, indent=2)
                        # f.write(",\n")

    @staticmethod
    def find_object_by_key_value(value):
        with open("PRODUCTS.json", 'r') as fp:
            products = json.load(fp)

            for obj in products:
                if obj.get('pk') == int(value):
                    return obj
            return None
            

    def dl_tr(self):
        with open("PRODUCT_IMAGES.json", 'r') as fi, open("44.json", 'a') as f4:
            links = json.load(fi)

            start = 0
            a = 1
            b = 1
            name = ''
            for id, l in enumerate(links[start:], start=start):
                print("ID", id)
                # ip = self.change_ip()
                # print("IP", ip)

                pk = l['fields']['product']
                prod = self.find_object_by_key_value(pk)
                if prod['fields']['slug'] == name:
                    b += 1 
                else:
                    b = 1
                name = prod['fields']['slug']
                try:
                    extension = re.search(r".(\w+)\?", l['fields']['url']).group(1)

                    if 2 in prod['fields']['brand']:
                        brand_name = "Air Jordan"
                    if 3 in prod['fields']['brand']:
                        brand_name = "Nike"
                    if 4 in prod['fields']['brand']:
                        brand_name = "New Balance"
                    if 5 in prod['fields']['brand']:
                        brand_name = "Adidas"
                    if 6 in prod['fields']['brand']:
                        brand_name = "Yeezy"
                    if 7 in prod['fields']['brand']:
                        brand_name = "Asics"
                    if 8 in prod['fields']['brand']:
                        brand_name = "Crocs"
                    if 9 in prod['fields']['brand']:
                        brand_name = "UGG"
                    if 10 in prod['fields']['brand']:
                        brand_name = "Converse"
                    if 11 in prod['fields']['brand']:
                        brand_name = "On-Running"

                    filepath = f"images/Laced/{brand_name}/{name}-{b}.{extension}"
                    print(filepath)
                    url = l['fields']['url'].split("?")[0]
                    

                    # r = requests.get(url, proxies=ip)
                    # print(r.status_code)
                    # if r.status_code == 200:
                    #     with open(filepath, 'wb') as f:
                    #         f.write(r.content)

                    # self._time()
                    n = {
                        "model": "products.image",
                        "pk": a,
                        "fields": {
                            "product": pk,
                            "image": filepath,
                            "url": url,
                            "status": None
                        }
                    }
                    json.dump(n, f4, indent=2)
                    a += 1
                    if start >= 0:
                        f4.write(",\n")
                except:
                    pass
                
    def dl(self):
        with open("44.json", 'r+') as fi:
            links = json.load(fi)
            
            start = 200
            s = 0
            # while True:
                # for id, l in enumerate(links[99:]):
                #     s += 1
                #     if s >= start:
                #         fi.seek(0)
                #         json.dump(links, fi, indent=2)
                #         fi.truncate()
                #         break
            for id, l in enumerate(links[1000:2000]):
                print("ID", id+1)
                try:
                    # if l['fields']['status'] == None:
                    if l['fields']['status'] is not True:
                        ip = self.change_ip()
                        print('IP', ip)
                        print('URL', l['fields']['url'])
                        r = requests.get(l['fields']['url'], proxies = { "http" : ip })
                        print(r.status_code)

                        directory, filename = os.path.split(l['fields']['image'])
                        current_path_directory = Path(__file__).resolve().parent
                        new_directory = current_path_directory / directory
                        new_directory.mkdir(
                            parents=True,
                            exist_ok=True,
                        )

                        if r.status_code == 200:
                            with open(f"{new_directory}/{filename}", 'wb') as f:
                                f.write(r.content)

                        l['fields']['status'] = True
                        self._time()
                except:
                    l['fields']['status'] = False
                    pass
                
            fi.seek(0)
            json.dump(links, fi, indent=2)
            fi.truncate()


    # def __fetch_sizes(self, sku_ls):
        # for i in sku_ls:
        #     try:
        #         self.close_modals(f"https://www.laced.com/account/selling/new/{i}")
        #         time.sleep(random.uniform(4, 8))
        #         select_element = self.driver.find_element(By.ID, 'sale_collection_size_conversion')

        #         select = Select(select_element)
                
        #         options = [x.text for x in select.options]
        #         print()
        #         print('getting', i)
        #         print('options')
        #         print(options)
        #         print()
        #         # uk_sizes = [size.split(' | ')[0].split(' ')[1] for size in options]
        #         c = [['id', 'UK', 'EU', 'US']]
        #         for x in options:
        #             n = [0]
        #             for y in x.split(' | '):
        #                 # n.append(y.split(' ')[1])
        #                 n.append(' '.join(y.split(' ')[1:]))
        #             c.append(n)

        #         # # Создаем регулярное выражение для поиска значения EU
        #         # pattern = re.compile(r'UK (\d+)')

        #         # # Используем регулярное выражение для извлечения значения EU из каждой строки
        #         # uk_sizes = [re.search(pattern, size).group(1) for size in options]

        #         # Выводим результат
        #         # print('uk_sizes')
        #         # print(c)
        #         yield c
        #     except:
        #         z = sku_ls.index(i)
        #         StopIteration(f"ALARM product pk {z}")
    def __fetch_sizes(self, file):

        for i in file:
            l = i['fields']['data']['sku']
            self.close_modals(f"https://www.laced.com/account/selling/new/{l}")
            time.sleep(random.uniform(4, 8))
            select_element = self.driver.find_element(By.ID, 'sale_collection_size_conversion')

            select = Select(select_element)
            
            options = [x.text for x in select.options]
            print()
            print('getting', i['fields']['name'])
            print('options')
            print(options)
            print()
            # uk_sizes = [size.split(' | ')[0].split(' ')[1] for size in options]
            c = [['id', 'UK', 'EU', 'US']]
            for x in options:
                n = [0]
                for y in x.split(' | '):
                    # n.append(y.split(' ')[1])
                    n.append(' '.join(y.split(' ')[1:]))
                c.append(n)

            i['fields']['data']['available_sizes'] = c

    def __login(self):
        try:
            self.close_modals("https://www.laced.com/users/sign_in")

            submit_button = self.driver.find_element(By.CSS_SELECTOR, 'form input[type="submit"]')

            # retrieve the form elements
            name_input = self.driver.find_element(By.ID, 'user_email')
            password_input = self.driver.find_element(By.ID, 'user_password')

            # filling out the form elements
            name_input.send_keys('kamil249@mail.ru')
            password_input.send_keys('HASDJ-73478Y537sjkhgsdhf')

            # submit the form and log in
            submit_button.click()
            print('logged in')
        except Exception as e:
            print('NOT LOGGED IN')   
            print(e)

    def __get_from_fetched_sizes(self, vars, ls: list):
        try:
            res_ls = []
            for v in ls:
                for t in vars:
                    if float(v) == t['fields']['data']['UK']:
                        res_ls.append(t['pk'])

            return res_ls        
        except:
            return [None]

    # def get_available_sizes(self, id, pk):
    def get_available_sizes(self):
        self.__login()
        with open(f"product.json", "r") as prod_file, open('modified3.json', 'a') as file:

            f = json.load(prod_file)
            
            # data_generator = self.__fetch_sizes(f)
            
            # for entry in enumerate(data_generator, start=pk):
            # for id, item in enumerate(data_generator):
            #     f[id]['fields']['data']['available_sizes'] = item
            #     print(id+1)
            #     json.dump(f[id], file, indent=2)
            #     file.write(",\n")
            # gy9584
            for i in f[5150:]:
                sku = i['fields']['data']['sku']
                self.close_modals(f"https://www.laced.com/account/selling/new/{sku}")
                time.sleep(random.uniform(4, 8))
                select_element = self.driver.find_element(By.ID, 'sale_collection_size_conversion')

                select = Select(select_element)
                
                options = [x.text for x in select.options]
                print()
                print('getting', i['fields']['name'])
                print('options')
                print(options)
                print()
                # uk_sizes = [size.split(' | ')[0].split(' ')[1] for size in options]
                c = [['id', 'UK', 'EU', 'US']]
                for x in options:
                    n = [0]
                    for y in x.split(' | '):
                        # n.append(y.split(' ')[1])
                        n.append(' '.join(y.split(' ')[1:]))
                    c.append(n)

                i['fields']['data']['available_sizes'] = c

                json.dump(i, file, indent=2)
                file.write(",\n")
            # newData = json.dump(f, indent=2)

        # with open('modified2.json', 'w') as file:
        #     # write
        #     # file.write(newData)
        #     json.dump(f, file, indent=2)
            # file.write(f)
                # json.dump(n, af, indent=2)
                # for q in pk_list_of_av_vars:
                #     n = {
                #         "model": "product.availablevariationoption",
                #         "pk": id,
                #         "fields": {
                #             "product": entry[0],
                #             "variation_option": q
                #             }
                #     }
                #     json.dump(n, av_vars_file, indent=2, ensure_ascii=False)
                #     av_vars_file.write(",\n")
                #     id += 1
            
