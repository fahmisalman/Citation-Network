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

    data = np.array(load_csv('Data_citation.csv'))
    y = data[:, 1]
    y_u = list(set(y))

    unique, counts = np.unique(y, return_counts=True)
    d_u = dict(zip(unique, counts))

    sorted_x = sorted(d_u.items(), key=operator.itemgetter(1), reverse=False)
    for i, j in enumerate(sorted_x):
        print(i, j)


