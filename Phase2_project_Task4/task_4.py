import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load and preprocess the data
train_data = pd.read_csv('train_dataset.csv')
test_data = pd.read_csv('test_dataset.csv')

X_train = train_data[['x']]
y_train = train_data['y']

X_test = test_data[['x']]
y_test = test_data['y']

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test dataset
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) to evaluate the model
mse = mean_squared_error(y_test, y_pred)

# Print the predictions and MSE
print("Predictions:")
print(pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}))
print("\nMean Squared Error (MSE):", mse)
