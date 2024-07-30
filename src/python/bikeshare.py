import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please choose one of the provided cities.")

    while True:
        month = input("Which month? January, February, March, April, May, June, or all? ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid input. Please choose a valid month or 'all'.")

    while True:
        day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all? ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid input. Please choose a valid day or 'all'.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    print('======================================================================')
    print('Starting data loading process.')
    print('======================================================================')

    
    city_files = {
        'chicago': 'chicago.csv',
        'new york city': 'new_york_city.csv',
        'washington': 'washington.csv'
    }

    
    if city in city_files:
        df = pd.read_csv(city_files[city])
    else:
        return "Erro: Arquivo da cidade não encontrado."

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name().str.lower()
    df['Day of Week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day of Week'] == day]

    print('======================================================================')
    print('Data loading process completed.')
    print('======================================================================')

    show_raw_data = input("Would you like to see the first 5 rows of raw data? Enter 'yes' or 'no'. ").lower()
    start_index = 0
    while show_raw_data == 'yes':
        print(df.iloc[start_index:start_index + 5])
        start_index += 5
        show_raw_data = input("Would you like to see the next 5 rows of raw data? Enter 'yes' or 'no'. ").lower()

    return df


def time_stats(df):
    print('======================================================================')
    print('Process of statistics on travel times Started.')
    print('======================================================================')
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if 'Start Time' in df.columns:
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        df['Month'] = df['Start Time'].dt.month_name()
        common_month = df['Month'].mode()[0]
        print(f"The most common month for travel is: {common_month}")

        df['Day of Week'] = df['Start Time'].dt.day_name()
        common_day = df['Day of Week'].mode()[0]
        print(f"The most common day of week for travel is: {common_day}")

        df['Hour'] = df['Start Time'].dt.hour
        common_hour = df['Hour'].mode()[0]
        print(f"The most common start hour for travel is: {common_hour}")

    else:
        print("Error: 'Start Time' column not found in the DataFrame.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('======================================================================')    
    print('Statistics process on travel times completed.')
    print('======================================================================')


def station_stats(df):
    print('======================================================================')
    print('Process of statistics on the most popular stations and trips Started.')
    print('======================================================================')
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {common_start_station}")

    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {common_end_station}")

    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print(f"The most frequent combination of start station and end station trip is: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('======================================================================')
    print('Process of statistics on the most popular stations and trips completed.')
    print('======================================================================')

def trip_duration_stats(df):
    print('======================================================================')
    print('Process of statistics on the total and average trip duration Started.')
    print('======================================================================')
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is: {total_travel_time} seconds")

    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('======================================================================')
    print('Process of statistics on the total and average trip duration completed.')
    print('======================================================================')


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('======================================================================')
    print('\nCalculating User Stats...\n')
    print('======================================================================')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    for index, value in user_types.items():
        print(f"{index}: {value}")

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:")
        for index, value in gender_counts.items():
            print(f"{index}: {value}")
    else:
        print("\nGender data is not available for this dataset.")

    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")
    else:
        print("\nBirth year data is not available for this dataset.")

    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
