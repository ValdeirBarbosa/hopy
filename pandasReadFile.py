import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


df = pd.read_excel('C:\\Users\\valde\\Documents\\Python-Workspace\\hope\\hopy\\files\\Espelho de Ponto-2021 (1).xlsx', sheet_name='Janeiro',skiprows = range(0, 11))

print("Column headings:")
print(df.columns)
