#!/usr/bin/env python3
import json
from colour import Color as color
from datetime import datetime, timedelta
from numpy import linspace

# sample data
with open("./data2.json", "r") as f:
    data = f.read()

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
        try:
            days[d]['contribs'] += int(data[d][x])
        except KeyError: pass  # date not in the last year

del data

# get range of contrib values
contribs = set([days[x]['contribs'] for x in days])
contribs = sorted(contribs)
l = 1
h = contribs[-1]

# number of color classes, diminishing returns around 25, unless there's a better color range function
classes = 25

# contrib value range
range_ = linspace(l, h, classes)

# color range
top = color("#c6e48b")
colors = list(top.range_to("#1b6228", classes))

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

