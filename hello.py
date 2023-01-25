from flask import Flask, render_template, request
import requests
import json
from search import searchAPI, idSearch

app = Flask(__name__)

# Here we define our query as a multi-line string
query = '''
query ($id: Int) { # Define which variables will be used in the query (id)
  Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    title {
      romaji
      english
      
    }
    averageScore
    season
    
    recommendations{
      nodes{
        
        rating
        mediaRecommendation{
          id
          title {
            english
          }
        }
        
      }
    }
    startDate {
      year
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'id': 98659
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
print(response.json())
response = json.dumps(response.json(), sort_keys=False, indent=2)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        response = searchAPI(request.form['searchbar'])
        return render_template("searchresults.html", result=response)
    if request.method == 'GET':
        search_query = request.args.get('search_query')
        response = searchAPI(search_query)
        return render_template("home.html")


@app.route("/anime/<int:anime_ID>", methods=['GET'])
def anime_page(anime_ID):
    # We have the ID of the anime we just clicked on in anime_ID.
    # We should now take that and pass it to a function called getAnimeByID(anime_ID)
    response = idSearch(anime_ID)
    # This function should return the response of the query we make to the API.
    # We can then take our response, pass it to anime.html, and display it however we like.
    return render_template('anime.html', result=response)


if __name__ == "__main__":
    app.run()
