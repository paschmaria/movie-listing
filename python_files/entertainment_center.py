import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "images/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "images/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=-9ceBgWV8io")
# print(avatar.storyline)
# avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                            "Using Rock Music to learn",
                            "images/School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouile",
                          "A rat is a chef in Paris",
                          "images/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                              "Going back in time to meet authors",
                              "images/Midnight_in_Paris_Poster.jpg",
                              "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
                          "A Real Reality TV Show",
                          "images/The_Hunger_Games_cover.jpg",
                          "https://www.youtube.com/watch?v=PbA63a7H0bo")

# You can create multiple instances of a class. When you create an instance of a class, the class' constructor gets called. This is essentially the init method of the class. Here all the data associated with the instance is initialized.

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)