import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
data_df = pd.read_csv("./california_house_dataset/housing.csv")
print(data_df)

print(data_df.isnull().sum()) # missing 207 null values

data_df = data_df.dropna()

print(data_df.info())


# check the correlation between the data 
# when performing correlation you need to have only features with numerical data
# dropping ocean_proximity
data_df = data_df.drop(["ocean_proximity"], axis=1)
correlation_matrix = data_df.corr()
sns.palplot(sns.color_palette("Blues",12))
# to plot using sns
plt.figure(figsize=(15,8))
print(correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, cmap="Blues")
plt.xticks(rotation=45, ha='right')
plt.title("Correlation matrix Heatmap of the Different data features")
# plt.tight_layout()
plt.show()


