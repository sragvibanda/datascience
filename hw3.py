"""
1)Filter the data to include only weekdays (Monday to Friday) 
and plot a line graph showing the pedestrian counts for each day 
of the week.


3) Implement a custom function to categorize time of day 
into morning, afternoon, evening, and night, and create a 
new column in the DataFrame to store these categories. Use 
this new column to analyze pedestrian activity patterns 
throughout the day.

"""

import pandas as pd # question 1
import matplotlib.pyplot as plt

data_url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
read_url = pd.read_csv(data_url)

read_url["hour_beginning"] = pd.to_datetime(read_url["hour_beginning"])
weekdays = read_url[(read_url["hour_beginning"].dt.dayofweek >= 0) & (read_url["hour_beginning"].dt.dayofweek <= 4)]
agg_ped_daily_count = weekdays.groupby(weekdays["hour_beginning"].dt.day_name())["Pedestrians"].sum()

plt.figure(figsize=(10,6))
agg_ped_daily_count.plot(kind="line", marker = "o")
plt.title("Total Pedestrians per day of the week")
plt.xlabel("Day of the week")
plt.ylabel("Numbe of Pedestrians")
plt.grid(True)
plt.show()

import seaborn as sns #question 2

brooklyn_bridge2019 = read_url[(read_url["location"] == "Brooklyn Bridge") & (read_url["hour_beginning"].dt.year == 2019)]
encoded_weather = pd.get_dummies(brooklyn_bridge2019["weather_summary"])
encoded_data = pd.concat([encoded_weather, brooklyn_bridge2019["Pedestrians"]], axis=1)

corr_matrix = encoded_data.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix of Pedestrians and Weather")
plt.show()


def time_of_day_categorize(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    elif 18 <= hour < 24:
        return "Evening"
    else:
        return "Night"
    
read_url["time_of_day"] = read_url["Hour_beginning"].dt.hour.apply(time_of_day_categorize)
num_peds_time_of_day = read_url.groupby("time_of_day")["Pedestrians"].sum()
print("Pedestrian Activity Patterns throughout the day:")
print(num_peds_time_of_day)
