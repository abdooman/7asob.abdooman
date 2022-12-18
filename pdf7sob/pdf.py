import PyPDF2
from pathlib import Path


OpenPdf = open(Path.home() / Path('OneDrive','pdf_test.pdf'), 'rb')
pdfeader = PyPDF2.PdfFileReader(OpenPdf)

#pages number 
print(pdfeader.numPages)

#read
pageObj = pdfeader.getPage(1)
print(pageObj.extractText())

OpenPdf.close()