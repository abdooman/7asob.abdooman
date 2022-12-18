from docx2pdf import convert
from pathlib import Path

docx_file = Path.home() / Path('OneDrive', 'Ar', 'Ac.docx') 
pdf_file = Path.home() / Path('OneDrive',  'PDFod.pdf')
#multi_file = 

convert(docx_file, pdf_file)