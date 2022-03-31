import xlrd
import datetime


    #xlrd

book = xlrd.open_workbook(r"Foreign_Holdings.xlsx")
sheet = book.sheet_by_index(0)


year_holdings_list = []
total_yearly_holdings = []
years_dict = dict()

for rowx in range(sheet.nrows):
    if rowx != 0:

        row_values = sheet.row_values(rowx)
        year = row_values[0].split('-')[0]
        holding = float(row_values[1])
        year_holdings_list.append([year, holding])

for data in year_holdings_list:
    # here define what key is
    key = data[0]
    # check if key is already present in dict
    if key not in years_dict:
        years_dict[key] = []
    # append some value
    years_dict[key].append(data[1])


for y in years_dict:
    total_yearly_holdings.append(f"{y} - {sum(years_dict[str(y)])}")

print(total_yearly_holdings)