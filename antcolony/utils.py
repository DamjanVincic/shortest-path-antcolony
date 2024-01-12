import math
import random
from typing import Dict


def edge_coefficient(pheromones: float, distance: float, alpha: float, beta: float) -> float:
    return math.pow(pheromones, alpha)*math.pow(1/distance, beta)


def roulette_selection(coefficients: Dict[str, float]) -> str:
    total_coefficients = sum(coefficients[k] for k in coefficients)
    relative_coefficients = {}

    #Calculate coefficients relative to the sum of all coefficients
    for k in coefficients:
        relative_coefficients[k] = coefficients[k]/total_coefficients

    current_sum = 0
    cumulative_probability = {} #Every node is assigned range proportional to its relative coefficient
    for k in coefficients:
        current_sum += relative_coefficients[k]
        cumulative_probability[k] = current_sum

    rand = random.random() # Random number between 0 and 1
    for k in cumulative_probability:
        if rand <= cumulative_probability[k]: # Selected node is one in which's range random number falls
            return k
