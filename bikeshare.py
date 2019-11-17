import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# Lists for menu selections
city_list = ['Chicago', 'New York City', 'Washington']
month_list = ['all','January', 'February', 'March', 'April', 'May', 'June']
day_list = ['all','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington).
    #HINT: Use a while loop to handle invalid inputs
    city_select = 10
    while city_select > 4:
        print('Select which city to load data for:')
        print('     1. {}'.format(city_list[0]))
        print('     2. {}'.format(city_list[1]))
        print('     3. {}'.format(city_list[2]))
        try:
            city_select = int(input('Input a number 1-3:'))
            print('\nThe city you selected is {}'.format(city_list[city_select-1]))
            ok = (input('Is this the data you want to see (Y/N)?'))
            if ok in('N','n'):
                city_select = 10
            else:
                city_select -= 1
        except:
            print('\nPlease enter 1, 2, or 3 to choose a city')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_select = 10
    while month_select > 7:
       print('\nSelect the month you want to see:')
       print('     1. {}               4. {}'.format(month_list[1], month_list[4]))
       print('     2. {}              5. {}'.format(month_list[2], month_list[5]))
       print('     3. {}                 6. {}'.format(month_list[3], month_list[6]))
       try:
           month_select = int(input('Input a number 1-6 or 0 for all:'))
           if month_select == 0:
               print('\nYou selected all 6 months')
           else:
               print('\nThe month you selected is {}'.format(month_list[month_select]))
           ok = (input('Is this what you want to see (Y/N)?'))
           if ok == 'N' or ok == 'n':
               month_select = 10
       except:
           print('Please enter 0 for all or 1-6 for a particular month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_select = 10
    while day_select > 7:
       print('\nSelect the day you want to see:')
       print('     1. {}               5. {}'.format(day_list[1], day_list[5]))
       print('     2. {}               6. {}'.format(day_list[2], day_list[6]))
       print('     3. {}              7. {}'.format(day_list[3], day_list[7]))
       print('     4. {}            0. All'.format(day_list[4]))
       try:
           day_select = int(input('Input a number 1-7 or 0 for all:'))
           if day_select == 0:
               print('\nYou selected all 7 days')
           else:
               print('\nThe day you selected is {}'.format(day_list[day_select]))
           ok = (input('Is this what you want to see (Y/N)?'))
           if ok == 'N' or ok == 'n':
               day_select = 10
       except:
           print('Please enter 0 for all or 1-6 for a particular month')
    print('-'*40)
    city = city_list[city_select].lower()
    month = month_list[month_select]
    day = day_list[day_select]
    print ('\n' * 50)

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
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        df = df[df['month'] == month_list.index(month)]
        month_message = ' the month of {},'.format(month)
    else:
        month_message = ' all months,'
    if day != 'all':
        df = df[df['day_of_week'] == day]
        day_message = ' only looking at {}s'.format(day.title())
    else:
        day_message = ' and all days of the week'
    city_message = 'For {},'.format(city.title())
    print(city_message + month_message + day_message)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print(' the most frequent times of travel are:')
    start_time = time.time()

    # TO DO: display the most common month
    print('     Month:  {}'.format(month_list[df['month'].mode()[0]]))

    # TO DO: display the most common day of week
    print('     Day:    {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('     Hour:   {}'.format(df['hour'].mode()[0]))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common pick up station is: ')
    print('     {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common drop off station is: ')
    print('     {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station_Pair'] = df['Start Station'] + ' and ' + df['End Station']
    print('The most common pick up / drop off station pairing is: ')
    print('     {}'.format(df['Station_Pair'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    travel_days =  int(travel_time/3600/24)
    travel_hours = int((travel_time - (travel_days*24*3600))/3600)
    travel_min = int((travel_time - (travel_days*24*3600) - (travel_hours*3600))/60)
    print('Total travel time is : {} seconds'.format(travel_time))
    print('     which is {} day(s), {} hour(s), and {} minute(s)'.format(travel_days, travel_hours, travel_min))
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    mean_min = int(mean_time/60)
    mean_sec = int(mean_time - (mean_min * 60))
    print('Mean travel time is: {} seconds'.format(mean_time))
    print('     which is {} minute(s) and {} seconds'.format(mean_min, mean_sec))
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser Types:\n')
    user_cts = df['User Type'].value_counts()
    print(user_cts)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nGender Stats:\n')
        df['Gender'].replace(np.NAN, 'unknown')
        gender_cts = df['Gender'].value_counts()
        print(gender_cts)
    else:
        print('\nNo Gender data available\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nAges:\n')
        oldest = int(df['Birth Year'].min())
        youngest = int(df['Birth Year'].max())
        most_common_yr = int(df['Birth Year'].mode()[0])
        print('The oldest person was born in {}'.format(oldest))
        print('The youngest person was born in {}'.format(youngest))
        print('Most users were born in {}'.format(most_common_yr))
    else:
        print('\nNo Birth Year data available\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        print ('\n' * 100)
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart(Y/N)?\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
