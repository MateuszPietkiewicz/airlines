# import csv
# import requests
# import pandas as pd
#
# start_date = "2019-01"
# end_date = "2020-03"
#
# date_list = pd.date_range(start=start_date, end=end_date, freq="MS").strftime("%Y-%m").tolist()
#
# print(date_list)
#
#
# output_file_path = "data/raw/airport_weather.csv"
# headers = {
#     "accept": "application/json",
#     "authorization": "iKRsQ8vdqgT903o2vH1rsejOeQ0F7YC9TvutH6Wk"
# }
#
# results = []
# for dat in date_list:
#
#     response = requests.get(f'https://api-datalab.coderslab.com/api/v2/airportWeather?date={dat}', headers=headers)
#     data = response.json()
#     results.append(data)
#
# df = pd.DataFrame(results)
# df.to_csv(output_file_path, index=False)


import csv
import requests
import pandas as pd

# Parametry wejściowe
start_date = "2019-01"
end_date = "2020-03"
output_file_path = "data/raw/airport_weather.csv"

# Nagłówki dla API
headers = {
    "accept": "application/json",
    "authorization": "iKRsQ8vdqgT903o2vH1rsejOeQ0F7YC9TvutH6Wk"
}

# Generowanie listy dat (pierwsze dni miesięcy)
date_list = pd.date_range(start=start_date, end=end_date, freq="MS").strftime("%Y-%m").tolist()

# Lista do przechowywania danych
all_data = []

# Pobieranie danych
for date in date_list:
    print(f"Pobieranie danych dla: {date}")
    response = requests.get(
        f'https://api-datalab.coderslab.com/api/v2/airportWeather?date={date}',
        headers=headers
    )

    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            all_data.extend(data)
        else:
            print(f"Nieoczekiwany format danych dla {date}: {data}")
    else:
        print(f"Błąd pobierania danych dla {date}: {response.status_code}")

if all_data:
    df = pd.DataFrame(all_data)
    df.to_csv(output_file_path, index=False)
    print(f"Dane zapisane w {output_file_path}")
else:
    print("Brak danych do zapisania.")