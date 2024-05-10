import unittest
from unittest.mock import patch, MagicMock
from weather_logic import get_weather


class TestWeatherApp(unittest.TestCase):
    
    @patch('weather_logic.requests.get')
    def test_get_weather_success(self, mock_get):
        # Mock the response from the API
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": 200,
            "main": {
                "temp": 20,
                "humidity": 50
            },
            "wind": {
                "speed": 10
            }
        }
        mock_get.return_value = mock_response
        
        # Test the function with a valid city
        city = "London"
        unit = "Celsius"
        
        data = get_weather(city, unit)
        
        # Check if data is returned correctly
        self.assertEqual(data["main"]["temp"], 20)
        self.assertEqual(data["main"]["humidity"], 50)
        self.assertEqual(data["wind"]["speed"], 10)

    @patch('weather_logic.requests.get')
    def test_get_weather_city_not_found(self, mock_get):
        # Mock the response from the API
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": "404"
        }
        mock_get.return_value = mock_response
        
        # Test the function with a city that is not found
        city = "InvalidCityName"
        unit = "Celsius"
        
        data = get_weather(city, unit)
        
        # Check if "cod" is "404" indicating city not found
        self.assertEqual(data["cod"], "404")

if __name__ == '__main__':
    unittest.main()
