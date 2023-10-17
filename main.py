import copy
import math
from random import random
import random

import numpy as np

import print_plot

record_distance = float('inf')
record_population = []
best_route_history = []
canvas_size = 300
cities = []
cities_name = []
total_city = 10
population = []

fitness = []

class City:
    def __init__(self, name, location):
        self.name = name
        self.location = location


# create cities - random location
def CreateCities(total_city):
    for i in range(total_city):
        tmp_c = City(i, (random.randint(0, canvas_size), random.randint(0, canvas_size)))
        cities.append(tmp_c)
        cities_name.append(tmp_c.name)
    return cities

#get the distance of a whole route
def GetDistanceOrder(cities, current_population):
    distance = 0
    for i in range(len(current_population)-1):
        cityA_name = current_population[i].name
        cityB_name = current_population[i+1].name

        cityA = cities[cityA_name]
        cityB = cities[cityB_name]

        distance += math.dist(cityA.location, cityB.location)
    return distance


def CalculateFtness(population):
    for i in range(len(population)):
        d = GetDistanceOrder(cities, population[i])

        if d < record_distance:
            record_distance = d
            record_population = population[i]
            best_route_history.append(record_population)
        fitness.append(1/(d+1))

def Crossover(parent1, parent2):
    start = 0
    end = round(total_city*0.75)
    if start > end:
        start, end = end, start

    child = []
    for i in range(start, end):
        child.append( parent1[i])

    for i in range(len(parent2)):
       if parent2[i] not in child:
           child.append(parent2[i])

    return child

def Mutate(child):
    i, j = random.sample(range(len(child)), 2)
    child[i], child[j] = child[j], child[i]

    return child

def GenericAlgorithm(population):
    new_population =  copy.deepcopy(population)
    for i in range(len(population)):
        parentA = random.choice(population)
        parentB = random.choice(population)

        while  parentA == parentB:
            parentB = random.choice(population)

        child = Crossover(parentA, parentB)

        if np.random.uniform() < 0.5:
            child = Mutate(child)

        child_distance = GetDistanceOrder(cities, child)
        parentA_distance = GetDistanceOrder(cities, parentA)


        if child_distance < parentA_distance:
            new_population[i] = child

    population = new_population

    return population



# create different salesmens
def CreatePopulation():
    for i in range(20):
        population.append(random.sample( cities, len(cities) ))



if __name__ == "__main__":
    CreateCities(total_city)
    CreatePopulation()

    for i in range(20000):
        population = GenericAlgorithm(population)

    min_distance = float('inf')
    best_route_history = []

    for i in range(len(population)):
        d = GetDistanceOrder(cities, population[i])
        if d < min_distance:
            min_distance = d
            best_route_history = population[i]

    print_plot.PrintPlot(best_route_history)


