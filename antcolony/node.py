import math


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        if not isinstance(other, type(self)):
            print("Can't compare these objects")
            return

        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
