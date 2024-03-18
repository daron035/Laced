# def generator(i):
#     yield (i)
#
# gen = generator()
#
# ls = [1, 2, 3, 4, 5]
#
#
# if __name__ == "__main__":
#     data_generator = generator
#     for i in generator:
#         a = generator(i)
#         print(a)


def generator(ls):
    for y in ls:
        yield y


ls_links = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    data_gen = generator(ls_links)

    for i in range(len(ls_links)):
        try:
            data = next(data_gen)
            print(data)
        except StopIteration:
            print("Task")

    try:
        while True:
            data = next(data_gen)
            print(data)
    except StopIteration:
        print("Task")

    print("23412341234211")
