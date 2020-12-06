import sys

k = sys.argv[1].strip()
car = {
    "mark": "Nissan",
    "model": "Qashqai",
    "year": 2018,
    "price": 1_200_000,
    'volume': 2.0
}
print(car.get(k, 'неизвестно'))
