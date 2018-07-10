import fresh_tomatoes

import media

# Instances of class Movie.
the_force_awakens = media.Movie("The Force Awakens",
                                "Thirty years after the defeat of the  \
                                Galactic Empire, the galaxy faces a new  \
                                threat from the evil Kylo Ren and the First  \
                                Order.",
                                "http://t0.gstatic.com/images?q=tbn:ANd9GcT6nGxj1D4P-9EiVSY32sb6Ql-XQrbeK5FgM37UI6QxcZwfcfVw",  # NOQA
                                "https://youtu.be/sGbxmsDFVnE")

the_last_jedi = media.Movie("The Last Jedi",
                            "Luke Skywalker's peaceful and solitary existence \
                            gets upended when he encounters Rey, a young  \
                            woman who shows strong signs of the Force.",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcRgcIU4MKHZkZNeDt_tAewyfwX7PAmSdj_7wdg_FInkZw8Um9F_",  # NOQA
                            "https://youtu.be/Q0CbN8sfihY")

rogue_one = media.Movie("Rogue One",
                        "Former scientist Galen Erso lives on a farm with his \
                        wife and young daughter, Jyn. His peaceful existence \
                        comes crashing down when the evil Orson Krennic takes \
                        him away from his beloved family. Many years later, \
                        Galen becomes the Empire's lead engineer for the most \
                        powerful weapon in the galaxy.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQ0S5JQhVplHbw7O6nt7Q0r23Bssl9UNzC-z3zy1r45_eLUB43l",  # NOQA
                        "https://youtu.be/sC9abcLLQpI")

solo_a_star_wars_story = media.Movie("Solo: A Star Wars Story",
                                     "Young Han Solo finds adventure when he \
                                     joins a gang of galactic smugglers, \
                                     including a 196-year-old Wookie named \
                                     Chewbacca.",
                                     "https://t2.gstatic.com/images?q=tbn:ANd9GcRvl3Dm7P7F6hRHmpiEF3oR5txrfUDc5Grt9RspFekcd4yS4Gzk",  # NOQA
                                     "https://youtu.be/ehJNE-MMQOc")

# List of instances of class Movie.
movies = [the_force_awakens, the_last_jedi, rogue_one, solo_a_star_wars_story]

# Takes list of movies, generates html file, and produces website
# displaying movies.
fresh_tomatoes.open_movies_page(movies)
