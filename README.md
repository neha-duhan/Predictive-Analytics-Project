# House Price Prediction Using Multiple Linear Regression

## Project Overview
This project predicts house prices using historical housing data and Multiple Linear Regression.

## Tools Used
- Python
- Pandas
- Scikit-Learn
- KaggleHub

## Features (X)
- Area
- Bedrooms
- Bathrooms

## Target Variable (Y)
- Price

## Steps Performed
1. Loaded housing dataset.
2. Selected features and target variable.
3. Split data into training and testing sets.
4. Trained a Multiple Linear Regression model.
5. Evaluated model performance using MAE and R² Score.
6. Predicted the price of a future house.

## Future Prediction
- Area: 2000 sq ft
- Bedrooms: 3
- Bathrooms: 2
- Predicted Price: $541,534.12

## Business Report

The objective of this project was to predict house prices using historical housing data.

A Multiple Linear Regression model was trained using information such as:

* House Area
* Number of Bedrooms
* Number of Bathrooms

The model learned patterns from past house sales and used those patterns to estimate the price of a future property.

To evaluate the model, we measured:

* **Mean Absolute Error (MAE):** Shows the average difference between predicted and actual house prices.
* **R² Score:** Indicates how well the model explains variations in house prices.

A sample prediction was performed for a house with:

* Area: 2000 sq ft
* Bedrooms: 3
* Bathrooms: 2

The model generated an estimated selling price along with an approximate error margin.

### Conclusion

The results demonstrate that machine learning can be used to forecast house prices based on property characteristics. Such models can assist real estate companies, buyers, and sellers in making informed pricing decisions using historical data rather than guesswork.
