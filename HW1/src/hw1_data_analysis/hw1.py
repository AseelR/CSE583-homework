import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("bicycle_data.csv")
print(df.columns)


print(df.dtypes)
print(df.shape)

# columns in df:
# date: originally a string, but shpuld convert to datetime for easier processing later
# total: num of cyclists crossing the bridge (float64)
# west sidewalk: num of cyclists on the west sidewalk (float64 dtype)
# east sidewalk: num of cyclists on the east sidewalk (float64 dtype)
 

df["Date"] = pd.to_datetime(df["Date"],format="%m/%d/%Y %I:%M:%S %p")

df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year
df["Total"] = df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"] + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]


# we have 1 row/data points missing information in the (original) total, east, and west columns 
# since it is only one observation of many thousand, we will drop it 
df_2016 = df[df["Year"] == 2016].copy() 
print(df_2016.isna().sum())
df_2016 = df_2016.dropna(subset=["Total"])
print(df_2016.isna().sum()) # confirm that the 1 missing row is removed 

# need to get the avg bikes crossing per hour of day, across all days in 2016 
hourly_avg = df_2016.groupby("Hour")["Total"].mean()

hourly_avg.plot(kind="bar")
plt.title("Average Bicycle Counts by Hour (2016)")
plt.xlabel("Hour of Day")
plt.ylabel("Average Bicycle Count")
plt.savefig("counts_by_hour.png")


# getting the highest hour -> use the idmax fxn not max, we want highest avg count, not the highest average count itself
busiest_hour = hourly_avg.idxmax()
print("Busiest hour:", busiest_hour) # busiest hour is 17:00, so 5pm 