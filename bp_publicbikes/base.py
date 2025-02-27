from bp_publicbikes import logger

import datetime

class Base:

    def __init__(self):
        self.logger = logger.StandardLogger().get_logger()       

    def _get_datetime_as_str(self) -> str:
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")