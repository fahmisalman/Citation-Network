from networkx.algorithms.approximation import clique
import networkx as nx
import csv


d = []
with open('Model/Edges.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        d.append([int(row['Source']), int(row['Target'])])

G = nx.Graph()
for i in range(len(d)):
    G.add_edge(d[i][0], d[i][1])

print(clique.max_clique(G))
