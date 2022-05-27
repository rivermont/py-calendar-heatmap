#!/usr/bin/env python3
from csv import DictReader
from time import strftime
import requests
import xml.etree.ElementTree as ET
from lxml import html

# maybe need separate function to add date to dict and return dict

def ingest_ebird(filename="./data/MyEBirdData.csv"):
    """Process the data export from eBird and output json to be used
    in the calender. The data comes as csv, with each line being an individual
    bird observation."""
    ids = set()
    dates = {}
    
    with open(filename, "r") as f:
        reader = DictReader(f)
        for row in reader:
            id_ = row["Submission ID"]
            if id_ not in ids:
                ids.add(id_)
                try:
                    dates[row["Date"]]["count"] += 1
                except KeyError:
                    dates[row["Date"]] = {"count": 1}
    
    return dates


def ingest_github(username):
    dates = {}
    url = f"https://github.com/{username}"
    
    response = requests.get(url).content
    root = html.fromstring(response)
    
    for i in root.iter("rect"):
        try:
            dates[i.attrib["data-date"]] = {"count": int(i.attrib["data-count"])}
        except KeyError: pass
    
    return dates


def ingest_inat(filename="./data/inat.csv"):
    """https://www.inaturalist.org/observations/export
    only need observed_on column"""
    dates = {}
    
    with open(filename, "r") as f:
        for row in f.readlines():
            try:
                dates[row.strip()]["count"] += 1
            except KeyError:
                dates[row.strip()] = {"count": 1}
    
    return dates


def ingest_wiki(filename):
    with open(filename, "r") as f:
        pass
    
    return None


def ingest_osm(username):
    t1 = strftime("%Y-%m-%dT%H:%M:%S%z")
    dates = {}
    
    while True:
        url = f"https://api.openstreetmap.org/api/0.6/changesets?display_name={username}&time=1900-01-01,{t1}"
        response = requests.get(url).content
        root = ET.fromstring(response)
        
        for i in root:
            x = i.attrib["created_at"]
            try:
                dates[x[:10]]["count"] += 1
            except KeyError:
                dates[x[:10]] = {"count": 1}
        
        if len(dates) > 366: break  # stop requesting data after at least a year ago
        if t1 == root[-1].attrib["created_at"]: break  # if it's the last page
        t1 = root[-1].attrib["created_at"]  # get time of oldest changeset in batch
    
    return dates


def ingest_obs(filename):
    """Process csv data export from observation.org"""
    dates = {}
    
    with open(filename, "r") as f:
        reader = DictReader(f)
        for row in reader:
            try:
                dates[row["date"]]["count"] += 1
            except KeyError:
                dates[row["date"]] = {"count": 1}
    
    return dates


if __name__ == "__main__":
    data = {}
    e = ingest_ebird()
    g = ingest_github("rivermont")
    i = ingest_inat()
    o = ingest_osm("rivermont")
    b = ingest_obs("./data/observations-will-bennett.csv")
    for a in (e, g, i, o, b):
        for x in a:
            try:
                data[x]["count"] += a[x]["count"]
            except KeyError:
                data[x] = {"count": a[x]["count"]}
    
    with open("data.json", "w+") as f:
        f.write('"'.join(str(data).split("'")))

