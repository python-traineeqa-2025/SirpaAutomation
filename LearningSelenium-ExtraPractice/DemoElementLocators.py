from openpyxl import workbook
from openpyxl.workbook import Workbook

wb = Workbook() #opening the workbook

ws=wb.active #opening sheet

ws['A1']="RCV ACADEMY"

wb.save("demo.xlsx")