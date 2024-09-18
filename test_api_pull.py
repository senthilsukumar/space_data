import requests
import pandas as pd

# Step 1: Make a request to the API
response = requests.get('https://fdo.rocketlaunch.live/json/launches/next/5')
data = response.json()  # Assuming the API returns JSON data

# Step 2: Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Save the DataFrame to an Excel file
print(df)
##df.to_excel('data.xlsx', index=False)