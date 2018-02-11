import requests 

data = {
    "title": "The Godfather",
    "director": "Francis Ford Coppola",
    "year": 1971
}

requests.post("http://localhost:9200/movies/movie/2",data=data)


