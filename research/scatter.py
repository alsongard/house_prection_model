import matplotlib.pyplot as plt
from scipy import stats


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]



# get important key values from linregression()

slope, intercept, r, p, std_err  = stats.linregress(x, y)  

print(f"The relationship for the x and y variables is : ${r}") # $-1.7512877115526118
print(f"Value for slope is : \n {slope}")

def myFunc(x):
    return slope * x + intercept

myModel = list(map(myFunc, x))
print(myModel)


plt.scatter(x, y)
plt.plot(x, myModel)
plt.show()