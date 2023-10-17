import copy
import math
from random import random
import random

import numpy as np

import print_plot
from City import City
from generic_algo import GenericAlgo




# create cities - random location
def CreateCities(total_city):
    cities = []
    for i in range(total_city):
        tmp_c = City(i, (random.randint(0, canvas_size), random.randint(0, canvas_size)))
        cities.append(tmp_c)
    return cities

# create different salesmens
def CreatePopulation():
    population = []
    for i in range(20):
        population.append(random.sample( cities, len(cities) ))

    return population


if __name__ == "__main__":
    record_distance = float('inf')
    canvas_size = 300
    total_city = 20

    cities = CreateCities(total_city)
    population = CreatePopulation()

    algo = GenericAlgo(total_city, canvas_size, cities, population)
    tmp_p = algo.RunGeneticAlgorithm(10000)
    print_plot.PrintPlot(tmp_p)


