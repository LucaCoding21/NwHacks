from flask import Flask, render_template, request
import requests
import json
from search import searchAPI
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


def getListOfAnimesBySearchTerm(term):
    response = searchAPI(term)
    return response
    # processing of response later


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        response = getListOfAnimesBySearchTerm(request.form['searchbar'])
        print("============================")
        print(response)
        return render_template("hello.html", result=response)
    if request.method == 'GET':
        return render_template("hello.html")


if __name__ == "__main__":
    app.run()
