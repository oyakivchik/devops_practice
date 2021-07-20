import os
import requests

TOKEN = os.environ.get('GITHUB_TOKEN')
OWNER = 'oyakivchik'
REPO = 'devops_practice'
WORKFLOW_ID = 'yevhenij-barabolin-344SK-5.yml'

headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': f'token {TOKEN}',
}

data = {
 'ref': 'yevhenij-barabolin-344SK'
}

url = f'https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}/dispatches'

print(url)
response = requests.post(
    url,
    headers=headers,
    data=data
)
print(response)

response = requests.get(
  f'https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows',
  headers=headers
)

print(response.json())
