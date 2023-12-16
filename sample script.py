import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('sss_stock_data.csv', index_col=0)


columns_of_interest = ['Open', 'High', 'Low', 'Close', 'Volume', 'Moving Average', 'Resistance', 'RSI', 'P/E', 'P/B', 'MACD']
selected_data = df[columns_of_interest]


selected_data = selected_data.dropna()


X = selected_data.drop('Close', axis=1)
y = selected_data['Close']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


coefficients = pd.Series(model.coef_, index=X.columns)
intercept = model.intercept_

# Print the results
print("Selected Columns for Analysis:")
print(selected_data.head())
print("\nCoefficients:")
print(coefficients)
print("\nIntercept:")
print(intercept)
print("\nModel Performance:")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
