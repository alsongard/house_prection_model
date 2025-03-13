import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
data_df = pd.read_csv("./california_house_dataset/housing.csv")
print(data_df)
print(f"Spape of data_df is {data_df.shape}")

print(data_df.isnull().sum()) # missing 207 null values

data_df = data_df.dropna()
print(f"Spape of data_df is {data_df.shape}")

print(data_df.info())


x_features = data_df.drop(["median_house_value"], axis=1)
y_features = data_df["median_house_value"]

print(x_features)

# split the data
x_train, x_test, y_train, y_test = train_test_split(x_features, y_features, test_size=0.33, random_state=42)


# combine the dataframe
train_data = x_train.join(y_train)
print(train_data)

print(train_data.hist(figsize=(15,8)))
plt.show()

train_data = train_data.drop(["ocean_proximity"], axis=1)
# check the correlation between values
print(train_data.corr())

# plot a heatmap to view the correlation between values
plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(), annot=True, cmap="YlGnBu")
plt.show()