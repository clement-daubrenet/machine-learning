import json
import operator


class MoviesSuggestion(object):
    """
    This class suggests movies to an end user based on :
    A database of all possible movies and users history
    e.g : movies.json
    An input list of movies (ids) the end user already watched
    e.g : [2,4,5]
    """
    def __init__(self, json_movies_path):
        """
        Setting up the data structures by reading the json file
        :movies_database: a list of all possible movies
        :users_preferences: movies watched per user
        """
        self.movies_database, self.users_preferences = \
            self.read_json(json_movies_path)

    def get_suggestions(self,
                        input_movies,
                        number_of_suggestions):
        """
        Returns suggestions of movies to the end user in a decreasing
        order of relevance.
        For each movie of the input list, we compute and update(max)
        an affinity dictionary with all movies of the database.
        In the end, we take the best grades in the final dictionary.
        n.b : This updating method is used to loop only
        once and save a bit of time complexity
        """
        movies_coefficients = {}
        for movie_id in input_movies:
            updated_coefficients = self.get_movies_coefficients(
                int(movie_id), movies_coefficients)
            movies_coefficients = updated_coefficients
        sorted_suggestions = sorted(movies_coefficients.items(),
                                    key=operator.itemgetter(1),
                                    reverse=True)[:int(number_of_suggestions)]
        # returning a list of the best graded movies excluding inputs
        ranked_list = map(lambda movie: int(movie[0]), sorted_suggestions)
        return [movie for movie in ranked_list if movie not in input_movies]

    def get_movies_coefficients(self, movie_to_grade, former_coefficients):
        """
        Returns an affinity dictionary for a given movie with
        all database movies (keys) based on updated Tanimoto
        coefficients (values).
        i.e: output shape for movie 1 in a 3 movies database :
        {u'3' : 0.0, u'2' : 0.5}
        """
        updated_coefficients = {}
        for id_movie in self.movies_database.iterkeys():
            if int(id_movie) != movie_to_grade:
                current_tanimoto_coefficient = self.tanimoto_coefficient(
                    int(id_movie), movie_to_grade)
                if id_movie in former_coefficients.keys():
                    former_tanimoto_coefficient = former_coefficients[id_movie]
                    # the important line : we keep the maximum coefficient only
                    updated_coefficients[id_movie] = max(
                        former_tanimoto_coefficient,
                        current_tanimoto_coefficient)
                else:
                    updated_coefficients[id_movie] = \
                        current_tanimoto_coefficient
        return updated_coefficients

    def tanimoto_coefficient(self, movie_1, movie_2):
        """
        Computes the Tanimoto coefficient for two distinct movies.
        The highest the coefficient is, the more similar the two movies are.
        n.b : the general formula is T(item_a,item_b) = a/a+b-ab
        a is the number of times item_a appeared in users history
        b is the number of times item_b appeared in users history
        ab is the number of times a and b appeared together in users history
        """
        movie_1_cnt, movie_2_cnt, movie_12_cnt = (0, 0, 0)
        for user_preference in self.users_preferences:
            user_movies = user_preference["movies"]
            if movie_1 in user_movies:
                movie_1_cnt += 1
            if movie_2 in user_movies:
                movie_2_cnt += 1
            if (movie_1 in user_movies) and (movie_2 in user_movies):
                movie_12_cnt += 1
        return float(movie_12_cnt)/(movie_1_cnt + movie_2_cnt - movie_12_cnt)

    @staticmethod
    def read_json(json_file):
        """
        Reads json file to transform it into two data structures :
        movies_database and users_preferences
        """
        data = json.loads(open(json_file).read())
        users_preferences = data["users"]
        movies_database = data["movies"]
        return movies_database, users_preferences
