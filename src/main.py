import get_data  

def main():
  data_dir='../data/'
  fname=data_dir+'cdc_sleep.json'
  url='https://chronicdata.cdc.gov/resource/eqbn-8mpz.json'
  df=get_data.get_df(url,fname)

  print(df.head())
if __name__=="__main__":
  main()
