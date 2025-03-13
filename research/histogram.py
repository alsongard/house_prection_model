import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
            'Age': [25, 30, 22, 35, 40, 28, 32, 31, 36, 39],
            'Salary': [4000, 5000, 3000, 7000, 8000, 4500, 6000, 5800, 7200, 4900]
        }

data_df = pd.DataFrame(data)

print(data_df["Age"].value_counts())

data_df.hist()
# plt.show()

data_df.hist(column=['Age', 'Salary'], bins=5, figsize=(10,5), color='orange')
# plt.show()


## checking the skew of the data
"""
positive skew: right tail(right skewed)
negative skew: left tail(left skewed)
"""

print(data_df["Age"].skew())
print(data_df["Salary"].skew())



## visualizing the skewness of the data using seaborn
plt.figure(figsize=(8,5))
sns.kdeplot(data_df["Age"], fill=True, color='skyblue')
plt.axvline(data_df["Age"].mean(), color="red", linestyle="dashed", label="mean")
plt.axvline(data_df["Age"].median(), color="green", linestyle="dashed", label="median")
plt.legend()
plt.title("Age Distribution vs skewness")
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()

# check if mean  and median
"""
Mean > median === Positive skew
Mean <  Median = Negative skew
Mean === Medain == Normal Distribution
"""

print(f"Mean of Age is {data_df["Age"].mean()}")
print(f"Medain of Age is {data_df["Age"].median()}")