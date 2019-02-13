import re
import csv


def load_data(loc):
    f = open(loc)
    line = f.readlines()
    return line


def get_paper(data):
    paper = []
    for row in data:
        if '!' not in row and '*' not in row:
            if 'index' in row:
                paper.append(row)
            if '%' in row:
                paper.append(row)
    return paper


def cleaning(line):
    line = line.rstrip()
    line = re.sub('#', '', line)
    line = re.sub('%', '', line)
    line = re.sub('index', '', line)
    return line


def tokenize(authors):
    return authors.split(',')


def save_data(loc, data):
    with open(loc, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    data = load_data("Dataset/outputacm.txt")
    auth = get_paper(data)
    cit = []
    for i in range(len(auth)):
        if 'index' in auth[i]:
            cit.append([cleaning(auth[i])])
        else:
            cit[-1].append(cleaning(auth[i]))
    res = []
    i = 0
    while i < len(cit):
        j = 1
        while j < len(cit[i]):
            res.append([cit[i][j], cit[i][0]])
            j += 1
        i += 1

    save_data('Data_citation.csv', res)

    

