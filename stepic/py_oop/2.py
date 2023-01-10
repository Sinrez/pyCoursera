import csv

from dateutil import parser

with open("Crimes.csv") as f:
    crime_reader = csv.DictReader(f)

    crimes_2015 = {}

    for line in crime_reader:
        if parser.parse(line["Date"]).year == 2015:
            if line["Primary Type"] in crimes_2015:
                crimes_2015[line["Primary Type"]] += 1
            else:
                crimes_2015[line["Primary Type"]] = 1

print(max(crimes_2015, key=crimes_2015.get))