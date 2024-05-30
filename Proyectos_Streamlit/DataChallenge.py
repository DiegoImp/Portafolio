import pandas as pd


def analyze_data():
    """
    Analyzes the dataset and answers several questions about the data.

    Returns:
    - A Pandas series with race names as the index labels, representing the count of people of each race in the dataset.
    - The average age of men in the dataset.
    - The percentage of people who have a Bachelor's degree.
    - The percentage of people with advanced education (Bachelors, Masters, or Doctorate) who make more than 50K.
    - The percentage of people without advanced education who make more than 50K.
    - The minimum number of hours a person works per week.
    - The percentage of people who work the minimum number of hours per week and have a salary of more than 50K.
    - The country with the highest percentage of people who earn more than 50K, and the corresponding percentage.
    - The most popular occupation for those who earn more than 50K in India.
    """
    df = pd.read_csv(
        r'D:\Programacion\Python\API_Streamlit\Proyectos_Streamlit\adult.data.csv')

    race_counts = df['race'].value_counts()

    average_age_of_men = df[df['sex'] == 'Male']['age'].mean()

    percentage_bachelors_degree = df[df['education'] == 'Bachelors'].value_counts(
    ).sum() / df['education'].value_counts().sum() * 100

    percentage_bachelors_degree2 = (
        df['education'] == 'Bachelors').mean() * 100

    # Filtramos las filas que tienen una educación avanzada y un salario >50K
    advanced_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])
    high_salary = df['salary'] == '>50K'

    # Calculamos el porcentaje de personas con educación avanzada que tienen un salario >50K
    percentage_advanced_education = df[advanced_education &
                                       high_salary].shape[0] / df[advanced_education].shape[0] * 100

    percentage_no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (
        df['salary'] == '>50K')].value_counts().sum() / df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].value_counts().sum() * 100

    min_hours_per_week = df['hours-per-week'].min()

    percentage_min_hours_salary_gt_50K = df[(df['hours-per-week'] == min_hours_per_week) & (df['salary'] == '>50K')].value_counts(
    ).shape[0] / df[(df['hours-per-week'] == min_hours_per_week)].value_counts().sum() * 100

    country_highest_percentage_gt_50K = (
        df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).idxmax()

    percentage_highest_percentage_gt_50K = (
        df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).max()

    most_popular_occupation_india = df[(df['native-country'] == 'India') & (
        df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return race_counts, average_age_of_men, percentage_bachelors_degree, percentage_bachelors_degree2, percentage_advanced_education, percentage_no_advanced_education, min_hours_per_week, percentage_min_hours_salary_gt_50K, country_highest_percentage_gt_50K, percentage_highest_percentage_gt_50K, most_popular_occupation_india


# Call the function to analyze the data
race_counts, average_age_of_men, percentage_bachelors_degree, percentage_bachelors_degree2, percentage_advanced_education, percentage_no_advanced_education, min_hours_per_week, percentage_min_hours_salary_gt_50K, country_highest_percentage_gt_50K, percentage_highest_percentage_gt_50K, most_popular_occupation_india = analyze_data()

# Print and explain each result
print("Count of people of each race:")
print(race_counts)
print("\nAverage age of men:")
print(average_age_of_men)
print("\nPercentage of people with a Bachelor's degree:")
print(percentage_bachelors_degree, percentage_bachelors_degree2)
print("\nPercentage of people with advanced education who make more than 50K:")
print(percentage_advanced_education)
print("\nPercentage of people without advanced education who make more than 50K:")
print(percentage_no_advanced_education)
print("\nMinimum number of hours a person works per week:")
print(min_hours_per_week)
print("\nPercentage of people who work the minimum number of hours per week and have a salary of more than 50K:")
print(percentage_min_hours_salary_gt_50K)
print("\nCountry with the highest percentage of people who earn more than 50K:")
print(country_highest_percentage_gt_50K)
print("\nPercentage of people in the country with the highest percentage of people who earn more than 50K:")
print(percentage_highest_percentage_gt_50K)
print("\nMost popular occupation for those who earn more than 50K in India:")
print(most_popular_occupation_india)
