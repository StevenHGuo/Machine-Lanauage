import media
import fresh_tomatoes

# Variable store the instance of movie
movie_object_list = []
# Variable store the basic information of movie, include movie name , the url movie poster url and the url movie trailers
movie_info_list = []

the_professional = ["The Professional",
                    "http://www.impawards.com/1994/posters/professional_ver1.jpg",
                    "https://www.youtube.com/watch?v=aNQqoExfQsg"]
movie_info_list.append(the_professional)

the_shawshank_redemption = ["The Shawshank Redemption",
                            "http://www.impawards.com/1994/posters/shawshank_redemption_ver2.jpg",
                            "https://www.youtube.com/watch?v=6hB3S9bIaco"]
movie_info_list.append(the_shawshank_redemption)

years_slave = ["12 Years a Slave",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTEzODkyN15BMl5BanBnXkFtZTcwNTU4NTc4OQ@@._V1_UY1200_CR89,0,630,1200_AL_.jpg",
                "https://www.youtube.com/watch?v=z02Ie8wKKRg"]
movie_info_list.append(years_slave)

wall_e = ["WALL-E",
          "http://www.impawards.com/2008/posters/wall_e.jpg",
          "https://www.youtube.com/watch?v=alIq_wG9FNk"]
movie_info_list.append(wall_e)

kung_fu = ["Kung Fu Hustle",
           "http://www.impawards.com/2005/posters/kung_fu_hustle.jpg",
           "https://www.youtube.com/watch?v=-m3IB7N_PRk"]
movie_info_list.append(kung_fu)

monkey_king = ["Monkey King: Hero Is Back",
                "https://upload.wikimedia.org/wikipedia/en/1/13/Monkey_King_Hero_is_Back_Chinese_film_poster.jpg",
               "https://www.youtube.com/watch?v=v33o9deALkA"]
movie_info_list.append(monkey_king)

pride_prejudice = ["Pride & Prejudice",
                   "http://www.impawards.com/2005/posters/pride_and_prejudice.jpg",
                   "https://www.youtube.com/watch?v=1dYv5u6v55Y"]
movie_info_list.append(pride_prejudice)

# Generate the movie object
for element in movie_info_list:
    movie_object = media.Movie( element[0], element[1], element[2] )
    movie_object_list.append(movie_object)


# Generate the html and open the page
fresh_tomatoes.open_movies_page(movie_object_list)