import csv
from pathlib import Path

#  اضافة متعددة
#header = ['Name', 'Salary', 'Date']
#data = [
#    ['Aml', 1500, '05/02/2019'],
#    ['Yzen', 500, '02/11/2020']
#]
#file = open(r"D:\py\sasa\CSV7sob\employees_1.csv", "a")
#writer = csv.writer(file)
#writer.writerow(header)
#writer.writerows(data)
#file.close

#delimiter  لوضع مسافة بين الكلمات 
#lineterminator لترك خط بين الجمل

file = open(r"D:\py\sasa\CSV7sob\employees_1.csv", 'w', newline='')
writer = csv.writer(file, delimiter='\t', lineterminator='\n-----------------------\n')
writer.writerow(['Sara', 800, '06/04/2021'])
writer.writerow(['Anas', 1200, '15/04/2019'])
writer.writerow(['Aml', 1500, '05/02/2019'])
file.close()