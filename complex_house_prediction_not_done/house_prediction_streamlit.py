import pandas as pd
import streamlit as st
data_df = pd.read_csv("./data/train.csv")
# data_df



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

st.write(trial_data_df)

# perform cleaning of data
st.write(trial_data_df.isnull().sum()) # no null values


# checking maximum and minimum SalePrice value
st.text(f"The highest SalePrice value is {trial_data_df["SalePrice"].max()}")
st.text(f"The lowest SalePrice value is {trial_data_df["SalePrice"].min()}")


# retrieve the rows of the maximum and minimum SalePrice
maximum_salePrice_value_row = trial_data_df.loc[trial_data_df["SalePrice"].idxmax()]
minimum_salePrice_value_row = trial_data_df.loc[trial_data_df["SalePrice"].idxmin()]

st.write("retrieve the rows of the maximum and minimum SalePrice")
st.write(maximum_salePrice_value_row)
st.write(minimum_salePrice_value_row)