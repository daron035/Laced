import json
from pprint import pprint


if __name__ == "__main__":
    # class G_6_82:
    #     gen_ex = ["Л", "П", "Д", "К", "У", "Д", "К", "Х"]
    #
    #     ncs = [0.5, 1, 2.5, 6, 10, 16]
    #     d = [
    #         [2, 3, 4],
    #         [2, 3, 4, 5],
    #         [3, 4, 5, 6, 8],
    #         [4, 5, 6, 8, 10],
    #         [5, 6, 8, 10, 12],
    #         [5, 6, 8, 10, 12],
    #     ]
    #     ex = ["Л", "П", "Д", "К", "У", "Д", "К", "Х"]
    #     mateiral = ["М", "ЛТ"]
    #     ncs = [0.5, 1, 2.5, 6, 10, 16]
    #
    #     table = [
    #         [
    #             "Номинальное сечение",
    #             "Диаметр контактного стержня",
    #             "Исполнение",
    #             "Материал",
    #             "Шифр покрытия",
    #         ],
    #         [0.5, 1, 2.5, 6, 10, 16],
    #         [
    #             [2, 3, 4],
    #             [2, 3, 4, 5],
    #             [3, 4, 5, 6, 8],
    #             [4, 5, 6, 8, 10],
    #             [5, 6, 8, 10, 12],
    #             [5, 6, 8, 10, 12],
    #         ],
    #         [["Л", "П", "Д", "К", "У", "Д", "К", "Х"]],
    #         [None],
    #     ]
    #
    #     def __init__(self, ncs, d, ex, mat, code=None):
    #         self.ncs = ncs
    #         self.d = d
    #         self.ex = ex
    #         self.mat = mat
    #         self.code = code
    #
    #         self.table = G_6_82.table[1:]
    #         self.t_ncs = G_6_82.table[1]
    #         self.t_d = G_6_82.table[2]
    #         self.t_ = G_6_82.table[2]
    #
    # a = G_6_82(3, 3, 3, 3)
    # # print(a.__dir__())
    # print(a.table)

    import pandas as pd

    # Sample DataFrames
    df1 = pd.DataFrame(
        {
            "ID": [1, 2, 3, 4],
            "Name": ["Alice", "Bob", "Charlie", "David"],
        }
    )
    # print(df1)

    df2 = pd.DataFrame(
        {
            "ID": [2, 3, 5],
            "Age": [25, 30, 22],
        }
    )

    # Merge DataFrames on the 'ID' column
    merged_df = pd.merge(df1, df2, on="ID", how="inner")

    # Display the result
    print(merged_df)


# import pandas as pd
#
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [[28, 24, 32], [1], [823]],
#     "Occupation": ["Engineer", "Designer", "Writer"],
# }
# df = pd.DataFrame(data)
# print()
# print(df)
# # print(df.at[0, "Age"])
#
# d = [
#     ["Name", "Age", "Occupation", "Execution"],
#     ["Alice", [28, 24, 32], "Engineer"],
#     ["Bob", 1, "Designer"],
#     ["Charlie", 823, "Writer"],
#     ["Л", "П", "Д", "К", "У", "Д", "К", "Х"],
# ]
# print()
# for id, item in enumerate(d):
#     if id == 0:
#         print(", ".join(item))
#     print(item)
