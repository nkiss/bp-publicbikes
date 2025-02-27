import bp_publicbikes.constants as constants
from bp_publicbikes.logger import StandardLogger

from bp_publicbikes.weather import Weather
from bp_publicbikes.publicbikes import Citybike


def main():
    logger = StandardLogger().get_logger()
    
    logger.info(f"Start {constants.NAME}")
    Weather().weather_data()
    Citybike().citybikes_data()
    logger.info(f"End {constants.NAME}")