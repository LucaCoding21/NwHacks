import requests


def idSearch(animeID):
    query = '''
    query ($id: Int) { # Define which variables will be used in the query (id)
        Media (id: $id, type: ANIME) {
            id
            title {
                romaji
                english
            }
            averageScore
            season
            startDate {
                year
            }
            recommendations{
                nodes{
                    rating
                    mediaRecommendation{
                        id
                        title {
                            english
                        }
                        coverImage{
                            medium
                        }
                        
                    }
                }
            }
        }
    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'id': animeID
    }
    url = 'https://graphql.anilist.co'

    response = requests.post(
        url, json={'query': query, 'variables': variables})
    print(response.json())
    return response.json()


def searchAPI(term):
    query = '''
  query ($id: Int, $page: Int, $perPage: Int, $search: String) {
      Page (page: $page, perPage: $perPage) {
          
          media (id: $id, search: $search) {
              id
              title {
                  english
              }
              averageScore
              genres
              coverImage {
                medium
              }
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
