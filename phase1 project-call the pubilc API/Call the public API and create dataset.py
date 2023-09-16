import requests
import pandas as pd

# Call the API
url = 'https://data.binance.com/api/v3/ticker/24hr'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('binance_data.csv', index=False)
    print('Dataset saved as binance_data.csv')
else:
    print('Error fetching data. Status code:', response.status_code)
