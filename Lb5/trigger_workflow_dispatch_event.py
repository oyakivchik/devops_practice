import requests

response = requests.post(
    'https://github.com/repos/oyakivchik/devops_practice/actions/workflows/andre-filipe-georgievich-344sk-lb5/dispatches',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
    data={'ref':'andre-filipe-georgievich-344sk'}
)
print(response.json())
# View the new `text-matches` array which provides information
# about your search term within the results
# json_response = response.json()
# print(json_response)
# repository = json_response['items'][0]
# print(f'Text matches: {repository["text_matches"]}')