import re
import difflib
from serpapi import GoogleSearch
import subprocess
import time

f = open("output.csv", "a")

enc = 'iso-8859-15'

import csv
from serpapi import GoogleSearch

with open('ipc.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
    for word in line:
      if len(word) > 4:
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
          print(profiles)

          name_matches = []
          affiliation_matches = []
          urls = []

          for idx, profile in enumerate(profiles):
            if idx >= 1:
              break
            name = profile["name"]
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
            name_matches.append(name)
            print(name)
            link = profile["link"]
            urls.append(link)
            affiliations = profile["affiliations"]
            affiliation_matches.append(affiliations)
            print(affiliations)
            cited_by = profile.get("cited_by")
            print("-----------DATA-----------------------")
            print(name, end=',')
            print(affiliations, end=',')
            print(ints)
            f.write(name + ',')
            f.write(affiliations + ',')
            f.write(ints + "\n")
f.close()
