from time import sleep


def cvs_read(filename):
    with open(filename, "r") as file:
        line = file.read()

        return line


def cvs_read_gn(filename):
    with open(filename, "r") as file:
        for line in file.readlines():
            yield line


if __name__ == "__main__":
    filename = "techcrunch.csv"
    print(cvs_read(filename))

    obj_gn = cvs_read_gn(filename)
    # print(obj_gn)reverseInParentheses

    # print(len(list(obj_gn)))
    # print(next(obj_gn))
    for obj in obj_gn:
        print(obj)
        sleep(1)
