import json

class MovieShort(object):

  def __init__(self, movie_id, title, year, cover_url):
    self.id = movie_id
    self.title = title
    self.title = year
    self.cover_url = cover_url

  def get_json(self):
    return {"id": self.id, "title": self.title, "year": self.year, "img_url": self.cover_url}


class MovieLong(object):

  def __init__(self, movie_id, title, year, cover_url, director, description):
    self.id = movie_id
    self.title = title
    self.year = year
    self.cover_url = cover_url
    self.director = director
    self.description = description

  def get_json(self):
    return {"id": self.id, "title": self.title, "year": self.year, "img_url": self.cover_url, "director": self.director, "description": self.description}
