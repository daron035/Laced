import json


def sort_files(file_1, file_2, brand_name):
    with open(f"links/{file_1}.json", "r") as f1, open(
        f"links/{file_2}.json", "r"
    ) as f2:
        ls1 = json.load(f1)
        ls2 = json.load(f2)

    result_ls = list(set(ls1 + ls2))
    print(len(result_ls))

    with open(f"links/{brand_name}.json", "w") as fr:
        json.dump(result_ls, fr, indent=2, ensure_ascii=False)
