import os

FILE_NAME = "ip_list.csv"
URL = "https://get.geojs.io/v1/ip/geo.json?ip="
DIRECTORY = "Countryips/"
IS_EXIST = os.path.exists(DIRECTORY)
CHUNK_SIZE = 20
COUNTRY_KEY = 'country'
