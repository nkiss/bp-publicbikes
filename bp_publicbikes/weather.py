import bp_publicbikes.constants as constants
import bp_publicbikes.logger as logger
from bp_publicbikes.base import Base

import requests


class Weather(Base):

    def _call_weather_api(self) -> tuple:
        try:
            url = constants.OPENMETEO_API_URL
            self.logger.info(f"Calling weather API: {url}")
            response = requests.get(url)
            
            response.raise_for_status()

            json_data = response.json()
            units = json_data['current_units']
            current = json_data['current']
            return units, current
        except Exception as e:
            self.logger.warning(f"Failed to get weather data: {e}")
            raise e

    def weather_data(self) -> None:
        try:
            units, current = self._call_weather_api()
            self.logger.info("Weather data processed successfully")

            file_name = f"units_{self._get_datetime_as_str()}.json"
            with open(file_name, 'w') as f:
                f.write(str(units))
            self.logger.info("Units data of written to Data Lake")

            weather_data = f"weather_{self._get_datetime_as_str()}.json"
            with open(weather_data, 'w') as f:
                f.write(str(current))
            self.logger.info("Weather data written to Data Lake")

        except Exception as e:
            self.logger.warning(f"Failed to process weather data: {e}")