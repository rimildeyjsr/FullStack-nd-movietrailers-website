import media
import fresh_tomatoes

#contains information about the title, plot, poster and trailer for the instances of the class movie

toy_story = media.Movie("Toy Story",
                        "A story of a boy and  his toys that comem to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY" )  

harry_potter_3 = media.Movie("Harry Potter and the Prisoner of Azkaban",
                            "In his third year at Hogwarts, Harry Potter learns that Sirius Black has escaped from the Azkaban prison and is planning to kill him.",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",
                            "https://www.youtube.com/watch?v=lAxgztbYDbs")

fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them",
                               "The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png/220px-Fantastic_Beasts_and_Where_to_Find_Them_poster.png",
                               "https://www.youtube.com/watch?v=ViuDsy7yb8M")

young_victoria = media.Movie("The Young Victoria",
                            "The film portrays the early childhood, teen and the following turbulent years of a young princess who came to be known as Queen Victoria.",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcQf9QDJitHfnMHAludMKEMtqSRofXmwQhDWpSCC75KNdhUpShCC",
                            "https://www.youtube.com/watch?v=6JOq6sOGVGo")

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump, a man with a low I.Q., joins the army for service where he meets Dan and Bubba. However, he cannot stop thinking about his childhood sweetheart Jenny Curran, whose life is messed up.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

beauty_and_beast = media.Movie("Beauty and the Beast",
                               "An adaptation of the fairy tale about a monstrous-looking prince and a young woman who fall in love.",
                               "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                               "https://www.youtube.com/watch?v=OvW_L8sTu5E")

martian = media.Movie("The Martian",
                      "Mark Watney is stranded on the planet of Mars after his crew leaves him behind, presuming him to be dead due to a storm. With minimum supply, Mark struggles to keep himself alive.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8")

interstellar = media.Movie("Interstellar",
                            "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=3WzHXI5HizQ")

#array created to pass the movies as a list to the open_movies_page method
movies = [toy_story, avatar, harry_potter_3, young_victoria, forrest_gump, beauty_and_beast, martian, fantastic_beasts, interstellar]

#open_movies_page method called with the list of movies as parameter.
fresh_tomatoes.open_movies_page(movies)            