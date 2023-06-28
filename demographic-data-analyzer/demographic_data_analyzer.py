import pandas as pd

def calculate_demographic_data():
    # Read the dataset
    df = pd.read_csv('adult.data.csv')

    # Question 1: How many people of each race are represented in this dataset?
    race_counts = df['race'].value_counts()

    # Question 2: What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()

    # Question 3: What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # Question 4: What percentage of people with advanced education make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100

    # Question 5: What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

    # Question 6: What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_earning_country = df.loc[df['salary'] == '>50K', 'native-country'].value_counts(normalize=True).idxmax()
    highest_earning_percentage = (df.loc[df['native-country'] == highest_earning_country, 'salary'] == '>50K').mean() * 100

    # Create a dictionary of the results
    demographic_data = {
        'race_counts': race_counts,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_percentage': round(highest_earning_percentage, 1)
    }

    return demographic_data

# Run the function and print the results
print(calculate_demographic_data())