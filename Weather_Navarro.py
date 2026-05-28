# Weather project
# Rosie Navarro-Martinez
# May 2026
# Weather application that looks up current weather conditions by zip or city/state

import requests

api_key = "62884bbc1da29106956a7554d891626a"


def welcome_message():
    """
    Displays welcome message to the user
    """
    print("Hello user, welcome to the Weather App!! ")
    print("="* 70)


def get_location(city, state):
    """
    Description: gets location from API. Gets the latitude and the longitude from the city/state.
        makes the call from the OpenWeatherMap API.
    parameter:
        city (str): name of city
        state (str): name of state
    return: tuple from lat/lon or if nothing is found nothing is returned.
    """

    # url for the city and state
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid={api_key}"


    try:
        # API requests
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()


        if not data: # Nothing is returned if API returns nothing
            return None, None

        # results from lat and lon results.
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon

    # HTTP error exceptions and other exceptions that could be encountered.
    except requests.exceptions.HTTPError as http_err:
        status_code = http_err.response.status_code

        if status_code == 401:
            print("Unauthorized, validate API key")
        elif status_code == 500:
            print("Server error")
        else:
            print("HTTP Error")

        return None, None

    except requests.exceptions.ConnectionError:
        print("Connection Error, check Internet connection")
        return None, None

    except requests.exceptions.RequestException:
        print(f"Request Error:\n")
        return None, None


def get_zip_location(zip_code):
    """
    Looks up latitude and longitude for a zip code. Makes the call
    from the OpenWeatherMap API.

    parameter:
        zip_code (str): US Zip codes

    return: tuple of lat/lon or nothing if location is not found.
    """
    # URL to look up zip codes
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={api_key}"

    # API requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # returns dictionary, not list.
        lat = data["lat"]
        lon = data["lon"]
        return lat, lon

    # HTTP error exceptions or other exceptions that could be encountered.
    except requests.exceptions.HTTPError as http_err:
        status_code = http_err.response.status_code
        if status_code == 401:
            print("Unauthorized, validate API key")
        elif status_code == 500:
            print("Server error")
        else:
            print("HTTP Error")

        return None, None

    except requests.exceptions.ConnectionError:
        print("Connection Error, check Internet connection")
        return None, None

    except requests.exceptions.RequestException:
        print(f"Request Error:\n")
        return None, None



def get_weather(lat, lon, units):
    """
    Gets weather information from a specific latitude and longitude.
        makes the call from OpenWeatherMap API
    parameter:
        lat (float): latitude of location
        lon (float):longitude of location
        units (float): temperature in units (imperial, metric, or standard).
    return: weather data or nothing if the request fails.
    """
    # forecast URL using coordinates
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}"

    # API request
    try:
        response = requests.get(url)  # GET request to API
        response.raise_for_status()  # HTTP statues code for exceptions
        data = response.json()
        return data

    # HTTP Error handling and other exceptions.
    except requests.exceptions.HTTPError as http_err:
        status_code = http_err.response.status_code
        if status_code == 401:
            print("Unauthorized, validate API key")
        elif status_code == 500:
            print("Server error")
        else:
            print("HTTP Error")

        return None

    except requests.exceptions.ConnectionError:
        print("Connection Error, check Internet connection")
        return None
    except requests.exceptions.RequestException:
        print(f"Request Error:\n")
        return None




def display_weather(data, unit_symbol):
    """
    Displays weather in a readable format. Extracts and prints
        temperature, description, humidity, pressure, cloud coverage, min,
        max temperatures for the day.
    parameter:
        data (dict): weather data returned from API
        unit_symbol (str): symbol for temperature
    return: none
    """

    # City name form the data that the user chooses
    city_name = data["city"]["name"]
    # get the first forecast entry of current condition
    first_forecast = data["list"][0]
    temp = first_forecast["main"]["temp"]
    description = first_forecast["weather"][0]["description"]
    feels_like = first_forecast["main"]["feels_like"]
    humidity = first_forecast["main"]["humidity"]
    pressure = first_forecast["main"]["pressure"]
    clouds = first_forecast["clouds"]["all"]

    # uses 8 entries to find the high and low temperatures of the day
    temps = [item["main"]["temp"] for item in data["list"][:8]]
    high_temp = max(temps)
    low_temp = min(temps)

    # Display all weather information.
    print(f"\n======== Weather for {city_name} =======")
    print(f"Description: {description.capitalize()}")
    print(f"Current Temperature: {round(temp)} {unit_symbol}")
    print(f"Feels like: {round(feels_like)} {unit_symbol}")
    print(f"High: {round(high_temp)} {unit_symbol}")
    print(f"Low: {round(low_temp)} {unit_symbol}")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure}hPa")
    print(f"Clouds Coverage: {clouds}%")


def search_choice():
    """
    Asks the user if they want to find their location through zip code
        or city/state. Loops in case there is some sort of invalid entry.
    return: tuple of lat and long from location.
    """

    while True:
        # asks user how they want to search
        print("choose how you want to search location: 1- Zip Code, 2- City & State")
        user_choice = input("Enter choice: ")

        if user_choice == "1": # Uses Zip code to find location
            while True:
                zip_code = input("Enter zip code: ")
                lat, lon = get_zip_location(zip_code)
                if lat is not None:
                    return lat, lon
                else: # asks user to check entry and reenter zip code
                    print("Invalid zip code. Check input again")
        elif user_choice == "2": # uses city to find location
            while True:
                city = input("Enter City: ")
                state = input("Enter State: ")
                lat, lon = get_location(city, state)
                if lat is not None:
                    return lat, lon
                else: # Asks user to check their entry and makes the reenter.
                    print("Invalid city. Check input again")
        else:
            print("Invalid choice, please 1 or 2")
            continue



def user_temp_choice():
    """
    Asks the user how they want their temperature to be displayed.
    User has three choices, Fahrenheit, Celsius, Kelvin.
    return:
        units (str): API unit system
        unit symbol (str): symbol for temperature
    """
    while True:
        # Shows user options to display temperature.
        print("Select one of the following temperature units: 1-Fahrenheit, 2-Celsius, 3-Kelvin")
        unit_choice = input("Enter choice: ")

        if unit_choice == "1":
            units = "imperial"
            unit_symbol = "°F"
        elif unit_choice == "2":
            units = "metric"
            unit_symbol = "°C"
        elif unit_choice == "3":
            units = "standard"
            unit_symbol = "K"
        else:
            print("Invalid choice, please select one of the following")
            continue

        return units, unit_symbol


def main():
    """
    Functions that controls the flow of the program.
    Call other functions and allows the user to use and look weather
    information for a given location, they can look up multiple locations.
    return: none
    """

    # displays welcome message
    welcome_message()
    # gets temperature unit preference from user
    units, unit_symbol = user_temp_choice()

    while True:
        # gets location from user and gets weather data
        lat, lon = search_choice()

        if lat is None:
            print("location is not found")
        else:
            # displays weather for the location
            data = get_weather(lat, lon, units)
            if data is None:
                print("Could not retrieve data")
            else:
                display_weather(data, unit_symbol)


        while True:
            # asks the user if they want to look up another location
            again = input(f"\n Do you want another location (Y/N): ").lower()
            if again == "y":
                break
            elif again == "n":
                print("Thank you for using the program! Goodbye!")
                return
            else:
                print("Invalid choice, enter 'y' or 'n'.")



if __name__ == "__main__":
    main()



