import requests
import json

# card = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
# dict_resp = json.loads(card.text)
# deck_id = dict_resp['deck_id']
# url_mix = 'https://deckofcardsapi.com/api/deck/' + deck_id + '/ shuffle /'
# card_mix = requests.get(url_mix)
# url = 'https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/?count=1'
# cardf = requests.get(url)
# card_json = cardf.json()
# print(card_json)


def suit_maker():
    "Масть, одна из S Spades (Пик), D Diamonds (Бубен), C Clubs (Треф) или H Hearts (Червей)"
    card = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    dict_resp = json.loads(card.text)
    deck_id = dict_resp['deck_id']
    url_mix = 'https://deckofcardsapi.com/api/deck/' + deck_id + '/ shuffle /'
    card_mix = requests.get(url_mix)
    url = 'https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/?count=1'
    cardf = requests.get(url)
    card_json = cardf.json()
    answer = ''

    if card_json['cards'][0]['suit'] in ('Spades','Clubs'):
        answer = 'Нет'
    else:
        answer = 'Да'
    return answer

for i in range(1,10):
    print(suit_maker())

# card = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
# dict_resp = json.loads(card.text)
# deck_id = dict_resp['deck_id']
# url = 'https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/?count=1'
#
# six_cards = requests.get(url)
# six_cards_json = six_cards.json()
# answer = 'Да'
#
#
#
# print(six_cards_json['cards'][0]['suit'])


