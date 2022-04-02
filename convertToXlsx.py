import os
import glob
import csv
from numpy import NaN
from xlsxwriter.workbook import Workbook


for csvfile in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook('Foreign_Holdings.xlsx', {'strings_to_numbers':  True})

    format_holdings_title = workbook.add_format({
        'font_size': 16,
        'valign': 'vcenter',
    })

    format_date_holdings = workbook.add_format({
        'font_size': 11,
        'bold': 1,
        'valign': 'vcenter',
    })

    format_background = workbook.add_format({'bg_color': '#44546a'})

    worksheet = workbook.add_worksheet('Foreign Holdings in Brazil')
    worksheet1 = workbook.add_worksheet('Chart (Brazil)')

    # create column chart
    column_chart = workbook.add_chart({'type': 'column'})
    row_numbers = []
    rr = 0
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)

        for r, row in enumerate(reader):
            row_numbers.append(r)

            for c, col in enumerate(row):

                worksheet.write(r + 2, c, col)

    _row = len(row_numbers)+2

    column_chart.add_series({
        "name": "Brazil, USD bn",
        "categories": "='Foreign Holdings in Brazil'!$A$4:$A$%s" % _row,
        "values": "='Foreign Holdings in Brazil'!$B$4:$B$%s" % _row

    })

    worksheet.freeze_panes(3, 1)
    worksheet.write('B1', 'Foreign Holdings in Brazil, USD bn',
                    format_holdings_title)
    
    worksheet.write('A3', 'Date', format_date_holdings)
    worksheet.write('B3', 'Brazil', format_date_holdings)

    worksheet1.conditional_format('A1:Y30', {'type':     'cell',
                                             'criteria': '==',
                                             'value':    NaN,
                                             'format':   format_background})

    worksheet.write_url(
        'M1', "internal:'Chart (Brazil)'!D4", string='Go to chart')

    column_chart.set_legend({'position': 'none'})

    worksheet1.insert_chart('D4', column_chart, {'x_scale': 2, 'y_scale': 1})
    workbook.close()
