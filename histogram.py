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
     
#word_list = ['A', 'A', 'B', 'B', 'A', 'C', 'C', 'C', 'C']



counts = Counter(word_list)

labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

print(indexes[0])
print(labels[0])
print(values[0])

bar_width = 0.35

indexes = indexes[1:]
labels = labels[1:]
values = values[1:]

plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels, rotation='vertical')
plt.show()
