from PyPDF2 import PdfFileWriter as w 
from pathlib import Path
import PyPDF2

#create 
pdf = w()
file = open(Path.home() / Path('OneDrive','pdf_tx2.pdf'),'wb')
for i in range(5):
    pdf.addBlankPage(219,297) #a4 size dimensions
pdf.write(file)

#copy 
pdfFile = open(Path.home() / Path('سطح المكتب','3DP project.pdf'), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdf.addPage(pageObj)

pdf.write(file)

file.close()