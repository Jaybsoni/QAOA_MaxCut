import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np


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


def zero_pad(bit_string, max_len):
    final_bit_string = bit_string

    while len(final_bit_string) < max_len:
        final_bit_string = '0' + final_bit_string

    return final_bit_string


def brute_force_soln(graph, debug=False):
    """
    Compute the maximum cut for a weighted graph using a brute force search
    :param graph: nx.graph object, the graph we want to cut
    :param debug: bool, if true adds print statements (default = False)
    :return: tuple (float, list), the magnitude of the cut, and one group of nodes, (the rest are in other group)
    """
    node_lst = graph.nodes()
    num_nodes = len(node_lst)
    if debug:
        print(node_lst)
        print(num_nodes)

    """
    We want to split the the nodes into 2 groups, such that we maximize the weights between
    the two groups. We can assign to each node a bit (0, 1) which represents the group it is in. 
    Thus we can use this to assign a unique bit string to each cut. I make use of this below: 
    """

    max_bin = 2**(num_nodes - 1)
    optimal_cut_size = None
    optimal_group_of_nodes = []

    for num in range(0, max_bin + 1):
        bit_string = str(np.base_repr(num, base=2))
        bit_string = zero_pad(bit_string, num_nodes)
        if debug:
            print('working on: ' + bit_string)

        group_of_nodes = []
        for index, digit in enumerate(bit_string):
            if digit == '1':
                group_of_nodes.append(index)

        cut_size = nx.cut_size(graph, group_of_nodes, weight='weight')

        if (num == 0) or (cut_size > optimal_cut_size):
            optimal_cut_size = cut_size
            optimal_group_of_nodes = group_of_nodes

        if debug:
            print(' --> cutsize = {}'.format(cut_size))

    return optimal_cut_size, optimal_group_of_nodes


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
    cut, group = brute_force_soln(g, debug=True)
    print('************\n Optimal cut = {}'.format(cut))
    print('Optimal group = ', group)
    return


if __name__ == "__main__":
    main()
