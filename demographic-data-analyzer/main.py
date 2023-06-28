from demographic_data_analyzer import calculate_demographic_data

# Run the calculate_demographic_data function and print the results
demographic_data = calculate_demographic_data()
print("Number of people of each race:")
print(demographic_data['race_counts'])
print("\nAverage age of men:", demographic_data['average_age_men'])
print("\nPercentage of people with a Bachelor's degree:", demographic_data['percentage_bachelors'])
print("\nPercentage of people with advanced education earning more than 50K:", demographic_data['higher_education_rich'])
print("\nPercentage of people without advanced education earning more than 50K:", demographic_data['lower_education_rich'])
print("\nMinimum number of hours worked per week:", demographic_data['min_work_hours'])
print("\nPercentage of people working the minimum number of hours per week earning more than 50K:", demographic_data['rich_percentage'])
print("\nCountry with the highest percentage of people earning more than 50K:", demographic_data['highest_earning_country'])
print("\nPercentage of people earning more than 50K in the highest earning country:", demographic_data['highest_earning_percentage'])
