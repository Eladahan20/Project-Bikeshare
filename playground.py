import pandas as pd
import numpy as np
import time
#
# # while True:
# #     try:
# #         city = str(input('Enter City Name - Chicago, NY or Washington \n')).lower()
# #         if (city != 'chiago' | 'new-york' | 'washington'):
# #                 print('Please only enter one of those cities')
# #         else:
# #             print('thanks')
# #     except Exception as e:
# #         print('Please only enter one of those cities')
# CITY_DATA = { 'chicago': 'chicago.csv',
#               'new york city': 'new_york_city.csv',
#               'washington': 'washington.csv' }
#
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#
# # def get_filters():
# #     """
# #     Asks user to specify a city, month, and day to analyze.
# #
# #     Returns:
# #         (str) city - name of the city to analyze
# #         (str) month - name of the month to filter by, or "all" to apply no month filter
# #         (str) day - name of the day of week to filter by, or "all" to apply no day filter
# #     """
# #     print('Hello! Let\'s explore some US bikeshare data!')
# #     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
# #     MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
# #     DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
# #
# #     while True:
# #         try:
# #             city = str(input('Enter City Name - Chicago, NY or Washington \n')).lower()
# #             if city in CITY_DATA.keys():
# #                 print('Thank you, you have choosen {}'.format(city))
# #                 break
# #             else:
# #                 print('Wrong input')
# #         except:
# #             print('Wrong Input')
# #
# #     # TO DO: get user input for month (all, january, february, ... , june)
# #     while True:
# #         try:
# #                 month = str(input('Enter desired month - all, january, february, ... , june\n')).lower()
# #                 if month in MONTHS:
# #                     print('Thank you, you have choosen {}'.format(month))
# #                     month = MONTHS.index(month)
# #                     break
# #                 else:
# #                     print('Wrong input')
# #         except:
# #                 print('Wrong Input')
# #
# #     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
# #     while True:
# #         try:
# #             day = str(input('Enter desired day - all, monday, tuesday, ... , sunday\n')).lower()
# #             if day in DAYS:
# #                     print('Thank you, you have choosen {}'.format(day))
# #                     day = DAYS.index(day)-1
# #                     break
# #         except:
# #                 print('Wrong Input')
# #
# #     print('-'*40)
# #     print(city, month, day)
# #
# # get_filters()
# #
# # -----------------------------------------------------------
#
# df = pd.read_csv(CITY_DATA['chicago'])
# df['Start Time'] = pd.to_datetime(df['Start Time'])
# df['Month'] = df['Start Time'].dt.month_name()
# df['Day'] = df['Start Time'].dt.day_name()
# df['Start Hour'] = df['Start Time'].dt.hour
# #
# # print(df.head(10))
#
# # -----------------------------------------------------------
#
# print('\nCalculating The Most Frequent Times of Travel...\n')
# start_time = time.time()
#
# # TO DO: display the most common month
# mc_month = df['Month'].mode()[0]
#
# # TO DO: display the most common day of week
# mc_day = df['Day'].mode()[0]
#
# # TO DO: display the most common start hour
# mc_hour = df['Start Hour'].mode()[0]
#
# print("The most common month is {}, Most common day is {} and the most common hour is {}:00".format(mc_month,mc_day,mc_hour))
# print("\nThis took %s seconds." % (time.time() - start_time))
# print('-'*40)

month = str(input('Enter desired month - all, january, february, ... , june\n')).lower()
if (month in MONTHS or month == 'all'):
    print('Thank you, you have choosen {}'.format(month))
    print(month.capitalize())
else:
    print("wrong input")
