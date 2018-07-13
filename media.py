import webbrowser

# Data structure to store favorite movies.
class Movie:
    """"Class definition for creating instances of favorite movies."""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens movie trailer.  Takes youtube trailer url as arg."""
        webbrowser.open(self.trailer_youtube_url)
