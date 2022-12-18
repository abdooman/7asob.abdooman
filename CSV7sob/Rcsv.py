import csv
from pathlib import Path

file = open(r"D:\py\sasa\CSV7sob\employees_1.csv", "r")
reader = csv.reader(file)

data = list(reader)
print(data)
print(data[1][0])
print(data[1][1])
print(data[1][2])