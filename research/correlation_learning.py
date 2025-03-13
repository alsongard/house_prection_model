import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
correlation is used to check how the features of a column relate to each other. Checks on numerial columns
it returns a correlation matrix with the following values:
-1 :  Negativley related(as once incrs, the other decreases)
0 : no correlation
1 :  positive correlation: (as one icnrs the other incrs)
"""


# Sample Data
employee_data = {
    "Age": [25, 32, 47, 19, 45],
    "Salary": [3000, 4500, 7000, 2000, 6500],
    "Experience": [2, 5, 10, 1, 9]
}
data_df = pd.DataFrame(employee_data)

# check correlation
print(data_df.corr())


# to visualize the correlation use seaborn heatmap
correlation_matrix = data_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()