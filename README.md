# 🏡 Multi-Linear Regression Model for USA Housing Prices

## 📚 Table of Contents
1. [Overview](#overview)
2. [Purpose](#purpose)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Example Prediction](#example-prediction)
7. [Contributing](#contributing)
8. [License](#license)
9. [Note](#note)

<a name="overview"></a>
## 🔍 Overview
This Python script demonstrates the creation of a multi-linear regression model using the `scikit-learn` library. It's designed to predict housing prices based on factors like average area income, house age, number of rooms and bedrooms, and area population. The script includes data loading, preprocessing, model training, evaluation, and saving the model for future predictions.

<a name="purpose"></a>
## 🎯 Purpose
The primary purpose of this script is to provide a practical application of multi-linear regression in predicting real estate prices, particularly useful for educational purposes in illustrating regression analysis in real-world scenarios.

<a name="requirements"></a>
## 🛠 Requirements
- Python 3.x
- Pandas (`pandas`): For data manipulation and analysis.
- NumPy (`numpy`): For numerical operations.
- Matplotlib (`matplotlib`): For plotting graphs.
- Seaborn (`seaborn`): For attractive statistical graphics.
- Scikit-Learn (`sklearn`): For machine learning algorithms and model evaluation.
- Joblib (`joblib`): For saving and loading the model.

<a name="installation"></a>
## 🚀 Installation
To install the required libraries, run:
```bash
pip install pandas numpy matplotlib seaborn sklearn joblib
```

## 🖥 Usage
- **Data Loading and Exploration**: Load the housing data using Pandas and explore it using descriptive statistics and pairplots.
- **Preprocessing**: Define features (X) and target (y), and split into training and test sets.
- **Model Training**: Train a linear regression model using Scikit-Learn's `LinearRegression`.
- **Model Evaluation**: Evaluate performance using MAE, MSE, and R2-score, and visualize results.
- **Model Persistence**: Save the trained model for future predictions.
- **Making Predictions**: Load the saved model to predict on new data.

<a name="example-prediction"></a>
## 🧮 Example Prediction
Provide input data in the format below to predict housing prices:
- 'Avg. Area Income': [income]
- 'Avg. Area House Age': [house_age]
- 'Avg. Area Number of Rooms': [num_rooms]
- 'Avg. Area Number of Bedrooms': [num_bedrooms]
- 'Area Population': [population]

<a name="contributing"></a>
## 👥 Contributing
Contributions to enhance the script are welcome. Please fork the repository and submit a pull request with your improvements.

<a name="license"></a>
## 📜 License
This project is open-sourced under the MIT License. See the [LICENSE](LICENSE.md) file for details.

<a name="note"></a>
## 📝 Note
- The script assumes that the data file `USA_Housing.csv` is present in the working directory.
- Adjust `test_size` and `random_state` in the train-test split according to your requirements.
- The visualization segment (pairplot) is commented out and can be enabled for a more in-depth analysis.

## 📊 Graphical representation of predictions vs actual values
![predictions_vs_actuals](https://github.com/pmoschos/multi_linear_regression/assets/133533759/31bcc475-c349-44dd-8447-5abfeabd33d7)

