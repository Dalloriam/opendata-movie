import json
import requests
import omdb
from flask import Flask, request
from movie import MovieShort


app = Flask(__name__)
endpoint_url = "https://data.sfgov.org/resource/yitu-d5am.json"

def movie_from_title(movie_title):
  om_result = omdb.request(t=movie_title).json()
  img_url = om_result['Poster']
  year = om_result['Year']
  om_id = om_result['imdbID']
  return MovieShort(om_id, movie_title, year, img_url)


@app.route('/movie/top', methods=['POST'])
def handle_top():
  rq_json = request.get_json()

  if 'count' in rq_json:
    limit = rq_json['count']
  else:
    limit = 100

  data = requests.get(endpoint_url + "?$limit={0}".format(limit))
  return_json = data.json()
  movie_title = return_json
  title_list = [movie['title'] for movie in movie_title]

  movie_objects = map(movie_from_title, title_list)

  return json.dumps([movie.get_json() for movie in movie_objects])


if __name__ == "__main__":
  app.run(debug=True)
