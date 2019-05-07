import numpy as np
import operator
import csv


def load_csv(loc):
    d = []
    with open(loc) as f:
        reader = csv.reader(f)
        for row in reader:
            d.append(row)
    return d


if __name__ == '__main__':

    # data = np.array(load_csv('Data_citation.csv'))
    # y = data[:, 0]
    # y_u = list(set(y))
    #
    # unique, counts = np.unique(y, return_counts=True)
    # d_u = dict(zip(unique, counts))
    #
    # sorted_x = sorted(d_u.items(), key=operator.itemgetter(1), reverse=False)
    # for i, j in enumerate(sorted_x):
    #     print(i, j)

    b = [[4, 6, 7], [2], [1, 2, 7]]
    a = {}
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] not in a.keys():
                a[b[i][j]] = 1
            else:
                a[b[i][j]] += 1
    print(a)
    print(sorted(a.items(), key=lambda kv: (kv[1], kv[0])))
    for i in a.items():
        print(i)
        if i[1] > 1:
            print(i[0])
