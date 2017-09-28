from cities import City
from heuristics import NearestNeighbour

# We define different cities (x and y coordinates)
list_of_cities = [City(3, 4), City(1, 2), City(8, 10), City(5, 5)]
nearest_neighbours = NearestNeighbour(list_of_cities)

# Launching NN algorighm
print(nearest_neighbours.execute(list_of_cities[0]))