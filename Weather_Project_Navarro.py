# Weather Application
# Rosie Navarro
# June 2026

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt
from weather_API import api_key


class WeatherApp(QWidget):
    """
    Weather application showing current weather for a city
    using the OpenWeatherMap API.
    """
    def __init__(self):
        """
        Starts the weather app window and creates the widgets.
        """
        super().__init__()

        # Input label where user can enter city.
        self.city_label = QLabel("Enter City:", self)
        self.city_input = QLineEdit(self)

        #Botton that user can press.
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel("Temperature:", self)
        self.description_label = QLabel("Description:", self)
        self.emoji_description = QLabel(self)
        self.feels_like_label = QLabel("Feels Like:", self)
        self.initUI()

    def initUI(self):
        """
        Window layout, widget alignment, object name, and botton
        signal connection.
        """
        self.setWindowTitle("Weather Project Navarro")

        vbox = QVBoxLayout()

        # Layout of the app
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.feels_like_label)
        vbox.addWidget(self.emoji_description)

        self.setLayout(vbox)

        # Centers the labels and inputs.
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_description.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.feels_like_label.setAlignment(Qt.AlignCenter)


        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temp_label.setObjectName("temp_label")
        self.emoji_description.setObjectName("emoji_description")
        self.description_label.setObjectName("description_label")
        self.feels_like_label.setObjectName("feels_like_label")


        self.setStyleSheet("""
            QLabel#city_label{
                font-size: 20px;
            }
            QLineEdit#city_input{
                font-size: 20px;
            }
            QPushButton#get_weather_button{
                font-size: 20px;
                font-weight: bold;
            }
            
            QLabel#emoji_description{
                font-size: 50px;
                font-family: Segoe UI emoji;
            }
            """)

        # Connect button to get_weather method.
        self.get_weather_button.clicked.connect(self.get_weather)



    def get_weather(self):
        """
        Request from API and calls information about current weather conditions.
        Handles specific HTTP errors and connection issues with a message for the user.
        """

        # Gets city from the input field
        city = self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Showing response code is working.
            if data["cod"] == 200:
                self.display_weather(data)

        # specific HTTP errors that the user could see- with message.
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                self.temp_label.setText("City not found, check input")
            elif response.status_code == 401:
                self.temp_label.setText("Unauthorize, validate API key")
            elif response.status_code == 500:
                self.temp_label.setText("Server error")
            else:
                self.temp_label.setText("HTTP Error")


        except requests.exceptions.ConnectionError:
            self.temp_label.setText("Connection Error, check Internet connection")
        except requests.exceptions.RequestException:
            self.temp_label.setText(f"Request Error:\n")



    def display_errors(self, message):
        """
        Displays error message in temp label and clears the emoji if there is an error.
        Args:
            message (str): the error message to display.
        """
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)
        self.emoji_description.clear()

    def weather_emoji(self, weather_id):
        """
        Returns and emoji that represents the current weather based on condition ID.
        Args:
            weather_id(int): condition id from API response
        Return:
            str: emoji string matching weather conditions.
        """

        # thunder storm
        if 200 <= weather_id <= 232:
            return "⛈️"
        # Drizzle
        elif 300 <= weather_id <= 321:
            return "☁️"
        # Rain
        elif 500 <= weather_id <= 531:
            return "🌧️"
        # Snow
        elif 600 <= weather_id <= 622:
            return "❄️"
        # Foggy conditions
        elif 700 <= weather_id <= 741:
            return "🌁"
        # Volcano erruption
        elif weather_id == 762:
            return "🌋"
        # Squall
        elif weather_id == 771:
            return "💨"
        # Tornado
        elif weather_id == 781:
            return "🌪️"
        # Clear sky
        elif weather_id == 800:
            return "☀️"
        # CLoudy range
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


    def display_weather(self, data):
        """
        Parse API JSON response and updates all labels with current temp, feels like,
        description, and emoji.
        agrs:
            data (dict): JSON response dictionary from weather API.
        """
        temp_k = data["main"]["temp"]
        temp_f = round((temp_k - 273.15) * 9/5 + 32)

        feels_like_k = data["main"]["feels_like"]
        feels_like = round((feels_like_k - 273.15) * 9/5 + 32)

        description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]


        self.temp_label.setText(f"Temperature: {temp_f} °F")
        self.feels_like_label.setText(f"Feels Like: {feels_like} °F")
        self.description_label.setText(f"Sescription: {description}")
        self.emoji_description.setText(self.weather_emoji(weather_id))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())







