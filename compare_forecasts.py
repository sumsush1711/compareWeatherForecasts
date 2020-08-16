"""This script takes in two city names as input and outputs the differences in
weather between the cities over the next 5 days.

Usage example:

    python compare_forecasts.py Toronto Cleveland

Output example:

    Weather forecast comparison between Toronto and Cleveland:

    Day 1:
    Toronto (18C) will be 3C cooler than Cleveland (21C).
    Toronto will have clear sky, but Cleveland will have rain.

    Day 2:
    Toronto (21C) will be 3C warmer than Cleveland (18C).
    Toronto will have scattered clouds, but Cleveland will have light rain.

    Day 3:
    Toronto and Cleveland will both have the same temperature (20C).
    Toronto and Cleveland will both have light rain.

    Day 4:
    Toronto (18C) will be 3C cooler than Cleveland (21C).
    Toronto and Cleveland will both have light rain.

    Day 5:
    Toronto and Cleveland will both have the same temperature (17C).
    Toronto will have scattered clouds, but Cleveland will have light rain.

Some considerations for this assignment:
    - The version of Python used is Python 3.6.6
    - To enter a city as an input with more than one word, put "" around it. Example, "Sao Paulo"
    - Since the assignment stated that the data for temperature and weather descriptions must come from the OpenWeatherMap's API, there are some
      weather descriptions such as 'sky is clear' (which should ideally say 'clear sky'), but that is the exact data provided from the API
    - Since there are multiple temperatures from the API response data, I have chosen to take the 'maximum temperature' value for each day, and I have
      rounded it up to the nearest integer.
"""
import argparse
import requests
import math

def main():
    parser = argparse.ArgumentParser(description="Compare weather forecasts between two cities.")
    parser.add_argument("city1", type=str, help="The first city. The city should only be one word.")
    parser.add_argument("city2", type=str, help="The second city. The city should only be one word.")
    args = parser.parse_args()

    #Exception handling for HTTP Requests failing due to error in inputs
    try:
        compare_forecasts(args.city1, args.city2)
    except Exception:
        print("One or both of the cities inputted are invalid. Please input a valid city name.")

def compare_forecasts(city1, city2):
    
    #Input API Token
    API_TOKEN = ''
    
    #HTTP Get Request for the first city's data for 5 days, and converting it to JSON format
    GETRequestCity1 = 'https://api.openweathermap.org/data/2.5/forecast/daily?q={}&appid={}&units=metric&cnt=5'.format(city1).format(API_TOKEN)
    ResponseCity1 = requests.get(GETRequestCity1)
    JSONResponseCity1 = ResponseCity1.json()

    #Rounding up the JSON response data for each Day's 'Maximum Temperature' for City 1
    TempCity1 = []
    for day in range(5):
        TempCity1.append(math.ceil(JSONResponseCity1['list'][day]['temp']['max']))

    #Collecting each day's weather description for City 1
    WeatherCity1 = []
    for day in range(5):
        WeatherCity1.append(JSONResponseCity1['list'][day]['weather'][0]['description'])

    #List of temperatures for city 1 for 5 days
    City1TempFor5Days = [TempCity1[0], TempCity1[1], TempCity1[2], TempCity1[3], TempCity1[4]]

    #List of weather descriptions for City 1 for 5 days
    City1WeatherFor5Days = [WeatherCity1[0], WeatherCity1[1], WeatherCity1[2], WeatherCity1[3], WeatherCity1[4]]

    #HTTP Get Request for the second city's data for 5 days, and converting it to JSON format
    GETRequestCity2 = 'https://api.openweathermap.org/data/2.5/forecast/daily?q={}&appid=fe9c5cddb7e01d747b4611c3fc9eaf2c&units=metric&cnt=5'.format(city2)
    ResponseCity2 = requests.get(GETRequestCity2)
    JSONResponseCity2 = ResponseCity2.json()

    #Rounding up the JSON response data for each Day's 'Maximum Temperature' for City 2
    TempCity2 = []
    for day in range(5):
        TempCity2.append(math.ceil(JSONResponseCity2['list'][day]['temp']['max']))

    #Collecting each day's weather description for City 2
    WeatherCity2 = []
    for day in range(5):
        WeatherCity2.append(JSONResponseCity2['list'][day]['weather'][0]['description'])

    #List of temperatures for city 2 for 5 days
    City2TempFor5Days = [TempCity2[0], TempCity2[1], TempCity2[2], TempCity2[3], TempCity2[4]]

    #List of weather descriptions for City 2 for 5 days
    City2WeatherFor5Days = [WeatherCity2[0], WeatherCity2[1], WeatherCity2[2], WeatherCity2[3], WeatherCity2[4]]

    print("")
    print("Weather forecast comparison between {} and {}:".format(city1, city2))
    print("")

    for day in range(5):
        print("Day {}:".format(day+1))

        #Logic to print out appropriate statement for the temperatures of both cities
        if City1TempFor5Days[day] < City2TempFor5Days[day]:
            print("{} ({}C) will be {}C cooler than {} ({}C).".format(city1, City1TempFor5Days[day], (City2TempFor5Days[day] - City1TempFor5Days[day]), city2, City2TempFor5Days[day]))
        elif City1TempFor5Days[day] > City2TempFor5Days[day]:
            print("{} ({}C) will be {}C warmer than {} ({}C).".format(city1, City1TempFor5Days[day], (City1TempFor5Days[day] - City2TempFor5Days[day]), city2, City2TempFor5Days[day]))
        else:
            print("{} and {} will both have the same temperature ({}C).".format(city1, city2, City1TempFor5Days[day]))

        #Logic to print out appropriate statement for the weather descriptions of both cities
        if City1WeatherFor5Days[day] == City2WeatherFor5Days[day]:
            print("{} and {} will both have {}.".format(city1, city2, City1WeatherFor5Days[day]))
        else:
            print("{} will have {}, but {} will have {}.".format(city1, City1WeatherFor5Days[day], city2, City2WeatherFor5Days[day]))

        if(day < 4):
            print("")

if __name__ == "__main__":
    main()
