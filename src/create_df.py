# read the data from the file
fname='../data/cdc_sleep.json'

try:
  file=open(fname, 'r')
  data=file.read()

  file.close()
except OSError:
  print('OSError Could not open/read file')

# convert the data to a pandas dataframe
df = pd.read_json(data)
