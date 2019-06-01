import networkx as nx


G = nx.path_graph(5)
print(G.nodes)
K5 = nx.convert_node_labels_to_integers(G, first_label=2)
print(K5.nodes)
G.add_edges_from(K5.edges())
# c = list(nx.k_clique_communities(G, 4))
# print(list(c[0]))

# G = [[1, 5] , [4, 3], [6, 1]]
print(G.nodes)
print(G.edges)
from networkx.algorithms.approximation import clique
print(clique.max_clique(G))



# import networkx as nx
# from itertools import combinations
#
#
# def get_percolated_cliques(G, k):
#     perc_graph = nx.Graph()
#     cliques = list(frozenset(c) for c in nx.find_cliques(G) if len(c) >= k)
#     perc_graph.add_nodes_from(cliques)
#     # Add an edge in the clique graph for each pair of cliques that percolate
#     for c1, c2 in combinations(cliques, 2):
#         if len(c1.intersection(c2)) >= (k - 1):
#             perc_graph.add_edge(c1, c2)
#     for component in nx.connected_components(perc_graph):
#         yield(frozenset.union(*component))


# mygenerator = get_percolated_cliques(G,5)
# for i in mygenerator:
#     print(i)