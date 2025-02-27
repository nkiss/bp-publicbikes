import os
import logging
import logging.config
import yaml
from threading import Lock
import datetime

import bp_publicbikes.constants as constants

class StandardLogger:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        # Load YAML logging config
        config_path = os.path.join(os.path.dirname(__file__), "logging_config.yaml")
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        # Generate dynamic filename with current date
        log_filename = f"/var/log/{constants.NAME}_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"

        # Update the filename in the config dictionary
        config["handlers"]["file"]["filename"] = log_filename

        # Apply the updated configuration
        logging.config.dictConfig(config)
        
        self.logger = logging.getLogger("base_logger")

    def get_logger(self):
        return self.logger