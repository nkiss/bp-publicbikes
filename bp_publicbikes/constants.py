"""
bp_publicbikes base module.

This is the principal module of the bp_publicbikes project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

# example constant variable
NAME = "bp_publicbikes"
CITIBIK_BUBI_URL = 'http://api.citybik.es/v2/networks/bubi'
OPENMETEO_API_URL = "https://api.open-meteo.com/v1/forecast?latitude=47.4984&longitude=19.0404&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,rain,showers,snowfall,cloud_cover,wind_speed_10m,wind_direction_10m,wind_gusts_10m&timezone=Europe%2FBerlin&forecast_days=1"
