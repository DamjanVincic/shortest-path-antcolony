from .nodes import Nodes
import utils


class Ant:
    def __init__(self, nodes, source, destination, alpha, beta):
        self.nodes = nodes
        self.current_node = source
        self.destination = destination
        self.alpha = alpha
        self.beta = beta
        self.path = [source]
        self.path_length = 0
        self.visited_nodes = set(source)
