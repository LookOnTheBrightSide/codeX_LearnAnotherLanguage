print "hello world"
"""
multi 
line
comment

this uses the csv module

"""

import csv

f = open('nelisaPurchases.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print row