import pandas as pd

data_df = pd.read_csv("./data/train.csv")
print(data_df)


# get necessary columns
print(data_df.info())
original_data_df = data_df[data_df["MSSubClass", "MSZoning"]]