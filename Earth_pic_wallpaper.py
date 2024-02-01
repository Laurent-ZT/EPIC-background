import json
import os
import pathlib
import ssl
import requests
from math import cos, pi
from ctypes import windll

# Constants
LONGITUDE_CITY = 1.349014
NASA_URL = 'https://epic.gsfc.nasa.gov/api/natural'
HOME = str(pathlib.Path.home())
FOLDERNAME_CITY = 'Earth_pics'

# Set up SSL context
ssl._create_default_https_context = lambda: ssl.create_default_context()

# Make HTTP request to NASA API
response = requests.get(NASA_URL)
Images_medadata = response.json()

# Find the image closest to the city
best_i_city = min(Images_medadata, key=lambda Image_medadata: 1 - cos((Image_medadata['centroid_coordinates']['lon'] - LONGITUDE_CITY) * pi / 180))

# Build the URL for the image
pic_city = f'https://epic.gsfc.nasa.gov/archive/natural/{best_i_city["date"][:4]}/{best_i_city["date"][5:7]}/{best_i_city["date"][8:10]}/png/{best_i_city["image"]}.png'

# Create folder if it doesn't exist
folder_path = pathlib.Path(HOME) / "Pictures" / FOLDERNAME_CITY
folder_path.mkdir(parents=True, exist_ok=True)

# Download the image to the folder
file_path = folder_path / 'Earth.png'
with file_path.open('wb') as f:
    f.write(requests.get(pic_city).content)

# Set the image as wallpaper
SPI_SETDESKWALLPAPER = 20
windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(file_path), 0)
