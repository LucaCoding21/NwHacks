from flask import Flask, render_template
import requests
import json
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


@app.route("/")
def hello_world():
    return render_template("hello.html", response=response)


if __name__ == "__main__":
    app.run()
