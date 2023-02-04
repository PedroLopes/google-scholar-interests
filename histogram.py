# This script opens a file with words on it (csv formatted)
#   and will plot a histogram of those
#   known workarounds: it takes in empty spaces for now
#                      they should be ignored
# Credit: modified from https://stackoverflow.com/questions/35596128/how-to-generate-a-word-frequency-histogram-where-bars-are-ordered-according-to


from collections import Counter
import csv
import numpy as np
import matplotlib.pyplot as plt

word_list = []

with open('cloud.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
    for word in line:
       word_list.append(word)
     
counts = Counter(word_list)
labels, values = zip(*counts.items())
# sort your values in descending order
indSort = np.argsort(values)[::-1]
# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]
indexes = np.arange(len(labels))

#print(indexes[0])
#print(labels[0])
#print(values[0])

bar_width = 0.5

# skipping the first element of all because it's the "" (empty space) data
indexes = indexes[1:]
labels = labels[1:]
values = values[1:]

# let's plot
plt.bar(indexes, values)
plt.xticks(indexes + bar_width, labels, rotation='vertical')
plt.show()
