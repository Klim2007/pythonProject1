import matplotlib as plt

import pandas as pd
pd.set_option('display.max_columns', None)
#df = pd.read_csv('http://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')
#df.to_json("C:\\Users\\User\\tit.json")
#df.to_json('./tmp.json')
df = pd.read_json('./tmp.json')
#df.info()
#df.shape
#df.head(3)
#df['Name'] # выбрать только столбец
#print(df[['Name','Age']].head(3)) # выбрать первые 3 строчки в столбцах Name Age, можно поменять местами столбцы
#print(df['Name'])
#print(df.loc[[5,10,15],['Name','Age']]) # лок когда нужно взять определенные строки
#print(df.iloc[[5,10,15],[0,1]]) # iloc выбирает не по названию колонки, а по индексу (порядковые номера столбцов)
#print(df.columns) # показывает наименования столбцов
#print([df['Age']>18]) # фильтр по булевой маске (лож истина) это объект типа SEries, можно отфильтровать для поиска или подсчета нужных значения
#print (df[df['Age'].isin([15])]) # фильтр по значению (точному) в колонке ищет значение
#age = range(1,100)
#df[(df['Name'] == 'Emanuel') & (df['Age'].isin([15]))]) # | - это булевое значение или можно использовать амперсант &, сравнивает только одинаковые по формату значения
#print(df['Age'].notna()) - булевая маска (чек на не пустые значения)
# когда df[df - это фильтр для всего дата фрейма
# insert(loc,column, value, allow_duplicates) номер столбца справа после которого нужно добавить столбец, название, данные, можно ли создать столбец с одинаковм названием
#print(df[df['Age'].notna()])  - можно добавить в фильтр
#print(df['Age'].isna().sum())
#print(df.loc[df['Age'].notna(),'Name']) все у кого не пустой возраст вывел имена
#print(df.sort_values(['Age','Name'],ascending =[True,False]).head(10)) # сортировка / true  false для указания порядка (возрастание, убывание)
df2 = df.copy(deep=True) # deep копирует все элементы внутри
cdf1 = pd.concat([df,df2]) # конкатинация дата фреймов (объединение в один) добавляеются вниз а по столбцам добавить axis = 1 после ] см.ниже
#print(cdf1.shape)
#print(cdf1.info)
mdf = pd.DataFrame(index=df.index) # можно создать пустой дата фрейм размером как существующий , для этого нужно использовать индекс
mdf['PassengerId'] = df['PassengerId']
mdf['evenId'] = mdf['PassengerId'].apply(lambda x: x % 2 == 0)# создаем колонку с булевой маской где булинг выбирает из столбца значения и приминяет к ним условие лямды (% это остаток от деления = 0, а значит число четное)
#print(pd.merge(df, mdf, how='inner')) # merge работает как join в sql т.к. создавали с одним и тем же индексом все совпадает
#статистические операторы функции
#print(df.count()) # считает количество не нулевых значений
#print(df['Age'].count())
# среднее  df['Age'].mean() / df['Age'].median() медиана
#print(df['Age'].describe()) # вернет несколько статистик например сред. количество максимальное минимальное разбивка по долям
#print(df.groupby('Sex')['Age'].mean()) #SEX колонка по которой нужно сгруппировать значения в круг.скобках.
#print(df.groupby('Sex')['Age'].describe())
#print(df.groupby(['Sex','Survived'])['Age'].agg(['mean','median'])) # агрегирование
#print(df['Sex'].value_counts()) # это тоже саме что сгруппировать и посчитать (это шорткат для группировки)
# корреляция (попарно между всеми ) какие данные зависам друг от друга df.corr()
# НАРИСОВАТЬ ГИСТОГРАММУ hist
#print(df['Age'].plot(kind = 'hist'))
#print(df['Age'].plot(kind='kde',xlim=[0,100],legend=True))
tmp_df = df.copy(deep=True)
tmp_df['Pclass'] = 1
#print(df['Pclass'].value_counts()) # общее количество значений в колонке
#print(tmp_df['Pclass'].value_counts())
tmp_df['isAdult'] = tmp_df['Age'] >= 18 # создаем новый столбец используя логическое вырожение младше 18 (да нет булевая маска)

print(tmp_df.head(10)) # можно вывести первые 10 значений
tmp_df['isAduledSurvived'] = tmp_df['isAdult']
tmp_df.loc[tmp_df['isAduledSurvived'] == 0, 'isAduledSurvived'] = False
tmp_df.rename(columns={'isAdultSurvived':'AdultSurv'}).head(1)
print(tmp_df)

