import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Prepare the Data
# House sizes in square feet (Features)
# We reshape it because the model expects a 2D array
X = np.array([[600], [800], [1000], [1200], [1500], [2000]])

# House prices in thousands of dollars (Labels)
y = np.array([150, 180, 220, 250, 310, 400])

# 2. Initialize the AI Model
# We are using a Simple Linear Regression model
model = LinearRegression()

# 3. Train the Model (The "Learning" phase)
# The AI looks at X and y to find the mathematical relationship
model.fit(X, y)

# 4. Make a Prediction
# Let's ask the AI: "How much should a 1,700 sq ft house cost?"
new_house_size = np.array([[1700]])
predicted_price = model.predict(new_house_size)

print(f"For a house of 1,700 sq ft, the AI predicts a price of: ${predicted_price[0]:.2f}k")
