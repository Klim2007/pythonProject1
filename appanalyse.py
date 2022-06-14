import datetime
import pandas as pd
import numpy as np
from pandas import DataFrame

report_date = datetime.datetime.now()
a = pd.read_csv(r"C:\\Users\User\Desktop\apls2.json")
df: DataFrame = pd.DataFrame(a)
df = df.astype(str)
df.columns = ['application', 'date']
cut =  df['application'].str.split(':').str[1]
df ['name'] = cut

df['Report date'] = report_date

df.to_json('./tmp2.json')
a = pd.read_json('./tmp2.json')
df: DataFrame = pd.DataFrame(a)
df = df.astype(str)

print(df)
# научится менять формат столбцов
# удалять ненужные символы из ячеек (адрес ячейки функция loc)




