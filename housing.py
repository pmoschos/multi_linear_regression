import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score
from joblib import dump, load

# Loading and checking our data
USAHousing = pd.read_csv('USA_Housing.csv')

# Print the head of our file
# print(USAHousing.head(10))

# print some information of our data
# print(USAHousing.info())

# print some description of our data
print(USAHousing.describe())

# print the names of the columns
print(USAHousing.columns)

# Create pairplots to check our data
# sns.pairplot(USAHousing)
# plt.show()

# Train Linear Regression Model
X = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 
                'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 
                'Area Population']]
y = USAHousing['Price']

# Split my data to train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Create my model
linear_model = LinearRegression()

# train my model
linear_model.fit(X_train, y_train)

# model evaluation

# print intercept
print(linear_model.intercept_)

# print coeffs
coeff_df = pd.DataFrame(linear_model.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

# make predictions
predictions = linear_model.predict(X_test)
plt.scatter(y_test, predictions, color = 'red', label = "Predictions")
plt.scatter(y_test, y_test, color = 'blue', label = 'Actual Values')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.show()

print()
print("MAE:", metrics.mean_absolute_error(y_test, predictions))
print("MSE:", metrics.mean_squared_error(y_test, predictions))
print("R2-score", r2_score(y_test, predictions))

# Save the model for future use
dump(linear_model, 'linear_model.joblib')