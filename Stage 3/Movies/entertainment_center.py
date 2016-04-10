import fresh_tomatoes
import media


# Movies to be on the website
stardust = media.Movie("Stardust",
                       "Magic, Fantasy, Mayhem, Stardust",
                       "https://upload.wikimedia.org/wikipedia/en/6/6f/Stardust_promo_poster.jpg",
                       "https://www.youtube.com/watch?v=VfYBKDyF-Dk")

highlander = media.Movie("Highlander",
                         "There can Only be One.",
                         "https://www.movieposter.com/posters/archive/main/95/MPW-47882",
                         "https://www.youtube.com/watch?v=omOZyLmNMJs")

josh_and_sam = media.Movie("Josh and S.A.M.",
                           "Runaway Road Trip",
                           "https://www.movieposter.com/posters/archive/main/178/MPW-89394",
                           "https://www.youtube.com/watch?v=_Zh5nJZhIIU")

mr_peabody_and_sherman = media.Movie("Mr. Peabody & Sherman",
                                     "A Boy and Genius Dog Adventure Through Time",
                                     "http://ia.media-imdb.com/images/M/MV5BMTkxMzM0NzcwN15BMl5BanBnXkFtZTgwNzk1MjMzMTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                                     "https://www.youtube.com/watch?v=aMl2tTVwsZA")

lola_rennt = media.Movie("Lola Rennt",
                         "Zeit ist Alles",
                         "http://movieposters.2038.net/p/Lola-Rennt_1.jpg",
                         "https://www.youtube.com/watch?v=Mx8XPYbMuXA")

mortal_kombat = media.Movie("Mortal Kombat",
                            "Fight to Save Earth!",
                            "http://images.moviepostershop.com/mortal-kombat-movie-poster-1995-1020243557.jpg",
                            "www.youtube.com/watch?v=6LxGtUWxv0o")

# Compiles movies into a list
movies = [mr_peabody_and_sherman, stardust, highlander, josh_and_sam, lola_rennt, mortal_kombat]

# Opens web-page containing each movie in movies (list)
fresh_tomatoes.open_movies_page(movies)
