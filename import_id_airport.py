import csv
import requests


csv_file_path1 = "data/airports.csv"
output_file_path2 = "data/airport_list.csv"

headers = {
    "accept": "application/json",
    "authorization": "iKRsQ8vdqgT903o2vH1rsejOeQ0F7YC9TvutH6Wk"
}

results = []


with open(csv_file_path1, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        airport_id = row["origin_airport_id"]

        response = requests.get(f'https://api-datalab.coderslab.com/api/v2/airport/{airport_id}', headers=headers)

        if response.status_code == 200:
            data = response.json()
            results.append(data)
        else:
            print(f"Błąd: {response.status_code} dla lotniska ID: {airport_id}")
            print(response.text)

with open(output_file_path2, mode="w", newline="") as output_file:

    fieldnames = results[0].keys()
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)


    csv_writer.writeheader()
    csv_writer.writerows(results)