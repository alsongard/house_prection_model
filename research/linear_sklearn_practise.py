import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
data = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [10, 20, 30, 40, 50],
    "feature3": [2, 4, 6, 8, 10],        
    "target": [5, 9, 13, 17, 21]
}

data_df = pd.DataFrame(data)
print(data_df)

# get features
x_features  = data_df[["feature1", "feature2", "feature3"]]
y_target_field = data_df["target"]

linear_model = LinearRegression()
prediction_model = linear_model.fit(x_features, y_target_field)


print("Coefficients:", linear_model.coef_) # shows feature importance
print("Intercepts", linear_model.intercept_)
print("R^2 Score: ", linear_model.score(x_features, y_target_field))

"""
# to plot i need to plot for each feature against target
plt.scatter(data_df["feature1"], data_df["target"], color="red", label="Feature1 vs Target")
plt.scatter(data_df["feature2"], data_df["target"], color="blue", label="Feature2 vs Target")
plt.scatter(data_df["feature3"], data_df["target"], color="green", label="Feature3 vs Target")
# plt.scatter(x_features,y_target_field )
plt.xlabel("Feature Values")
plt.ylabel("Target Values")
plt.title("Scatter Plot features vs Target")
plt.legend()
plt.show()
"""


features_values = ["feature1", "feature2", "feature3"]
color_values = ["red", "blue", "green"]

for feature, single_color  in zip(features_values, color_values):
    # print(f"The feature is {feature} and color is : {color}")

    x = data_df[[feature]] # Indendent Variable (must be a 2D)
    y = data_df[["target"]]


    linear_model = LinearRegression()
    prediction_model = linear_model.fit(x, y)

    plt.scatter(x, y, color=single_color, label=f"{feature} vs Target")


    # get minimum value == x.min(), get max value x.max(), generate 100 values, reshape into 2d array reshape(-1,1)
    X_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)

    # get target values, this increases the number of values in the features and for the y_pred === target feature
    y_pred = linear_model.predict(X_range)

    plt.plot(X_range, y_pred, color=single_color, linestyle="--")


plt.xlabel("Feature Values")
plt.ylabel("Target Values")
plt.title("Scatter Plot with Regression Lines")
plt.legend()
plt.show()