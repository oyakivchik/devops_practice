import os
import requests

TOKEN = os.environ.get('GITHUB_TOKEN')
OWNER = 'oyakivchik'
REPO = 'devops_practice'
WORKFLOW_ID = 'yuriy-popyuk-341-lab5.yml'
# WORKFLOW_ID = '11426921'

headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': f'token {TOKEN}',
}

data = {
 'ref': 'yuriy-popyuk-341'
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
