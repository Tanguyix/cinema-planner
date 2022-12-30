import requests
import json

def getGraphQLQuery():
  return """query Results($query: String, $filters: [SKFiltersSet], $page: SKPageInput, $sortBy: String) {
    results(query: $query, filters: $filters) {
      hits(page: $page, sortBy: $sortBy) {
        items {
          ... on ResultHit {
            id
            fields {
              title
              casting
              cover
              creators
              genres
              sc_rating
            }
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
  }
  """

def getGraphQLJSONData(movieTitle, graphQLQuery):
  return {
    "query": graphQLQuery,
    "variables": {
          "filters": [{
        "identifier": "universe",
        "value": "Films"
            }],
            "page": {
                "from": 0,
                "size": 1
            },
            "query": movieTitle
    },
  }

def getInfoFromSensCritique(movieTitle):
  graphQLQuery = getGraphQLQuery()
  graphQLJSONData = getGraphQLJSONData(movieTitle, graphQLQuery) 
  apiUrl = "https://apollo.senscritique.com"

  res = requests.post(apiUrl, json=graphQLJSONData)
  return res.json()["data"]["results"]["hits"]["items"][0]
