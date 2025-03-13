when working with YearBuilt and SalePrice the correlationship between the values is 0.5228973328794969. Values near 0 mean they don't have any relationship




types of regression we have:
- simple linear regression : single independent feature and the target feature
- multiple linear regression : multiple independent features and target feature
- polynomial linear regression: lineaar regression line is a curve


applications:
economic growth of a country
housing sales
product sales
score predictions


## understanding linear regression:



### intresting features
totalRooms: total number of room swithin a block
population: total number of people residing  in a bloack

target_feature = 


📌 Importance of Normal Distribution in Linear Regression

In Linear Regression, having normally distributed features is beneficial because:  
- Better Model Performance – Linear regression assumes a linear relationship between features and target variables. If features are normally distributed, the model can learn patterns more effectively.  
- Reliable Statistical Tests – Many statistical tests (e.g., t-tests, p-values, and confidence intervals) assume normality to produce meaningful results.
- Reduced Bias – Normally distributed features prevent overfitting or biased predictions.
- More Accurate Predictions – Helps in meeting the assumption of homoscedasticity (equal variance of residuals).

📌 What If Features Are Not Normally Distributed?

If features are skewed (not normally distributed), it can lead to:
- Poor Model Fit – The linear regression model might not generalize well.
- Heteroscedasticity – Unequal variance in residuals, leading to unreliable predictions.
- Non-linear Relationships Ignored – Skewed features may indicate a non-linear relationship, which Linear Regression cannot capture.
- Outliers Influence Results – If skewness is high, outliers may significantly impact model coefficients.


To handle skewness in data features do the following:
1. For positive skewness ``skew() > 1``  

- Log Transformation (for right-skewed data)
```
import numpy as np
data_df["feature"] = np.log1p(data_df["feature"])  # log1p prevents log(0) error
```

- Square Root Transformation (reduces right skew)
```
data_df["feature"] = np.sqrt(data_df["feature"])
```

