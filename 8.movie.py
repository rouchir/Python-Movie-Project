#  Here,I'm Importing Another Two Files In This
import fresh_tomatoes
import movieclass

# Creating Instances Of Movie Class .
inception = movieclass.Movie(
    "Inception",
    """A thief, who steals corporate secrets through the use of dream-sharing ,
    is given the inverse task of planting an idea into the mind of a CEO""",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=ATCN00oVMNM"
  )

oldboy = movieclass.Movie(
    "Oldboy",
    """After being kidnapped and imprisoned for fifteen years,
    Oh Dae-Su is released, only to find that he must find his captor""",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Oldboykoreanposter.jpg/220px-Oldboykoreanposter.jpg",
    "https://www.youtube.com/watch?v=MOchcLyeU94"
  )


madmax = movieclass.Movie(
    "Mad Max : Fury Road",
    """A woman rebels against a tyrannical ruler in Australia in search for her
    home-land with the help of a group of female prisoners, and a drifter""",
    "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
    "https://www.youtube.com/watch?v=hEJnMQG9ev8"
  )

ocean11 = movieclass.Movie(
    "Ocean's 11",
    "Danny Ocean and his eleven  plan to rob three Las Vegas casinos .",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Ocean%27s_Eleven_2001_Poster.jpg/220px-Ocean%27s_Eleven_2001_Poster.jpg",
    "https://www.youtube.com/watch?v=C6vD5cRhw14"
  )

memento = movieclass.Movie(
    "Memento",
    """A man juggles searching for his wife's murderer and
    keeping his short-term memory loss from being an obstacle""",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Memento_poster.jpg/220px-Memento_poster.jpg",
    "https://www.youtube.com/watch?v=0vS0E9bBSL0"
  )

galaxy = movieclass.Movie(
    "Guardians Of The Galaxy",
    """A group of intergalactic criminals are forced to work together
    to stop a fanatical warrior from taking control of the universe.""",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",
    "https://www.youtube.com/watch?v=d96cjJhvlMA"
  )

# creating array of movies
movies = [
    inception,
    oldboy,
    madmax,
    ocean11,
    memento,
    galaxy
    ]

# Passing An Array
fresh_tomatoes.open_movies_page(movies)
