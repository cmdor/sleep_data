import os
import requests
import pandas as pd
import json

def get_data(url,fname):
  resp = requests.get(url=url)
  data = resp.json()
  try:
    with open(fname, "w") as file:
      json.dump(data, file)
    file.close()
  except OSError:
    print('OSError Could not open/read file')

def get_df(url, fname):
  # read the data from the file

  data=None
  
  if(not os.path.exists(fname)):
    get_data(url,fname)
    get_df(url, fname)
  else:
    df = pd.read_json(fname)
    return df

