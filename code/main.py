import os
import requests
from dotenv import load_dotenv

# Carrega o token do GitHub a partir de uma variável de ambiente para maior proteção
load_dotenv()
ACCESS_TOKEN = os.getenv('GITHUB_TOKEN')
if not ACCESS_TOKEN:
    raise ValueError("Token do GitHub não encontrado")

# Configurações da API
API_URL = 'https://api.github.com/graphql'
REQUEST_HEADERS = {"Authorization" : f"token {ACCESS_TOKEN}"}
QUERY = """
query ($searchQuery: String!, $reposPerPage: Int!, $cursor: String) {
  search(query: $searchQuery, type: REPOSITORY, first: $reposPerPage, after: $cursor) {
    repositoryCount
    edges {
      node {
        ... on Repository {
          nameWithOwner
          createdAt       
          pullRequests(states: MERGED) { 
            totalCount
          }
          releases {        
            totalCount
          }
          pushedAt        
          primaryLanguage { 
            name
          }  
          issues {          
            totalCount
          }
          closedIssues: issues(states: CLOSED) {
            totalCount
          }
        }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
"""

# Função para obter uma página de repositórios 
# Esta função atua como a camada de comunicação com a API. 
# Monta o payload da requisição com as variáveis necessárias e trata a resposta. 
# Retorna os dados em formato JSON ou lança uma exceção em caso de falha.
#   :param str query: A string de busca para a API.
#   :param int repos_per_page: O número de repositórios a serem buscados nesta página.
#   :param str or None cursor: O cursor da página anterior para continuar a paginação.
def getRepositories(query, repos_per_page, cursor):
    
    variables = {
        "searchQuery": query,
        "reposPerPage": repos_per_page,
        "cursor": cursor
    }
    payload = {"query": QUERY, "variables": variables}
    
    response = requests.post(url=API_URL, headers=REQUEST_HEADERS, json=payload)
    
    if response.status_code == 200:
        json_response = response.json()
        if "errors" in json_response:
            raise Exception(f"Erro na resposta da API: {json_response['errors']}")
        return json_response
    else:
        raise Exception(f"Falha na requisição: Status {response.status_code}\n{response.text}")
    
    
