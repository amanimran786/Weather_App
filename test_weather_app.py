import unittest
from unittest.mock import patch, MagicMock
from app import get_weather, temperature_label, humidity_label, wind_speed_label

class TestWeatherApp(unittest.TestCase):
    
    @patch('app.requests.get')
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
        city_entry = MagicMock()
        city_entry.get.return_value = "London"
        
        unit_var = MagicMock()
        unit_var.get.return_value = "Celsius"
        
        get_weather()
        
        expected_temperature = "Temperature: 20 °C"
        expected_humidity = "Humidity: 50 %"
        expected_wind_speed = "Wind Speed: 10 m/s"
        
        temperature_label.config.assert_called_once_with(text=expected_temperature)
        humidity_label.config.assert_called_once_with(text=expected_humidity)
        wind_speed_label.config.assert_called_once_with(text=expected_wind_speed)
    
    @patch('app.requests.get')
    def test_get_weather_city_not_found(self, mock_get):
        # Mock the response from the API
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": "404"
        }
        mock_get.return_value = mock_response
        
        # Test the function with a city that is not found
        city_entry = MagicMock()
        city_entry.get.return_value = "InvalidCityName"
        
        unit_var = MagicMock()
        unit_var.get.return_value = "Celsius"
        
        get_weather()
        
        temperature_label.config.assert_called_once_with(text="City not found")

if __name__ == '__main__':
    unittest.main()
