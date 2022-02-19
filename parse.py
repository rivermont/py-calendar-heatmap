#!/usr/bin/env python3
import csv

# maybe need separate function to add date to dict and return dict

def ingest_ebird(filename="./MyEBirdData.csv"):
    """Process the data export from eBird and output json to be used
    in the calender. The data comes as csv, with each line being an individual
    bird observation."""
    ids = set()
    dates = {}
    
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            id_ = row["Submission ID"]
            if id_ not in ids:
                ids.add(id_)
                try:
                    dates[row["Date"]]["count"] += 1
                except KeyError:
                    dates[row["Date"]] = {"count": 1}

    return dates


def ingest_git(filename):
    with open(filename, 'r') as f:
        pass
    
    return None


def ingest_inat(filename="./inat.csv"):
    """https://www.inaturalist.org/observations/export
    only need observed_on column"""
    dates = {}
    
    with open(filename, 'r') as f:
        for row in f.readlines():
            try:
                dates[row.strip()]["count"] += 1
            except KeyError:
                dates[row.strip()] = {"count": 1}
    
    return dates


def ingest_wiki(filename):
    with open(filename, 'r') as f:
        pass
    
    return None


def ingest_osm(filename):
    with open(filename, 'r') as f:
        pass
    
    return None


def ingest_obs(filename):
    with open(filename, 'r') as f:
        pass
    
    return None


with open("data2.json", "w+") as f:
    data = {}
    e = ingest_ebird()
    i = ingest_inat()
    for a in (e, i):
        for x in a:
            try:
                data[x]["count"] += a[x]["count"]
            except KeyError:
                data[x] = {"count": a[x]["count"]}
    
    f.write('"'.join(str(data).split("'")))

