#!/usr/bin/which python3
# 1.make-pivot-table.py
# read the supermarket sales spreadsheet
# select 3 columns by Gender, Product, Total Sales
# create a pivot table using Gender for y-axis showing Product and Total Sales
# output to excel

import pandas as pd
import os
import sys
PROG = os.path.basename(sys.argv[0])
IN_FILE = os.path.expanduser('supermarket_sales.xlsx')
OUT_FILE = os.path.expanduser('pivot_table.xlsx')
# Read Excel File
df = pd.read_excel(IN_FILE)
print('{}--> {}'.format(PROG, IN_FILE))  # , end='', flush=True)

# Select columns: 'Gender', 'Product line', 'Total'
df = df[['Gender', 'Product line', 'Total']]
print('selecting columns')
print(df)

# Make pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product line',
                             values='Total', aggfunc='sum').round(0)

# Export table to Excel file w/ sheet='Report' starting at row 4
pivot_table.to_excel(OUT_FILE, 'Report', startrow=4)
print(pivot_table)
print(' -->{}'.format(OUT_FILE))
