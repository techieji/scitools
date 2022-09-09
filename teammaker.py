import toml
import csv
import itertools as it
import operator as op

pg = op.itemgetter('people')
profgetter = op.itemgetter('proficiencies')

with open('events.toml') as f:
    events = toml.load(f)

with open('people.csv') as f:
    people = list(csv.DictReader(f))

def chunk(l, lengths):
    for n in lengths:
        yield l[:n]
        l = l[n:]

def hash_roster(l):
    return hash(tuple(map(frozenset, chunk(map(op.itemgetter('name'), l), map(pg, events.values())))))
    l = []
    for _, v in events.items():
        p = v['people']
        l.append(frozenset({l[:p]}))
        l = l[p:]
    return hash(tuple(l))

def suitability(l):
    s = 0
    for prof, people in zip(map(profgetter, events.values()), chunk(l, map(pg, events.values()))):
        for x in people:
            for profname, v in x.items():
                if profname != 'name':
                    s += prof.get(profname, 0) * float(v)
    return s

seen = set()
best = None
bestval = 0

for r in it.permutations(people):
    #if hash_roster(r) not in seen:
    if True:
        s = suitability(r)
        if s > bestval:
            best = r
            bestval = s

import pprint
pprint.pprint(list(map(op.itemgetter('name'), best)))
print(bestval)