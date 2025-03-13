"""
this file will be used for analysis, including the following:

- checking the skewedness of data features
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
data_df = pd.read_csv("./california_house_dataset/housing.csv")
print(data_df)
# print(f"Spape of data_df is {data_df.shape}")

print(data_df.isnull().sum()) # missing 207 null values

data_df = data_df.dropna()
# print(f"Spape of data_df is {data_df.shape}")

print(data_df.info())


## checking the skew of the data
"""
positive skew: right tail(right skewed)
negative skew: left tail(left skewed)
"""


total_room_skew_value = data_df["total_rooms"].skew()
house_holds_skew_value = data_df["households"].skew()
total_bedrooms_skew_value = data_df["total_bedrooms"].skew()
population_skew_value = data_df["population"].skew()

print(f"total_room skew value is : {total_room_skew_value}")
print(f"house_hold skew value is : {house_holds_skew_value}")
print(f"total_bedrooms skew value is : {total_bedrooms_skew_value}")
print(f"population skew value is : {population_skew_value}")

# compare with the features which seem to have a normal distribution based on the histogram
longitude_skew_value = data_df["longitude"].skew()
latitude_skew_value = data_df["latitude"].skew()
house_median_age_skew_value = data_df["housing_median_age"].skew()
median_house_value_skew = data_df["median_house_value"].skew()

print(f"longitude skew value is : {longitude_skew_value}")
print(f"latitude skew value is {latitude_skew_value}")
print(f"house_median_age skew value is {house_holds_skew_value}")
print(f"median_house_value_skew is {median_house_value_skew}")

"""
total_room skew value is : 4.15881642276731
house_hold skew value is : 3.413850191065247
total_bedrooms skew value is : 3.4595463315233417
population skew value is : 4.96001654238539
longitude skew value is : -0.2961409005750841
latitude skew value is 0.4649342770118454
house_median_age skew value is 3.413850191065247
median_house_value_skew is 0.9782898908925552
"""

# ploting using KDE to see curve
sns.kdeplot(data_df["total_rooms"], fill=True, color='skyblue')
plt.axvline(data_df["total_rooms"].mean(), color="red", label="mean", linestyle="dashed")
plt.axvline(data_df["total_rooms"].median(), color="green", label="median", linestyle='dashed')
plt.legend()
plt.title("Total Rooms vs skewness")
plt.xlabel("Rooms")
plt.ylabel("Density")
plt.show()


print(data_df["total_rooms"].max())

data_df["latitude"]

sns.kdeplot(data_df["latitude"], fill=True, color='skyblue')
plt.axvline(data_df["latitude"].mean(), color="red", label="mean", linestyle="dashed")
plt.axvline(data_df["latitude"].median(), color="green", label="median", linestyle='dashed')
plt.legend()
plt.title("Latitude vs skewness")
plt.xlabel("Latitude")
plt.ylabel("Density")
plt.show()