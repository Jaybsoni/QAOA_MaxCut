import networkx as nx
import matplotlib.pyplot as plt
import random


def random_graph_gen(max_num_nodes=5, max_num_edges=10, seed=None):
    """
    random graph generator produces a networkx.graph object

    :param max_num_nodes: int, max number of nodes in the graph
    :param max_num_edges: int, max number of edges in the graph
    :param seed: int, random seed
    :return: networkx.graph object, the randomly generated graphs
    """
    num_nodes = random.randint(2, max_num_nodes + 1)
    num_edges = random.randint(1, max_num_edges + 1)
    g = nx.gnm_random_graph(num_nodes, num_edges, seed=seed)         # generate a random graph (no weighted edges)

    edge_lst = g.edges()
    edge_attr = {}
    for index, edge in enumerate(edge_lst):
        weight = random.uniform(-10.0, 10.0)      # randomly generate weights between -10, 10
        edge_attr[edge] = {'weight': weight}      # add the weights and other attributes

    nx.set_edge_attributes(g, edge_attr)
    return g


def brute_force_soln(graph):
    
    return set_a


def main():
    g = random_graph_gen()

    # lst_of_edges = [(0, 1, {"weight": 1.5}), (1, 2, {"weight": 2}), (2, 0, {"weight": -1}), (2, 3, {"weight": -0.5})]
    # g = nx.Graph()
    # g.add_edges_from(lst_of_edges)
    # edges = g.edges()
    # labels = nx.get_edge_attributes(g, 'weight')
    # nx.draw_networkx_edge_labels(g, nx.random_layout(g), labels=labels)
    nx.draw(g, with_labels=True)
    plt.show()
    return


if __name__ == "__main__":
    main()
