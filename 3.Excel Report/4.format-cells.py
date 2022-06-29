#!/usr/bin/which python3
# 4.format-cells.py
# loads the Excel report.xlsx 'Report' workbook created in 2.add-charts.py
# select the 'Report' sheet
# annotate cells A1 and A2 with titles
# output to excel
from openpyxl import load_workbook
from openpyxl.styles import Font
import os
import sys
PROG = os.path.basename(sys.argv[0])
IN_FILE = os.path.expanduser('report.xlsx')
OUT_FILE = os.path.expanduser('report_january.xlsx')

if not os.path.exists(IN_FILE):
    print("{} -- file '{}' not found".format(PROG, IN_FILE))
    exit(1)

# if the barchart.xlsx file has been modified by IntelliJ's ExcelReader,
# this will throw a 'KeyError' exception
wb = load_workbook(IN_FILE)
sheet = wb['Report']
print("{}--> '{}({})'".format(PROG, IN_FILE, sheet), end='', flush=True)

# Add format
sheet['A1'] = 'Sales Report'
sheet['A2'] = 'January'
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

wb.save(OUT_FILE)
print(" --> '{}'".format(OUT_FILE))
