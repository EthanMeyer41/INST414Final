import yfinance as yf
import requests
import pandas as pd

# Function to get data from Yahoo Finance API
def get_yahoo_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date, interval='1wk')
    return stock_data


def get_athena_data(symbol):
    athena_url = f'https://api.aletheiaapi.com/StockData?symbol={symbol}'
    response = requests.get(athena_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")
        return None

#30 at a time
stock_symbols = ['MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ATVI', 'ADBE', 'AAP', 'AES', 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALXN', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP']



start_date = '2012-01-01'
end_date = '2022-01-01'


df = pd.DataFrame()
for symbol in stock_symbols:
    yahoo_data = get_yahoo_data(symbol, start_date, end_date)
    athena_data = get_athena_data(symbol)
    
    if yahoo_data is not None and athena_data is not None:
        # Combine the data from both APIs
        merged_data = pd.concat([yahoo_data, pd.DataFrame(athena_data)], axis=1)
        df = pd.concat([df, merged_data])

df.to_csv('sss_stock_data.csv')

print("Dataset  completed.")
