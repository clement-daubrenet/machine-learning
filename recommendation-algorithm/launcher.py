from suggestion import MoviesSuggestion
import argparse

# Movies Recommendation Launcher
# Exemple of possible command lines :
# python launcher.py --movies 2 12 --file movies.json
# python launcher.py --movies 2 12 --file movies.json --number 15

parser = argparse.ArgumentParser(description="Movies suggestion algorithm")
parser.add_argument('-m', 
                    '--movies',
                    nargs='*',
                    type=int,
                    help='List of input movies (ids)',
                    required=True)
parser.add_argument('-f',
                    '--file',
                    type=str,
                    help="json file (movies and users database)",
                    required=True)
parser.add_argument('-n',
                    '--number',
                    default=10,
                    help='Number of output suggestions (default : 10)')
arguments = vars(parser.parse_args())

movies_suggestion = MoviesSuggestion(arguments["file"])
print "Movies suggestions : "
print movies_suggestion.get_suggestions(arguments["movies"],
                                        arguments["number"])
