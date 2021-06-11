import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


df = pd.read_excel('C:\\Users\\valdeir.barbosa\\Documents\\vscode_poll\\hopy\\hopy\\files\\Ponto.xlsx', sheet_name='Janeiro',skiprows = range(0, 11))

print("Column headings:")
print(df.columns)
