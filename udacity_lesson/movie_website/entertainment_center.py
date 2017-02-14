import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        123,
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/zh/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        200,
                     "A marine on a alien planet",
                     "https://upload.wikimedia.org/wikipedia/zh/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=aVdO-cx-McA")

#print(avatar.storyline)
#avatar.show_trailer()

dahuaxiyou = media.Movie("A Chinese Odyssey",
                            122,
						 "A monkey king's love story",
						 "https://upload.wikimedia.org/wikipedia/zh/0/0c/A_Chinese_Odyssey_2.jpg",
						 "https://www.youtube.com/watch?v=LnNKNApIOAo")
#print(dahuaxiyou.storyline)

#dahuaxiyou.show_trailer()
lengeds_of_the_fall = media.Movie("Legends of the Fall",
                                    222,
								  "Three brothers and their father living in the wilderness and plains of Montana in the early 20th century and how their lives are affected by nature, history, war and love.",
								  "https://upload.wikimedia.org/wikipedia/en/1/1d/Legendsoffallposter.jpg",
								  "https://www.youtube.com/watch?v=ocAeBZdSDWg")
movies = [toy_story, avatar, dahuaxiyou, lengeds_of_the_fall]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__module__)
print(media.Movie.__name__)
print(media.Movie.__dict__)
print(media.Movie.__bases__)
