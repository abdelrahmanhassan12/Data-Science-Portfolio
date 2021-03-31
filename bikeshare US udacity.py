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
    check = True 
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ("enter the name of the city to analyze chicago,new york city or washington : ").lower()
    while True :
        if city  in (CITY_DATA.keys()):
            check = False
            break 
        else:
            print ("City not exist enter again  \n")
            city = input ("enter the name of the city to analyze chicago,new york city or washington : ").lower()
    ##############################################################
    filter_menu = ['days','months']
    filteration = input ("you want to filter by days or months ").lower()
    while True :
        if filteration in (filter_menu):
            check = False
            break 
        else:
            print ("invalid choice ")
            filteration = input ("you want to filter by days or months  :  ").lower()
    ##############################################################    
    # TO DO: get user input for month (all, january, february, ... , june)
    check2 = True 
    months = ['january','february','april','may','june','all']
    month = input("choose month january,february,april,may,june or all months  :  ").lower()
    while True :
        if month  in (months):
            check2 = False
            break 
        else:
            print ("you entered invalid month ")
            month = input("choose month january,february,april,may,june or all months : ").lower()
     ##################################################################################       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    check3 = True 
    days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    day = input ("enter day saturday,sunday,monday,tuesday,wednesday,thursday,friday or all  : ").lower()
    while True :
        if day  in (days):
            check3 = False
            break 
        else:
            print ("you entered invalid day ")
            day = input ("enter day saturday,sunday,monday,tuesday,wednesday,thursday, friday or all  :  ").lower()
    #####################################################################################
    print('-'*40)
    return city, month, day
    ####################################################################################

def load_data(city, month, day):
    #Read Data 
    df = pd.read_csv (CITY_DATA[city])
    #convert the column Start Time from object to datatime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #seprate day and month from the StartTime column 
    df['month'] = df['Start Time'].dt.month 
    df['dayofweek'] = df['Start Time'].dt.day_name()
    df['hour'] = df ['Start Time'].dt.hour
    if month != 'all' :
        months=['january','february','april','may','june']
        month = months.index(month)+1
        df=df[df['month']==month]
        
    if day != 'all' :
        
        df=df[df['dayofweek']==day.title()]
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #most frequent means to calculate the mode
    months=['january','february','april','may','june']
    month = df['month'].mode()[0]
    print ('most common month' , month)


    # TO DO: display the most common day of week
    
    day = df['dayofweek'].mode()[0]
    print ('most common day' , day)

    # TO DO: display the most common start hour
    hours = df['hour'].mode()[0]
    print ('most common hours' , hours)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostcommonstartstation = (df['Start Station'] + df['Start Station']).mode()[0]
    print ('most common start station is  ' , mostcommonstartstation)
    # TO DO: display most commonly used end station
    mostcommonendstation = (df['End Station'] + df['End Station']).mode()[0]
    print ('most common end station is  ' , mostcommonendstation)
    # TO DO: display most frequent combination of start station and end station trip
    # select by both end station and start station 
    mostcommontrip =('from  '+ df['Start Station'] + '  to  ' + df['End Station']).mode()[0]
    print ('most common trip is ' , mostcommontrip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltraveltime = df['Trip Duration'].sum()
        
    # TO DO: display mean travel time
    meantraveltime = df['Trip Duration'].mean()
    
    print ('total travel time : ' , totaltraveltime )
    print ('mean travel time : ' , meantraveltime )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('User Type Stats ' , df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print ('gender stats  : ' , df['Gender'].value_counts())
        print ('most common year : ' , df['Birth Year'].mode()[0])
        print ('most recent year : ' , df['Birth Year'].max())
        print ('most earliest year : ' , df['Birth Year'].min())

    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
