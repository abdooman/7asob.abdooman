import csv 
from pathlib import Path

file = open(Path.home() / Path('OneDrive', 'employees_1.csv'))
dictreader = csv.DictReader(file)

for row in dictreader:
    print(row['Name'], row['Salary'], row['Date'])