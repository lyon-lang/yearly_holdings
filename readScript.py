import xlrd

book = xlrd.open_workbook(r"Foreign_Holdings.xlsx")
sheet = book.sheet_by_index(0)

result = dict()

for index in range(1, sheet.nrows):
    row_values = sheet.row_values(index)
    year = row_values[0].split('-')[0]
    holding = float(row_values[1])

    if year not in result:
        result[year] = 0
    result[year] += holding

print(result)
