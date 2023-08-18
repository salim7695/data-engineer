import csv
import requests
import os
from constants import *

fields = []
ips = []

def check_directory():
	if not IS_EXIST:
		os.makedirs(DIRECTORY)

def split_ips(ips_list):

  for i in range(0, len(ips_list), CHUNK_SIZE):
    yield ips_list[i:i + CHUNK_SIZE]

def get_file_name(country):
	return f"{DIRECTORY}{country}.txt"

def write_response(response):
	for data in response:
		if COUNTRY_KEY in data:
			file = open(get_file_name(data['country']), 'a+')
			file.write(f"{data['ip']} \n")
			file.close()
			print(data['country'])

with open(FILE_NAME, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile)
     
    fields = next(csvreader)
 
    for row in csvreader:
        ips.extend(row)

check_directory()

for chunk in list(split_ips(ips)):
	payload = ",".join(chunk)
	response = requests.get(url=URL+payload)
	if response.status_code in range(200, 299):
		write_response(response.json())
