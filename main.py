from antcolony import AntColonyOptimization, Nodes


if __name__ == "__main__":
    nodes = Nodes("data/data_path_nodes.txt")
    aco = AntColonyOptimization(nodes, 1000, 0.8, 0.2, 0.3, 100, 0)
    print(aco.find_shortest_path('3653296222', '3653134376'))
    # print(aco.find_shortest_path('2316793331', '2316793362'))
    # print(nodes['2316793362', '2316793331'])
    # for id in ('2', '3', '5', '6' ,'9'):
    #     print(nodes[id])
