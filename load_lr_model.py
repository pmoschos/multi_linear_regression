from joblib import load
import numpy as np

# Load my 'saved' linear model
loaded_linear_model = load('linear_model.joblib')

# 'Avg. Area Income':  80000
# 'Avg. Area House Age': 5
# 'Avg. Area Number of Rooms': 7
# 'Avg. Area Number of Bedrooms': 4
# 'Area Population': 25000

new_data = [80000, 7, 7, 4, 25000]

# 2-dimentional array with 1 row and 'as many columns as we need'
reshape_data = np.array(new_data).reshape(1, -1)

# Make my prediction
price_predicted = loaded_linear_model.predict(reshape_data)

# Display the prediced price (result)
print(f"Predicted house price: ${price_predicted[0]:,.2f}")
