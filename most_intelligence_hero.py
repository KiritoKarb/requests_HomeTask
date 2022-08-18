import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
page = requests.get(url=url)
for el in page.json():
    N = el['name']
    if N == 'Hulk' or N == 'Captain America' or N == 'Thanos':
        intelligence = 0
        if el['powerstats']['intelligence'] > intelligence:
            the_most_intelligence = el['name']

print(f'Самый умный: {the_most_intelligence}')
