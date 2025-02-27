import bp_publicbikes.constants as constants
from bp_publicbikes.base import Base
import requests


class Citybike(Base):

    def _write_json_response(self, json):
        if json is None:
            self.logger.warning("No Bubi data to process")
            return
        
        station_data = json['network']['stations']
        if station_data is None:
            self.logger.warning("No Bubi station data to process")
            return

        try:
            file_name = f"bubi_{self._get_datetime_as_str()}.json"
            with open(file_name, 'w') as f:
                f.write(str(station_data))
            self.logger.info("Bubi data written to Data Lake")
        except Exception as e:
            self.logger.warning(f"Failed to process Bubi data: {e}")
            raise e

    def _citybikes_api(self) -> dict:
        try:
            self.logger.info(f"Calling Bubi API: {constants.CITIBIK_BUBI_URL}")
            response = requests.get(constants.CITIBIK_BUBI_URL)

            response.raise_for_status()
            if response.status_code == 200:
                return response.json()
            
        except Exception as e:
            self.logger.warning(f"Failed to get Bubi data: {e}")
            raise e

    def citybikes_data(self) -> dict:
        json_data = self._citybikes_api()
        self._write_json_response(json_data)