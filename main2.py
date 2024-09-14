import pandas as pd

df = pd.read_csv("adult.data.csv")

print(df[['race']].value_counts().to_list()) #nº de razas  df[df['sex'] == 'Male'].mean()[0].round(1)

male_adults = df[df['sex'] == 'Male'].mean(numeric_only = True)[0].round(1) #edad media de hombres

percentage_bachelors = (df['education'].value_counts('Bachelors') * 100).round(1)

print(percentage_bachelors)
