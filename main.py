#!/usr/bin/env python3
import json
from colour import Color as color
from datetime import datetime, timedelta
from numpy import linspace

# random data
data = """{
  "2022-01-01": {"git": "2", "osm": "23", "ebird": "1", "mw": "1"},
  "2022-01-02": {"git": "0", "osm": "10", "ebird": "2", "inat": "1", "obs": "0"}
}
"""

t = datetime.now()  # date of today
w = int(t.strftime("%w"))  # weekday of today

days = {}

x = 624
y = w*10
if w: y += (w)*2

for i in range(0, 365):
    s = t - timedelta(days=i)  # date of loop
    d = s.strftime("%Y-%m-%d")  # str date of loop
    
    days[d] = {'date': d, 'contribs': 0, 'color': '#ffaaaa', 'y': y, 'x': x}
    
    if y:
        if y == 10: y -= 10
        else: y -= 12
    else:
        y = 72
        x -= 12

del x, y, t, s

data = json.loads(data)

for d in data:
    for x in data[d]:
        days[d]['contribs'] += int(data[d][x])

# get range of contrib values
contribs = set([days[x]['contribs'] for x in days])
contribs = sorted(contribs)
l = 1
h = contribs[-1]

classes = 5  # number of color classes

# contrib value range
range_ = linspace(l, h, classes)

# color range
top = color("#1b6228")
colors = list(top.range_to("#c6e48b", classes))

ranges = {}
for i in range(classes):
    ranges[range_[i]] = colors[i]


# calculate color value for the day and add to dict
for i in days:
    for x in ranges:
        if x <= days[i]['contribs']:
            days[i]['color'] = ranges[x]


# generate svg code
with open("./calendar.svg", "w+") as f:
    f.write("""<svg xmlns="http://www.w3.org/2000/svg" width="634" height="82">\n""")
    
    for c in days:
        o = f"""<rect name="{days[c]['date']}" alt="{days[c]['contribs']}" fill="{"%s" % days[c]['color']}" width="10" height="10" y="{days[c]['y']}" x="{days[c]['x']}" />"""
        f.write(o + "\n")
    
    f.write("""</svg>""")

