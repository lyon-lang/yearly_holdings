import pandas as pd

df = pd.read_excel("Foreign_Holdings.xlsx",  usecols='A:B', skiprows=[
                   0, 1], sheet_name='Foreign Holdings in Brazil')

date = df["Date"] = pd.to_datetime(df.Date, format='%Y-%m-%d')
df["Year"] = date.dt.year
dataframe = df[["Date", "Brazil", "Year"]]

yearly_holdings = df.groupby(by=["Year"])["Brazil"].sum()

print(yearly_holdings.to_dict())
