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


"""
the hist() function shows the distribution of data
histogram show the distribution of data specifically numerical data
"""
# data_df.hist() # as expected this only shows the hist() of numerical data

# to check the individual feature histogram
data_df["median_house_value"].hist()
# plt.show()

print(data_df["households"])
