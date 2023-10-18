import copy
import math
from random import random
import random
import numpy as np

import print_plot


class GenericAlgo:
    def __init__(self, total_city, canvas_size, cities, population):
        self.total_city = total_city
        self.canvas_size = canvas_size
        self.cities = cities
        self.population = population

    def Crossover(self, parent1, parent2):
        start = 0
        end = round(len(parent1) * 0.5)

        child = []
        for i in range(start, end):
            child.append(parent1[i])

        for i in range(len(parent2)):
            if parent2[i] not in child:
                child.append(parent2[i])


        firts_city = child[0]
        child.append(firts_city)

        return child

    def Mutate(self, child):
        i = random.randint(1, len(self.cities)-2)
        j = random.randint(1, len(self.cities)-2)
        child[i], child[j] = child[j], child[i]

        return child

    def GetDistanceOrder(self, cities, current_population):
        distance = 0
        for i in range(len(current_population) - 1):
            cityA_name = current_population[i].name
            cityB_name = current_population[i + 1].name

            cityA = cities[cityA_name]
            cityB = cities[cityB_name]

            distance += math.sqrt((cityA.location[0] - cityB.location[0]) ** 2 + (cityA.location[1] - cityB.location[1]) ** 2)
        return distance

    def GenericAlgorithm(self, population):

        # get a new population
        new_population = copy.deepcopy(population)
        min_distance = float('inf')

        # for each individual in population be an A parent
        for i in range(len(self.population)):
            parentA = self.population[i]
            parentB = random.choice(self.population[:len(self.population)-2])

            # be sure that parrents are different
            while parentA == parentB:
                parentB = random.choice(self.population[:len(self.population)-2])

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

        population = new_population
        self.population = population

        index = 0
        distances = []
        for i in range(len(self.population)):
            d = self.GetDistanceOrder(self.cities, self.population[i])
            distances.append(d)
            if d < min_distance:
                min_distance = d

        print("All distances: "+str(sum(distances)))

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
