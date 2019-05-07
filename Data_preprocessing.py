import re
import csv


def load_data(loc):
    f = open(loc)
    line = f.readlines()
    return line


def get_paper(data):
    paper = []
    index = []
    for row in data:
        # if '!' not in row and '*' not in row:
        if '#index' in row:
            paper.append(row)
            index.append(row)
        if '#t' in row:
            paper.append(row)
        if '#%' in row:
            paper.append(row)
        if '#*' in row:
            paper.append(row[2:-1])
        if '#c' in row:
            paper.append(row)
    return paper, index


def cleaning(line):
    line = line.rstrip()
    line = re.sub('#t', '', line)
    line = re.sub('#c', '', line)
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
    # data = load_data("Dataset/outputacm.txt")
    # auth, index = get_paper(data)
    # cit = []
    # for i in range(len(auth)):
    #     if '#index' in auth[i]:
    #         cit.append([cleaning(auth[i])])
    #     elif '#%' in auth[i]:
    #         cit[-1].append(cleaning(auth[i]))
    #     # elif '#c' in auth[i]:
    #     #     cit[-1].append(cleaning(auth[i]))
    #     # elif '#t' in auth[i]:
    #     #     cit[-1].append(cleaning(auth[i]))
    #     # else:
    #     #     cit.append([cleaning(auth[i])])
    # res = [['Source', 'Target']]
    # # i = 0
    # # while i < len(cit):
    # #     if len(cit[i]) > 100:
    # #     j = 1
    # #     while j < len(cit[i]):
    # #         res.append([cit[i][0], cit[i][j]])
    # #         j += 1
    # #     i += 1
    # temp = {}
    # for i in range(len(cit)):
    #     for j in range(len(cit[i])):
    #         if cit[i][j] not in temp.keys():
    #             temp[cit[i][j]] = 1
    #         else:
    #             temp[cit[i][j]] += 1
    #
    # print(sorted(temp.items(), key=lambda kv: (kv[1], kv[0])))
    # temp2 = []
    # for item in temp.items():
    #     if item[1] > 400:
    #         temp2.append(item[0])
    #
    # print(len(temp2))
    #
    # i = 0
    # while i < len(cit):
    #     j = 1
    #     while j < len(cit[i]):
    #         if cit[i][j] in temp2:
    #             res.append([cit[i][0], cit[i][j]])
    #         j += 1
    #     i += 1
    #
    # print(len(res))
    # save_data('Edges.csv', res)

    # --------------------------------

    # cit = []
    # for i in range(len(auth)):
    #     if '#index' in auth[i]:
    #         cit[-1].append(cleaning(auth[i]))
    #     elif '#c' in auth[i]:
    #         cit[-1].append(cleaning(auth[i]))
    #     elif '#t' in auth[i]:
    #         cit[-1].append(cleaning(auth[i]))
    #     elif '#%' in auth[i]:
    #         pass
    #     else:
    #         cit.append([cleaning(auth[i])])
    #
    # save_data('Nodes.csv', cit)
    #
    # # --------------------------------
    #
    # index = []
    # with open('Nodes.csv') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         index.append(row[-1])
    #
    # save_data('Index.csv', [index])

    # --------------------------------

    nodes = []
    with open('Edges.csv') as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            for i in range(len(row)):
                nodes.append(row[i])
            # nodes.append(row[1])

    index = []
    with open('Index.csv') as f:
        r = csv.reader(f)
        for row in r:
            for i in range(len(row)):
                index.append(row[i])

    temp = []
    with open('Nodes.csv') as f:
        r = csv.reader(f)
        for row in r:
            temp.append(row)

    res = [['Title', 'Year', 'Categorize', 'Id']]
    nodes = list(set(nodes))
    for i in range(len(nodes)):
        if nodes[i] in index:
            res.append(temp[index.index(nodes[i])])
        else:
            res.append(None)

    save_data('Result.csv', res)
