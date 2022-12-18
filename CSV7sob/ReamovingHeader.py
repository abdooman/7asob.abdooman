import csv, os
from pathlib import Path 

os.makedirs(Path.home() / Path('OenDrive','Empo'), exist_ok=True)

for csvFilename in os.listdir( Path.home() / Path('OenDrive','Empo')):
    if not csvFilename.endswith('.csv'):
        continue

    print('سوف يتم ازالة الترويسة' + csvFilename + '....')
    csvRows = []
    csvF = open(Path.home() / Path('OenDrive','Empo', csvFilename))
    readerObj = csv.reader(csvF)

    for row in readerObj:
        if readerObj.line_num == 1:
            continue #تخطى السطر الأول 
        csvRows.append(row)
    csvF.close()

    csvF = open(Path.home() / Path('OenDrive','Empo', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvF)
    for row in csvRows:
        csvWriter.writerow(row)
    csvF.close()