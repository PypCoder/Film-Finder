movie = {
28:'Action',
12:'Adventure',
16:"Animation",
35:"Comedy",
80:"Crime",
99:"Documentary",
18:"Drama",
10751:"Family",
14:"Fantasy",
36:"History",
27:"Horror",
10402:"Music",
9648:"Mystery",
10749:"Romance",
878:"Science_Fiction",
10770:"TV_Movie",
53:"Thriller",
10752:"War",
37:"Western",
}


movie2 = {value: key for key, value in movie.items()}


def key_finder(genres):
    results = []
    for genre in genres:
        genre= genre.capitalize()
        if genre in movie2:
            results.append(movie2[genre])
        else:
            results.append("INVALID")
    results = [str(genre) for genre in results]
    return results