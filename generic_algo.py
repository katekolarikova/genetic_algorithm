import copy
import math
from random import random
import random
import numpy as np


class GenericAlgo:
    def __init__(self, total_city, canvas_size, cities, population):
        self.total_city = total_city
        self.canvas_size = canvas_size
        self.cities = cities
        self.population = population

    def Crossover(self, parent1, parent2):
        start = 0
        end = round(self.total_city * 0.5)

        child = []
        for i in range(start, end):
            child.append(parent1[i])

        for i in range(len(parent2)):
            if parent2[i] not in child:
                child.append(parent2[i])

        return child

    def Mutate(self, child):
        i, j = random.sample(range(len(child)), 2)
        child[i], child[j] = child[j], child[i]

        return child

    def GetDistanceOrder(self, cities, current_population):
        distance = 0
        for i in range(len(current_population) - 1):
            cityA_name = current_population[i].name
            cityB_name = current_population[i + 1].name

            cityA = cities[cityA_name]
            cityB = cities[cityB_name]

            distance += math.dist(cityA.location, cityB.location)
        return distance

    def GenericAlgorithm(self, population):

        # get a new population
        new_population = copy.deepcopy(population)

        # for each individual in population be an A parent
        for i in range(len(population)):
            parentA = population[i]
            parentB = random.choice(population)

            # be sure that parrents are different
            while parentA == parentB:
                parentB = random.choice(population)

            # create a child
            child = self.Crossover(parentA, parentB)

            # mutate some of the childs
            if np.random.uniform() < 0.5:
                child = self.Mutate(child)

            # get distance of child and parentA for the whole route
            child_distance = self. GetDistanceOrder(self.cities, child)
            parentA_distance = self. GetDistanceOrder(self.cities, parentA)

            # if child is better than parentA, replace parentA with child
            if child_distance < parentA_distance:
                new_population[i] = child
                print(str(parentA_distance)+"  "+ str(child_distance))

        population = new_population
        return population


    def RunGeneticAlgorithm(self, num_generations):
        min_distance = float('inf')
        best_route_history = []

        # run genetic algorithm num_generations times
        for i in range(num_generations):
            self.population = self.GenericAlgorithm(self.population)

        # get best route from population
        for i in range(len(self.population)):
            d = self.GetDistanceOrder(self.cities, self.population[i])
            if d < min_distance:
                min_distance = d
                best_route_history = self.population[i]

        return best_route_history
