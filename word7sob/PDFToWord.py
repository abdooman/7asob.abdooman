from pdf2docx import Converter
from pathlib import Path

pdf_file = Path.home() / Path('OneDrive', 'Ar', 'article.pdf')
docx_file = Path.home() / Path('OneDrive', 'Ac.docx')

# تحويل من pdf الى docx
cv = Converter(pdf_file)
#cv.convert(docx_file, start=3, end=7)  تستطيع اختيار البداية والنهاية 
cv.convert(docx_file) # جميع الصفحات 
cv.close()
