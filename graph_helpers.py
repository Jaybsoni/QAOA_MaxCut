import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


class Edges:
    def __init__(self, start_node, end_node):
        self.snode = start_node
        self.enode = end_node


def main():
    lst_of_edges = [Edges(0, 1), Edges(1, 2), Edges(2, 0), Edges(2, 3)]
    G = nx.Graph()

    for edge in lst_of_edges:
        G.add_edge(str(edge.snode), str(edge.enode))

    nx.draw(G)
    plt.show()
    return


if __name__ == "__main__":
    main()
