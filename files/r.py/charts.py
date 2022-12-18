from turtle import title
import openpyxl
from pathlib import Path

excelfile = openpyxl.load_workbook(Path.home() / Path('OneDrive') / 'example.xlsx')
sheet = excelfile['Sheet1']

#charts

title = openpyxl.chart.Reference(sheet, min_col=1, max_col=1, min_row=1, max_row=6)
data = openpyxl.chart.Reference(sheet, min_col=2, max_col=2, min_row=1, max_row=6)
chart = openpyxl.chart.BarChart()

chart.title = 'My Chart'
chart.add_data(data=data)
chart.set_categories(title)

sheet.add_chart(chart, 'E8')
excelfile.save(filename= (Path.home() / Path('OneDrive') / 'example.xlsx'))