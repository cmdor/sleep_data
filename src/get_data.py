import requests
import pandas as pd

# get the data from the cdc
url = "https://chronicdata.cdc.gov/resource/eqbn-8mpz.json"
resp = requests.get(url=url)
data = resp.json() # Check the JSON Response Content documentation below

# write the data to the data/ directory
fname='../data/cdc_sleep.json'
try:
  file=open(fname, 'w')
  file.write(str(data))
  file.close()
except OSError:
  print('OSError Could not open/read file')
