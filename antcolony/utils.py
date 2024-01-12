import math
import random


def edge_coefficient(pheromones, distance, alpha, beta):
    return math.pow(pheromones, alpha)*math.pow(1/distance, beta)


def roulette_selection(coefficients):
    total_coefficients = sum(coefficients[k] for k in coefficients)
    relative_coefficients = {}

    for k in coefficients:
        relative_coefficients[k] = coefficients[k]/total_coefficients

    current_sum = 0
    cumulative_probability = {}
    for k in coefficients:
        current_sum += relative_coefficients[k]
        cumulative_probability[k] = current_sum

    rand = random.random()
    for k in cumulative_probability:
        if rand <= cumulative_probability[k]:
            return k
