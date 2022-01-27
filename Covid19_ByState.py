import json
import requests
from bs4 import BeautifulSoup

data_src = requests.get("https://api.apify.com/v2/key-value-stores/TyToNta7jGKkpszMZ/records/LATEST?disableRedirect=true")
data_txt = data_src.text
soup = BeautifulSoup(data_txt, 'html.parser')
data = json.loads(data_txt)

def GetCasesPerState(state):
    state = state.upper()
    data_infecteds = data['infectedByRegion']
    dictionary = dict((i['state'], i['count']) for i in data_infecteds)
    return(f"Número de infectados no estado {state}: {dictionary[state]} | Atualizado em: {data['lastUpdatedAtSource']}")

data_infected = data['infectedByRegion']
statesList = []
for dtf in data_infected:
    statesList.append(dtf['state'])
