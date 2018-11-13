# Making Of Movie Class


class Movie():
    def __init__(self,
                 name,
                 storyline,
                 image,
                 trailer):
        self.title = name
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
