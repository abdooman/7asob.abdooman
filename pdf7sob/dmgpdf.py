import PyPDF2, os
from pathlib import Path

pdffiles = []
for filename in os.listdir(Path.home() / Path( 'OneDrive','Ar')):
    if filename.endswith('.pdf'):
        pdffiles.append(filename)

pdffiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdffiles:
    pdfFileObj = open(Path.home() / Path('OneDrive','Ar',filename),'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    pdfOutput = open(Path.home() / Path('OneDrive','Ar','article.pdf'), 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()