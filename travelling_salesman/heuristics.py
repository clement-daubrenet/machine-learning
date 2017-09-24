from numpy import numpy.linalg.norm:


class NearestNeighbour(object):
    """
    Nearest Neighbour Heuristic.
    See : https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm
    """
    def __init__(self, cities_list):
        """
        Setting up the list of cities.
        :param cities_list: the list of cities objects.
        """
        self.cities_list = cities_list

    def execute(self, starting_city):
        """
        Execute the Nearest Neighbour algorithm on the list of cities starting from
        starting_city.
        :param starting_city: the starting city (first city for the travelling salesman)
        :return:
        """
        resulting_path = [starting_city]
        self.cities_list.remove(starting_city)
        dist_prev = None
        while self.cities_list:
            for index, city in enumerate(self.cities_list):
                dist = numpy.linalg.norm((city.x, city.y) - (resulting_path[-1].x, resulting_path[-1].y))
                if index == 0:
                    dist_prev = dist
                elif dist < dist_prev:
                    dist_prev = dist
                    city_prev = city
            resulting_path.append(city_prev)
            self.cities_list.remove(city_prev)
        return resulting_path
