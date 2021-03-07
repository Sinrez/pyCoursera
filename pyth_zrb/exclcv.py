import csv
rows = [
["name", "phone", "age", 'height', "weight"], ["mark", "+79514286598", "23", '187', "83"], ["anna", "+79514286598", "20", '165', "57"], ["oleg", "+79514286598", "27", '181', "80"],
]
with open("table.csv", "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerows(rows)