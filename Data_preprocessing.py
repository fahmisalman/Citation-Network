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
    data = load_data("Dataset/outputacm.txt")
    auth, index = get_paper(data)
    # cit = []
    # for i in range(len(auth)):
    #     # print(auth[i])
    #     if 'index' in auth[i]:
    #         cit.append([cleaning(auth[i])])
    #     elif '%' in auth[i]:
    #         cit[-1].append(cleaning(auth[i]))
    #     # elif '#c' in auth[i]:
    #     #     cit[-1].append(cleaning(auth[i]))
    #     # elif '#t' in auth[i]:
    #     #     cit[-1].append(cleaning(auth[i]))
    #     # else:
    #     #     cit.append([cleaning(auth[i])])
    # res = [['Source', 'Target']]
    # i = 0
    # while i < len(cit):
    #     if len(cit[i]) > 100:
    #         j = 4
    #         while j < len(cit[i]):
    #             res.append([cit[i][j], cit[i][0]])
    #             j += 1
    #     i += 1
    # print(len(res))
    #
    # save_data('Edges.csv', res)

    cit = []
    for i in range(len(auth)):
        # print(auth[i])
        if 'index' in auth[i]:
            cit[-1].append(cleaning(auth[i]))
        elif '#c' in auth[i]:
            cit[-1].append(cleaning(auth[i]))
        elif '#t' in auth[i]:
            cit[-1].append(cleaning(auth[i]))
        else:
            cit.append([cleaning(auth[i])])

    i = 0
    res = []

    while i < len(cit):
        if cit[i][-1] not in index:
            i += 1
        else:
            res.append(cit[i])
            i += 1
        print(i)

    save_data('Nodes.csv', res)



    

