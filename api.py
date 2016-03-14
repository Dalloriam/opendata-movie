import json
import requests
import omdb
from flask import Flask, request
from movie import MovieShort, MovieLong


app = Flask(__name__)
endpoint_url = "https://data.sfgov.org/resource/yitu-d5am.json"

def movie_from_title(movie_title):
  try:
    om_result = omdb.request(t=movie_title).json()
    img_url = om_result['Poster']
    year = om_result['Year']
    om_id = om_result['imdbID']
    return MovieShort(om_id, movie_title, year, img_url)
  except Exception as e:
    return None


@app.route('/movie/top', methods=['POST', 'GET'])
def handle_top():
  rq_json = request.get_json()

  if rq_json and 'count' in rq_json:
    limit = rq_json['count']
  else:
    limit = 10

  max_limit = limit * 5

  data = requests.get(endpoint_url + "?$limit={0}".format(max_limit))
  return_json = data.json()
  movie_title = return_json
  title_list = list(set([movie['title'] for movie in movie_title]))

  result_list = []

  while len(result_list) < limit:
    for title in title_list[:limit-len(result_list)]:
      result = movie_from_title(title)
      title_list.remove(title)
      if result:
        result_list.append(result)

  return json.dumps([movie.get_json() for movie in result_list])

@app.route('/movie/<movie_id>')
def handle_movie_details(movie_id):
  resp = omdb.request(i=movie_id).json()
  description = resp['Plot']
  title = resp["Title"]
  cover_url = resp["Poster"]
  year = resp["Year"]
  director = resp["Director"]
  data = requests.get(endpoint_url+"?$select=locations&title={0}".format(title)).json()
  print(data)
  return "HELLO"

@app.after_request
def add_headers(response):
  response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
  return response


if __name__ == "__main__":
  app.run(debug=True)
