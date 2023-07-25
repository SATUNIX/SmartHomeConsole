#





import requests
from EventLogger import EventLogger

class WeatherGrabber:
    def __init__(self, city='Brisbane,AU'):
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'
        self.api_key = 'your_api_key'
        self.city = city

    def get_weather_data(self):
        params = {'q': self.city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.base_url, params=params)
        data = response.json()

        return data

    def log_weather_data(self):
        data = self.get_weather_data()

        # Log Temperature
        try:
            temperature = data['main']['temp']
            EventLogger.log_event('Temperature', str(temperature))
        except Exception as e:
            logging.error(f"Error logging Temperature: {str(e)}")

        # Log Humidity
        try:
            humidity = data['main']['humidity']
            EventLogger.log_event('Humidity', str(humidity))
        except Exception as e:
            logging.error(f"Error logging Humidity: {str(e)}")

        # Log UV index (UV index is not provided by OpenWeatherMap in their free tier)
        # You might need to use a different service to get this data.

        # Log Precipitation (Rain volume for the last 1 hour)
        try:
            precipitation = data.get('rain', {}).get('1h', 0)
            EventLogger.log_event('PrecipitationChance', str(precipitation))
        except Exception as e:
            logging.error(f"Error logging PrecipitationChance: {str(e)}")

        # PM2.5 is also not provided by OpenWeatherMap API in their free tier.
        # You will need to use a different service to get this data.

if __name__ == "__main__":
    wg = WeatherGrabber()
    wg.log_weather_data()


'''
Please note that you will need to use different services for PM2.5 and UV index as OpenWeatherMap does not provide these in their free tier.
 These services will have their own APIs and you'll need to write separate code to interact with them.

Furthermore, the precipitation logged here is actually the rain volume for the last 1 hour, which might differ from the concept of precipitation chance you intended.
 You may need to use additional services or algorithms to estimate the precipitation chance based on the provided weather data.
'''







#
