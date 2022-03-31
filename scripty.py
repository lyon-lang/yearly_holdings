import os
import glob
import csv
from xlsxwriter.workbook import Workbook

for csvfile in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook('Foreign_Holdings.xlsx')

    worksheet = workbook.add_worksheet()

    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)

    worksheet.write('A1', 'Date')
    worksheet.write('B1', 'Brazil')
    workbook.close()
