import csv
from typing import ItemsView
people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]

with open('people.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for row in people:
        writer.writerow(row)
with open('people.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
        