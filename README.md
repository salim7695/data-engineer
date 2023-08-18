# Requirements

`Python 3.8`

In project directory install the requirements via

`pip3 install -r requirements.txt`

### A brief Introduction:

Add IP adresses in `ip_list.csv` file similar data has been added please follow the same pattern 1 IP each line. 

Script is reading the above mentioned file and creates an array for all the IPs and in the chunks of 20. Chunk of 20 is for consistent load on API to fetch data. Once response is received it will save into respective file according to country name.

### How to run:

Open the terminal in project directory and run 

`python main.py`

If python 3 is installed

`python3 main.py`
