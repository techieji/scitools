import toml
import csv

with open('events.ini') as f:
    events = toml.load(f)

with open('people.csv') as f:
    people = list(csv.DictReader(f))

def hash_roster(l):
    for _, v in events.items():
        pass
