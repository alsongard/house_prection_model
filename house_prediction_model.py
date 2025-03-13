import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

data_df = pd.read_csv("./california_house_dataset/housing.csv")
print(data_df)

print(data_df.isnull().sum()) # missing 207 null values

data_df = data_df.dropna()

print(data_df.info())


# check the correlation between the data 
# when performing correlation you need to have only features with numerical data
# dropping ocean_proximity
ocean_proximity_df = data_df["ocean_proximity"]
data_df = data_df.drop(["ocean_proximity"], axis=1)
correlation_matrix = data_df.corr()
# to plot using sns
plt.figure(figsize=(15,8))
print(correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, cmap="Blues")
plt.xticks(rotation=45, ha='right')
plt.title("Correlation matrix Heatmap of the Different data features")
# plt.tight_layout()
# plt.show()


# transform the features which have a positive skew to have normal distribution
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
total_room skew value is : 4.15881642276731 : positive skew
house_hold skew value is : 3.413850191065247 : positive skew
total_bedrooms skew value is : 3.4595463315233417 : positive skew
population skew value is : 4.96001654238539 :positive skew

# comparison 
longitude skew value is : -0.2961409005750841
latitude skew value is 0.4649342770118454
house_median_age skew value is 3.413850191065247 : positive skew
median_house_value_skew is 0.9782898908925552
"""

data_df.hist()

data_df["households"] = np.log1p(data_df["households"])
data_df["population"] = np.log1p(data_df["population"])
data_df["total_rooms"] = np.log1p(data_df["total_rooms"])
data_df["total_bedrooms"] = np.log1p(data_df["total_bedrooms"])


data_df.hist()
# plt.show()


# perform one-hot encoding for the ocean_proximity feature
# print(ocean_proximity_df)
data_df = data_df.join(ocean_proximity_df)
print(data_df)

new_ocean_proximity_values = pd.get_dummies(data_df["ocean_proximity"])
print(new_ocean_proximity_values)
print(new_ocean_proximity_values.info()) # new features have boolean values 

value_mapping = {True: 1, False: 0}
new_ocean_proximity_values["<1H OCEAN"] =new_ocean_proximity_values["<1H OCEAN"].map(value_mapping)
new_ocean_proximity_values["INLAND"] =new_ocean_proximity_values["INLAND"].map(value_mapping)
new_ocean_proximity_values["ISLAND"] =new_ocean_proximity_values["ISLAND"].map(value_mapping)
new_ocean_proximity_values["NEAR BAY"] =new_ocean_proximity_values["NEAR BAY"].map(value_mapping)
new_ocean_proximity_values["NEAR OCEAN"] =new_ocean_proximity_values["NEAR OCEAN"].map(value_mapping)

# print(new_ocean_proximity_values.value_counts())
"""
<1H OCEAN  INLAND  ISLAND  NEAR BAY  NEAR OCEAN
1          0       0       0         0             9034
0          1       0       0         0             6496
           0       0       0         1             2628
                           1         0             2270
                   1       0         0                5
Name: count, dtype: int64
"""

data_df = data_df.join(new_ocean_proximity_values)

data_df = data_df.drop(["ocean_proximity"], axis=1)
# print(data_df.info())

# after this check how  these new features correlate with the target value = median_house_value
correlation_matrix = data_df.corr()
plt.figure(figsize=(15,8))
print(correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, cmap="Blues")
plt.xticks(rotation=45, ha='right')
plt.title("Correlation matrix Heatmap with New Features and Normalized Distributed Data")
# plt.show()


plt.figure(figsize=(15, 8))
sns.scatterplot(x="latitude", y="longitude", data=data_df, hue="median_house_value", palette="coolwarm")
plt.title("Scatter Plot for longitude vs latitude")
# plt.show()

#  totalRooms: Total number of rooms within a block
# households: Total number of households, a group of people residing within a home unit, for a block
"""
1. totalRooms: Total number of rooms within a blocks
Correct Interpretation: The description states that totalRooms refers to the total number of rooms within a block,
not just a single house. A block typically refers to a group of houses or a neighborhood area, so this feature represents
the sum of all rooms across multiple housing units in that block.
Example: If a block has 10 houses, and each house has 5 rooms, then totalRooms would be 50.

2. households: Total number of households, a group of people residing within a home unit, for a block
Correct Interpretation: The description states that households refers to the total number of households within a block, not the number of people.
A household is defined as a group of people (e.g., a family) living together in a single home unit. So, this feature counts 
the number of such units (households) in a block, not the number of individuals.
Example: If a block has 10 houses, and each house is occupied by one family, then households would be 10, regardless of how many people live in each house.
"""
data_df["household_rooms"] =  data_df["total_rooms"] / data_df["households"] 

correlation_matrix = data_df.corr()
plt.figure(figsize=(15,8))
print(correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, cmap="Blues")
plt.xticks(rotation=45, ha='right')
plt.title("Latest Correlation matrix Heatmap with Additional Features")
# plt.show()


print(data_df.info())
# get target feature

target_df = data_df["median_house_value"]
features_df  = data_df.drop("median_house_value", axis=1)
# print(target_df)
# print(features_df.info())

# split the dataset
x_train, x_test, y_train, y_test = train_test_split(features_df, target_df, test_size=0.33, random_state=42)


print("x_train dataframe")
print(x_train)

print("y_train dataframe")
print(y_train)


print("x_test dataframe")
print(x_test)

print("y_test dataframe")
print(y_test)

regression_model = LinearRegression()
regression_model.fit(x_train, y_train)

y_predicted_values = regression_model.predict(x_test)


## evaluate the MODEL

# Measures the average absolute difference between predicted and actual values.
mean_error = mean_absolute_error(y_test, y_predicted_values)

#  R² Score (Coefficient of Determination) Measures how well the independent variables explain the variance in the dependent variable.
print(regression_model.score(x_test, y_test)) # -.677 (no correlation)

# loser to 1 means better fit, 0 means no correlation, and negative values indicate a poor fit.
# print("y_test")
# print(y_test)
# print("y_predicted_values")
# print(y_predicted_values)


# print(mean_error)