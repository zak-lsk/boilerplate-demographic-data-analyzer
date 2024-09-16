import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df[['race']].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male'].mean(numeric_only = True)[0].round(1)

    # What is the percentage of people who have a Bachelor's degree?
    total_count = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors_count / total_count)*  100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher = df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    higher_education_count = (df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')])
    higher_education_rich = round((higher_education_count.shape[0] / higher.shape[0]) * 100, 1)
    
    lower = df[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))]
    lower_education_count = (df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate') & (df['salary'] == '>50K')])
    lower_education_rich = round((lower_education_count.shape[0] / lower.shape[0]) * 100, 1)

    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week'] == df['hours-per-week'].min())]
    richest_persons_min_hours = df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')]
    rich_percentage = richest_persons_min_hours.shape[0] / num_min_workers.shape[0] * 100


    # What country has the highest percentage of people that earn >50K?
    hightest_earning_countries = df[df['salary'] == '>50K'].groupby('native-country')
    all_countries = df.groupby('native-country')
    high_percentage_country = round(hightest_earning_countries['salary'].count() / all_countries['salary'].count() * 100, 1).sort_values(ascending=False)
    high_percentage_country.reset_index()

    highest_earning_country = high_percentage_country.index[0]
    highest_earning_country_percentage = high_percentage_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    richest_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    indian_occupations = richest_indians.value_counts('occupation').sort_values(ascending = False)
    top_IN_occupation = indian_occupations.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
