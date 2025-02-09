import requests
import pandas as pd

output_file_path = "data/raw/aircraft.csv"
headers = {
    "accept": "application/json",
    "authorization": "iKRsQ8vdqgT903o2vH1rsejOeQ0F7YC9TvutH6Wk"
}

response = requests.get(f'https://api-datalab.coderslab.com/api/v2/aircraft', headers=headers)
data = response.json()


df = pd.DataFrame(data)
df.to_csv(output_file_path, index=False)