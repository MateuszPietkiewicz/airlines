import requests
import pandas as pd


df = pd.read_csv('data/raw/airport_list.csv', header=None)
id_samolotow = df[0][1:].tolist()
print(id_samolotow)

start_date = "2019-01"
end_date = "2020-03"

date_list = pd.date_range(start=start_date, end=end_date, freq="MS").strftime("%Y-%m").tolist()
print(date_list)

headers = {
    "accept": "application/json",
    "authorization": "iKRsQ8vdqgT903o2vH1rsejOeQ0F7YC9TvutH6Wk"
}
results = []

# Iteracja przez listy
for id_sam in id_samolotow:
    for date in date_list:
        try:
            # Wykonanie zapytania do API
            response = requests.get(
                f'https://api-datalab.coderslab.com/api/v2/flight?airportId={id_sam}&date={date}',
                headers=headers
            )
            response.raise_for_status()  # Wyrzuć wyjątek, jeśli status nie jest 200

            # Pobranie odpowiedzi w formacie JSON
            data = response.json()

            # Sprawdzenie, czy odpowiedź zawiera dane o lotach
            if len(data) > 0:  # Jeśli odpowiedź zawiera dane
                for flight in data:
                    results.append({
                        'MONTH': flight.get('MONTH', None),
                        'DAY_OF_MONTH': flight.get('DAY_OF_MONTH', None),
                        'DAY_OF_WEEK': flight.get('DAY_OF_WEEK', None),
                        'OP_UNIQUE_CARRIER': flight.get('OP_UNIQUE_CARRIER', None),
                        'TAIL_NUM': flight.get('TAIL_NUM', None),
                        'OP_CARRIER_FL_NUM': flight.get('OP_CARRIER_FL_NUM', None),
                        'ORIGIN_AIRPORT_ID': flight.get('ORIGIN_AIRPORT_ID', None),
                        'DEST_AIRPORT_ID': flight.get('DEST_AIRPORT_ID', None),
                        "CRS_DEP_TIME": flight.get("CRS_DEP_TIME", None),
                        "DEP_TIME": flight.get("DEP_TIME", None),
                        "DEP_DELAY_NEW": flight.get("DEP_DELAY_NEW", None),
                        "DEP_TIME_BLK": flight.get("DEP_TIME_BLK", "string"),
                        "CRS_ARR_TIME": flight.get("CRS_ARR_TIME", None),
                        "ARR_TIME": flight.get("ARR_TIME", None),
                        "ARR_DELAY_NEW": flight.get("ARR_DELAY_NEW", None),
                        "ARR_TIME_BLK": flight.get("ARR_TIME_BLK", "string"),
                        'CANCELLED': flight.get('CANCELLED', None),
                        "CRS_ELAPSED_TIME": flight.get("CRS_ELAPSED_TIME", None),
                        "ACTUAL_ELAPSED_TIME": flight.get("ACTUAL_ELAPSED_TIME", None),
                        'DISTANCE': flight.get('DISTANCE', None),
                        "DISTANCE_GROUP": flight.get("DISTANCE_GROUP", None),
                        'YEAR': flight.get('YEAR', None),
                        "CARRIER_DELAY": flight.get("CARRIER_DELAY", None),
                        "WEATHER_DELAY": flight.get("WEATHER_DELAY", None),
                        "NAS_DELAY": flight.get("NAS_DELAY", None),
                        "SECURITY_DELAY": flight.get("SECURITY_DELAY", None),
                        "LATE_AIRCRAFT_DELAY": flight.get("LATE_AIRCRAFT_DELAY", None)
                    })
            else:
                print(f'Brak lotów dla samolotu {id_sam} w miesiącu {date}')
        except requests.exceptions.RequestException as e:
            print(f'Błąd podczas przetwarzania {id_sam} dla {date}: {e}')




df = pd.DataFrame(results)

# Zapisanie wyników do pliku CSV
df.to_csv('data/raw/flights.csv', index=False)

print("Dane zapisano do pliku 'flights.csv'.")