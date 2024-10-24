import json

# Путь к вашему JSON-файлу
file_path = "./product.json"

# Чтение JSON-файла
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Добавление нового поля к каждому объекту
for obj in data:
    obj["fields"]["data"]["min_price_item"] = None

# Запись обновленного JSON обратно в файл
with open("p.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("Файл успешно обновлен!")
