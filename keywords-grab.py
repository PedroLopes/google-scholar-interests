# This scriptused serpapi to crawl google scholar and return authors' interests
#   input: a list of authors formatted as "Name, Affiliation, anything else"
#   output: same list but appended with the "interest 1, interest 2, ..."

# Known workarounds: this is only retrieving the first author match
#    if you want to compare string names, call difflib on top of name and affil
#    it works exceptionally well if you use that matching function

import re
import difflib
from serpapi import GoogleSearch
import subprocess
import time
import csv

# set the output file
f = open("output.csv", "a")

# set encoding for input file
enc = 'iso-8859-15'

# open the input file (e.g., list of authors from a PC meeting)
with open('ipc.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
    for word in line:
      if len(word) > 4: #skip if name and affilliation is not longer than this
        print(word)
        if len(word.split(",")) > 1: 
          author = word.split(",")[0] 
          affil = word.split(",")[1] 
          print("search:" + author + " from:" + affil)

          #find this person on scholar
          params = {
            "engine": "google_scholar_profiles",
            "mauthors": author,
            "affiliation": affil,
            "api_key": "..."
          }

          search = GoogleSearch(params)
          results = search.get_dict()
          profiles = results["profiles"]
          #print(profiles)

          name_matches = []
          affiliation_matches = []
          urls = []

          for idx, profile in enumerate(profiles):
            if idx >= 1:
              break
            name = profile["name"]
            name_matches.append(name)
            print(name)
            print("================")
            ints = []
            interests = profile.get("interests")
            if interests:
              for interest in profile["interests"]:
                print(interest["title"])
                ints.append(interest["title"])
            ints = ','.join(ints)
            print("================")
            print(ints)
            link = profile["link"]
            urls.append(link)
            affiliations = profile["affiliations"]
            affiliation_matches.append(affiliations)
            print(affiliations)
            cited_by = profile.get("cited_by")
            print("-----------WRITTEN DATA------------")
            print(name, end=',')
            print(affiliations, end=',')
            print(ints)
            f.write(name + ',')
            f.write(affiliations + ',')
            f.write(ints + "\n")
f.close()
