import os


def load_data(loc):
    f = open(loc)
    line = f.readlines()
    return line


if __name__ == '__main__':
    line = load_data("Dataset/outputacm.txt")
    for row in line:
        if '@' in row:
            print(row)
