class Movie():
    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # The last four are instance variables

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# A class can have both data and methods.
# The constructor uses the keyword "self". All the cariables associated with a specific instance are called "Instance Variables". These are unique to an object and called be accessed using the "self" keyword of the class.
# All the functions inside the class that are associated with an instance and have the first argument as self are called "Instance Methods".
