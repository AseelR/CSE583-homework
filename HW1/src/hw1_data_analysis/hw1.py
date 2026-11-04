import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("bicycle_data.csv")
print(df.columns)

# datatypes seem to be floats for the total, West sidewalk, and East sidewalk 
# but the date is currently a string when it should be a datetime format since it includes date and time 
print(df.dtypes)
print(df.shape)


df["Date"] = pd.to_datetime(df["Date"],format="%m/%d/%Y %I:%M:%S %p")

df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year
df["Total"] = df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"] + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]


df_2016 = df[df["Year"] == 2016].copy()
print(df_2016.isna().sum())