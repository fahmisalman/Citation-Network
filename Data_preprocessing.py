import os


def load_data(loc):
    f = open(loc)
    line = f.readlines()
    return line


def get_author(data):
    authors = []
    for row in data:
        if '@' in row:
            authors.append(row)
    return authors


if __name__ == '__main__':
    data = load_data("Dataset/outputacm.txt")
