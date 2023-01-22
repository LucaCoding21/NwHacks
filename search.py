import requests


def searchAPI(term):
    query = '''
  query ($id: Int, $page: Int, $perPage: Int, $search: String) {
      Page (page: $page, perPage: $perPage) {
          
          media (id: $id, search: $search) {
              
              title {
                  english
              }
              averageScore
              genres
              
          }
      }
  }
  '''
    variables = {
        'search': term,
        'page': 1,
        'perPage': 3
    }
    url = 'https://graphql.anilist.co'

    response = requests.post(
        url, json={'query': query, 'variables': variables})
    print(response.json())
    return response.json()
