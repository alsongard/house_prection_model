import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



data_df = pd.read_csv("./data/train.csv")
print(data_df)


# get necessary columns
# print(data_df.info())

selected_features = [
    "MSSubClass", "MSZoning", "LotArea", "Neighborhood", "OverallQual", 
    "OverallCond", "YearBuilt", "YearRemodAdd", "GrLivArea", "TotalBsmtSF", 
    "1stFlrSF", "2ndFlrSF", "FullBath", "HalfBath", "BedroomAbvGr", 
    "TotRmsAbvGrd", "Fireplaces", "GarageCars", "GarageArea", "WoodDeckSF", 
    "OpenPorchSF", "PoolArea", "SaleCondition", "SalePrice"
]
original_data_df = data_df[selected_features]

# print(original_data_df)

# checking on room, utilities, lotArea, YearBuilt
trial_data_df  = data_df[["LotArea", "YearBuilt", "YearRemodAdd", "PoolArea", "SalePrice"]]

print(trial_data_df)


#  get the row with the maximum value and minimum SalePrice value
maximum_salePrice_value_row = trial_data_df.loc[trial_data_df["SalePrice"].idxmax()]
minimum_salePrice_value_row = trial_data_df.loc[trial_data_df["SalePrice"].idxmin()]

print(maximum_salePrice_value_row)
print(minimum_salePrice_value_row)



# perform cleaning of data
# print(trial_data_df.isnull().sum())  # no null values


# checking which columns/features have a correlation
# r == 1 || r ==  -1 shows good correlation, r == 0 (poor correlation)
year_built_values = trial_data_df["YearBuilt"]
sale_price_values = trial_data_df["SalePrice"]


print(year_built_values.shape)
print(sale_price_values.shape)

print("year_built_values")
print(year_built_values)


# slope, intercept, r, p, std_err = stats.linregress(year_built_values, sale_price_values)

# print(f"Check the correlation of the YearBuilt and SalePrice is : {r}")  # poor



# slope, intercept, r, p, std_err = stats.linregress(trial_data_df["LotArea"], trial_data_df["SalePrice"])
# print(f"Check the correlation of the LotArea and SalePrice is : {r}")  # poor 




# def myFunc(x):
#     return slope * x + intercept

# myModel = list(map(myFunc, year_built_values))
# print(myModel)
# plt.scatter(trial_data_df["YearBuilt"], trial_data_df["SalePrice"])
# plt.plot(x_values, myModel)
# plt.show()

feature_values = ["LotArea", "YearBuilt"]
color_values = ["red", "green", "blue"]
for feature, single_color in zip(feature_values, color_values):
    x = data_df[[feature]]
    y =  data_df[["SalePrice"]]

    linear_model = LinearRegression()
    prediction_model = linear_model.fit(x, y)

    plt.scatter(x, y, color=single_color, label=f"{feature} vs Target")

plt.xlabel("Feature Values")
plt.ylabel("Target Values")
plt.title("Scatter Plot with Regression Lines")
plt.legend()
plt.show()