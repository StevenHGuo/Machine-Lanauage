import webbrowser

class Movie():
    """  This is a class for the movie! You can see some basic information by it! """

    """
    Initialize the basic information of the object
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        # The title of the movie
        self.title = title
        # The address of poster image for the movie
        self.poster_image_url = poster_image_url
        # The trailer of the movie
        self.trailer_youtube_url = trailer_youtube_url


    """
    Open the trailer of instance movie object in the browser
    """
    def show_trailer(self):
        webbrowser.open(self.poster_image)
