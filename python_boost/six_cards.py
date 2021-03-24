import requests
import json

card = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
dict_resp = json.loads(card.text)
deck_id = dict_resp['deck_id']
url = 'https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count=6'

six_cards = requests.get(url)
six_cards_json = six_cards.json()

for c in six_cards_json['cards']:
    suit = c['value']
    print(f'Вот карта номинала {suit}')
    print(c['images']['png'])

