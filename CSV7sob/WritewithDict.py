import csv
from pathlib import Path 

file = open(Path.home() / Path('OneDrive', 'employees_1.csv'), 'a', newline='')
DictWriter = csv.DictWriter(file, ['Name', 'Salary', 'Date'], delimiter=';')
DictWriter.writerow({'Name': 'Mjed', 'Salary': '1800', 'Date': '08/02/2020'})
file.close