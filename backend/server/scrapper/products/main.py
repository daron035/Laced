import json

if __name__ == "__main__":
    with open("IMG.json", "r") as f1, open("new_322323.json", "r") as f2:
        images1 = json.load(f1)
        images2 = json.load(f2)

        nl = images1 + images2
        xl = sorted(nl, key=lambda x: x['fields']['product'])
        l = []
        for i in images1:
            url = i.get("url", None)
            i['fields']['image'] = None  # Добавляем 'image': None, если 'image' отсутствует

    with open("999999.json", "w") as f:
        json.dump(xl, f, indent=2)
