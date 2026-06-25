import pandas as pd
import kagglehub
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
 
# Download Dataset 
path = kagglehub.dataset_download(
    "zafarali27/house-price-prediction-dataset"
)

print("Dataset Path:", path)
print("Files:", os.listdir(path))

# Load CSV
csv_file = os.path.join(path, os.listdir(path)[0])
df = pd.read_csv(csv_file)
print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())
 
# Select Features and Target 
X = df[["Area", "Bedrooms", "Bathrooms"]]
y = df["Price"]
 
# Split Dataset 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
 
# Train Model 
model = LinearRegression()
model.fit(X_train, y_train)
 
# Evaluate Model 
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nModel Performance")
print("Mean Absolute Error:", mae)
print("R² Score:", r2)
 
# Future Prediction 
future_house = pd.DataFrame({
    "Area": [2000],
    "Bedrooms": [3],
    "Bathrooms": [2]
})

predicted_price = model.predict(future_house)
print("\nFuture House Prediction")
print("Area: 2000 sq ft")
print("Bedrooms: 3")
print("Bathrooms: 2")
print(f"Predicted Price: ${predicted_price[0]:,.2f}")
print(f"Approximate Error Margin: ±${mae:,.2f}")