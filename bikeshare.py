import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
        try:
            city = str(input('Which city would you like to explore - Chicago, New York City or Washington? \n')).lower()
            if city in CITY_DATA.keys():
                print('Pulling data for {}'.format(city.capitalize()))
                break
            else:
                print('Wrong Input, try again please')
        except:
            print('Wrong Input')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Should we filter by month? if yes - type month name, if no - type "all"\n')).lower()
            if month in MONTHS:
                print('We will show data for {} only'.format(month.capitalize()))
                break
            elif month == 'all':
                print('We will show data for all months')
                break
            else:
                print('Wrong Input, try again please')
        except:
            print('Wrong Input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Should we filter by day? if yes - type day name, if no - type "all"\n')).lower()
            if day in DAYS :
                print('Thank you, you have choosen {}'.format(day.capitalize()))
                break
            elif day == 'all':
                print('We will show data for all days')
                break
            else:
                print('Wrong Input, try again please')
        except:
            print('Wrong Input')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #Read corresponding data.csv
    df = pd.read_csv(CITY_DATA[city])
    #Convert 'Start Time' column to Datetime() object
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Create columns for month, day and hour
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    # Filtering dataframe by chosen month
    if month != 'all':
        month = month.capitalize()
        df = df.loc[df['Month'] == month]
    #Filtering dataframe by chosen day
    if day != 'all':
        day = day.capitalize()
        df = df.loc[df['Day'] == day]

    return df

def data_chunks(df):
    i = 0
    while True:
        try:
            user_chunks_agreed = input('Would you like to see 5 rows of the raw data?').lower()
            if user_chunks_agreed == 'no':
                print('OK, moving forward')
                break
            elif user_chunks_agreed == 'yes':
                while user_chunks_agreed == 'yes':
                    print(df.iloc[i:i+5])
                    user_chunks_agreed = input('Care to see 5 more rows?')
                    i +=5
            else:
                print('Wrong Input, try again please')
        except:
            print('Wrong Input')


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    print('-'*40)

    start_time = time.time()

    # TO DO: display the most common month, if df is unfiltred by month
    if len(df['Month'].unique())>1:
        mc_month = df['Month'].mode()[0]
        print("Most common month is {}".format(mc_month))

    # TO DO: display the most common month, if df is unfiltred by day
    if len(df['Day'].unique())>1:
        mc_day = df['Day'].mode()[0]
        print("Most common day of week is {}".format(mc_day))

    # TO DO: display the most common start hour
    #Finds most common hour
    mc_hour = df['Start Hour'].mode()[0]
    #Finds it's precentage amongst all start hours
    mc_hour_precentage = df['Start Hour'].value_counts(normalize=True, ascending=False)[mc_hour]

    print("Most common starting hour is {}:00, Which is {:.0%} of all rides".format(mc_hour,mc_hour_precentage))
    print("\n(This took %s seconds)" % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    print('-'*40)
    start_time = time.time()
    # TO DO: display most commonly used start station
    mc_start_station = df['Start Station'].mode()[0]
    # TO DO: display most commonly used end station
    mc_end_station = df['End Station'].mode()[0]
    # TO DO: display most frequent combination of start station and end station trip
    mc_combination = ' <---> '.join(df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).idxmax())


    print("Most popular start station is {}, \nMost popular end station is {} \nMost popular combination is {}".format(mc_start_station,mc_end_station,mc_combination))
    print("\n(This took %s seconds)" % (time.time() - start_time))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    print('-'*40)

    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    total_travel_sum = str(datetime.timedelta(seconds=int(df['Trip Duration'].sum())))
    # TO DO: display mean travel time
    mean_travel = str(datetime.timedelta(seconds=int(df['Trip Duration'].mean())))
    # mean_travel = time.strftime('%H:%M:%S', time.gmtime(df['Trip Duration'].mean()))

    print("Total travel time is {} seconds, which is {} \nAverage travel time is {} hours".format(total_travel,total_travel_sum,mean_travel))
    print("\n(This took %s seconds)" % (time.time() - start_time))


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    print('-'*40)
    start_time = time.time()

    # TO DO: Display counts of user types
    types_count = dict(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    gender_count = dict(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year, recent_year, common_year = int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])

    print("Counts of user types: {}, \nCounts of gender: {} \nEarliest is: {}, most recent is: {}, and most common year of birth is: {}".format(types_count,gender_count,earliest_year,recent_year,common_year))
    print("\n(This took %s seconds)" % (time.time() - start_time))




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        data_chunks(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
