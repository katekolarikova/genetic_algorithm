import copy
import math
from random import random
import random

import numpy as np

import print_plot
from City import City
from generic_algo import GenericAlgo
from initial import CreateCities, CreatePopulation

# create cities - random location

if __name__ == "__main__":
    record_distance = float('inf')
    canvas_size = 300
    total_city = 15

    cities = CreateCities(total_city, canvas_size)
    population = CreatePopulation(cities)

    algo = GenericAlgo(total_city+1, canvas_size, cities, population)
    tmp_p = algo.RunGeneticAlgorithm(20)
    print_plot.PrintPlot(tmp_p)

