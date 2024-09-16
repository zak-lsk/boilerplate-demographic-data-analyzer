import pandas as pd

df = pd.read_csv("adult.data.csv")

df[['race']].value_counts().to_list() #nº de razas  df[df['sex'] == 'Male'].mean()[0].round(1)

male_adults = df[df['sex'] == 'Male'].mean(numeric_only = True)[0].round(1) #edad media de hombres

total_count = len(df)

bachelors_count = len(df[df['education'] == 'Bachelors'])
percentage_bachelors = round((bachelors_count / total_count)*  100, 1)

higher_education_count = len(df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')])
higher_education = round((higher_education_count / total_count) * 100, 1)
#print('Higher education making more than 50k ' + str(higher_education))

lower_education_count = len(df[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')])
lower_education = round((lower_education_count / total_count) * 100, 1)
#print('Lower education making more than 50k ' + str(lower_education))


#min hour_per_week 

(df['hours-per-week'].min())

# % persons has min hours-per-week >50k

num_min_workers = df[(df['hours-per-week'] == 1)].shape[0]
rich_percentage = ((num_min_workers.shape[0] / df.shape[0]) * 100)

print(rich_percentage)