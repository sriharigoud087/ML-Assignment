import pandas as pd

# Task 1: Read the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/ManidharKondeti/Assignmnt3ML/main/data.csv')

print("CSV file read successfully:\n", df.head())

# Question 2
# Showing basic statistical description of the data using the describe() function
print("\nBasic statistical description of the data:\n", df.describe())

# Question 3
# Check if the data has null values.
print('\nAre there any null values present in data: ', df.isnull().values.any())

# Replace the null values with the mean
df.fillna(df.mean(), inplace=True)
print('Are there any null values after using fillna: ', df.isnull().values.any())

# Question 4
# Select at least two columns and aggregate the data using: min, max, count, mean.
aggregat = df.groupby('Duration').agg({'Calories': ['mean', 'min', 'max', 'count']})
print("\nAggregation of Calories by Duration:\n", aggregat)

# Question 5
# Filter the dataframe to select the rows with calories values between 500 and 1000
calories_between_500_and_1000 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
print("\nRows with Calories between 500 and 1000:\n", calories_between_500_and_1000)

# Question 6
# Filter the dataframe to select the rows with calories values > 500 and pulse < 100
calories_above_500_pulse_below_100 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print("\nRows with Calories > 500 and Pulse < 100:\n", calories_above_500_pulse_below_100)

# Question 7
# Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”
df_modified = df.drop(columns=['Maxpulse'])
print("\ndf_modified DataFrame:\n", df_modified.head())

# Question 8
# Delete the “Maxpulse” column from the main df dataframe
df = df.drop('Maxpulse', axis=1)
print("\nMain df DataFrame after dropping 'Maxpulse' column:\n", df.head())

# Question 9
# Convert the datatype of Calories column to int datatype
df['Calories'] = df['Calories'].astype('int64')
print("\nData types after converting 'Calories' to int:\n", df.dtypes)

