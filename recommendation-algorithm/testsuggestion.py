import unittest
from suggestion import MoviesSuggestion


class TestMoviesSuggestion(unittest.TestCase):
    def setUp(self):
        """
        All the tests are performed with a test database called
        movies-test.json. It contains only 3 movies and 3 users.
        """
        self.movies_suggestion = MoviesSuggestion("movies-test.json")

    def test_read_json(self):
        """
        Testing the json reading method for the test json file.
        i.e: checking the shape of the resulting data structures.
        """
        expected_movies_database = ("{u'1': u'Toy Story (1995)',"
                                    " u'3': u'Twelve Monkeys (1995)',"
                                    " u'2': u'GoldenEye (1995)'}")
        expected_users_preferences = ("[{u'movies': [2, 3], u'user_id': 1},"
                                      " {u'movies': [1], u'user_id': 2},"
                                      " {u'movies': [1, 2], u'user_id': 3}]")
        self.assertEqual([str(self.movies_suggestion.movies_database),
                          str(self.movies_suggestion.users_preferences)],
                         [expected_movies_database,
                          expected_users_preferences])

    def test_tanimoto_coefficient(self):
        """
        Testing computations of all possible Tanimoto coefficients.
        i.e: checking that all pairs of the test database
        give right values.
        """
        one_two = self.movies_suggestion.tanimoto_coefficient(1, 2)
        two_three = self.movies_suggestion.tanimoto_coefficient(2, 3)
        one_three = self.movies_suggestion.tanimoto_coefficient(1, 3)
        expected_coefficients = [0.3333333333333333, 0.5, 0.0]
        self.assertEqual([one_two, two_three, one_three],
                         expected_coefficients)

    def test_affinities(self):
        """
        Testing the shape of the coefficient dictionaries for movies
        in the case of no prior computation.
        i.e : we test the first iteration of the loop over the input list.
        """
        m1_affinities = self.movies_suggestion.get_movies_coefficients(1, {})
        m2_affinities = self.movies_suggestion.get_movies_coefficients(2, {})
        m3_affinities = self.movies_suggestion.get_movies_coefficients(3, {})
        expected_affinities_m1 = "{u'3': 0.0, u'2': 0.3333333333333333}"
        expected_affinities_m2 = "{u'1': 0.3333333333333333, u'3': 0.5}"
        expected_affinities_m3 = "{u'1': 0.0, u'2': 0.5}"
        self.assertEqual([str(m1_affinities),
                          str(m2_affinities),
                          str(m3_affinities)],
                         [expected_affinities_m1,
                         expected_affinities_m2,
                         expected_affinities_m3])

    def test_affinities_with_previous(self):

        """
        Testing the shape of the coefficient dictionary for a given movie
        in the case of a prior computation.
        i.e: represents any iteration over the input list.
        Verifies that the maximum of each coefficient is taken.
        """
        prev = {u'3': 1.0, u'2': 0.0}
        m1_affinities = self.movies_suggestion.get_movies_coefficients(1,
                                                                       prev)
        expected_m1_affinities = "{u'3': 1.0, u'2': 0.3333333333333333}"
        self.assertEqual(str(m1_affinities),
                         expected_m1_affinities)

    def test_get_suggestions(self):
        """
        Test the overall algorithm by checking that the right
        suggestions are given after watching movie 1 or 2.
        """
        suggestions_movie_1 = self.movies_suggestion.get_suggestions([1], 2)
        suggestions_movie_2 = self.movies_suggestion.get_suggestions([2], 2)
        self.assertEqual([suggestions_movie_1, suggestions_movie_2],
                         [[2, 3], [3, 1]])
