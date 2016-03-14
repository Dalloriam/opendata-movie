import json

class MovieShort(object):

  def __init__(self, movie_id, title, year, cover_url):
    self.id = movie_id
    self.title = title
    self.year = year
    self.cover_url = cover_url

  def get_json(self):
    return {"id": self.id, "title": self.title, "year": self.year, "img_url": self.cover_url}
