import json
from random import choice


class ExceptionGetProxy(Exception):
    """Proxy file path error."""



class Proxy:
    @classmethod
    def get(cls, path):
        try:
            with open(path) as json_file:
                list_proxy = json.load(json_file)

                print(f"rest proxy url: {len(list_proxy)}")
                if len(list_proxy) <= 8:
                    raise ExceptionGetProxy(f"Empty proxy list, rest {len(list_proxy)}")

                # get random ip
                random_dict = choice(list_proxy)
                ip, port = random_dict["ip"], random_dict["port"]

                # # remove the selected item and save
                # list_proxy.remove(random_dict)
                # with open(path, "w") as new_file:
                #     json.dump(list_proxy, new_file, indent=2)
                #
                return f"{ip}:{port}"
        except FileNotFoundError:
            raise ExceptionGetProxy("Not file exsists")
