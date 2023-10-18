import random

from City import City


def CreateCities(total_city, canvas_size):
    cities = []
    for i in range(total_city):
        tmp_c = City(i, (random.randint(0, canvas_size), random.randint(0, canvas_size)))
        cities.append(tmp_c)
    return cities

# create different salesmens
def CreatePopulation(cities):
    population = []
    for i in range(20):
        new_p=random.sample( cities, len(cities) )
        start_city = new_p[0]
        new_p.append(start_city)
        population.append(new_p)

    return population

