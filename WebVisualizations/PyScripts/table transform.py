import pandas as pd
import os


filename = os.path.join('..','Resources','cities.csv')
outputname = os.path.join('..','Resources','cities.html')
df=pd.read_csv(filename)
df['City']=df['City'].str.title()
df['Date']=pd.to_datetime(df['Date'],unit='s')
df_html=df.to_html(outputname,index=False)