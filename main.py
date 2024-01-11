from antcolony import AntColonyOptimization, Nodes


if __name__ == "__main__":
    nodes = Nodes("data/data_path_nodes.txt")
    aco = AntColonyOptimization(nodes, 1000, 0.8, 0.2, 0.3, 100, 0)
    print(aco.find_shortest_path('3653296222', '3653134376'))
