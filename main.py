from antcolony import AntColonyOptimization, Nodes


if __name__ == "__main__":
    nodes = Nodes("data/data_path_nodes.txt", 1.0)
    aco = AntColonyOptimization(nodes, 1750, 1.0, 2.0, 0.3, 125, 50)
    print(aco.find_shortest_path('3653296222', '3653134376'))
