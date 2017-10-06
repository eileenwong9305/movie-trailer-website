import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS=["G","PG","PF-13","R"]
    def __init__(self, movie_title, movie_year, movie_storyline, movie_rating,
                    movie_genre, movie_screenwriter, movie_director,
                    movie_release_date, movie_runtime, movie_poster, movie_trailer):
        self.title=movie_title
        self.year=movie_year
        self.storyline=movie_storyline
        self.rating=movie_rating
        self.genre=movie_genre
        self.screenwriter=movie_screenwriter
        self.director=movie_director
        self.release_date=movie_release_date
        self.runtime=movie_runtime
        self.poster_image_url=movie_poster
        self.trailer_youtube_url=movie_trailer

    def play_trailer(self):
        """Play youtube trailer"""
        webbrowser.open(self.trailer_youtube_url)
