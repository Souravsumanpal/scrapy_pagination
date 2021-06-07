import requests
import json

headers = {
    'authority': 'api.sofascore.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'accept': '*/*',
    'origin': 'https://www.sofascore.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.sofascore.com/',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"f3ff909470"',
}

response = requests.get('https://api.sofascore.com/api/v1/sport/football/events/live', headers=headers)
data = json.loads(response.text)
# print(data['events'][0])
# print(data['events'][0]['tournament']['name'])
# league = data['events'][0]['tournament']['name']
# hometeam = data['events'][0]['homeTeam']['name']
# awayteam = data['events'][0]['awayTeam']['name']

# homescore = data['events'][0]['homeScore']['name']
# awayscore = data['events'][0]['awayScore']['name']


for game in data['events']:
    league = game['tournament']['name']
    hometeam = game['homeTeam']['name']
    awayteam = game['awayTeam']['name']
    homescore = game['homeScore']['current']
    awayscore = game['awayScore']['current']
    print(league, "|", hometeam, homescore, " - ", awayscore, awayteam)