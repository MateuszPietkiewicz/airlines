import requests
import pandas as pd


df = pd.read_csv('data/airport_list.csv', header=None)
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
                        'CANCELLED': flight.get('CANCELLED', None),
                        'DISTANCE': flight.get('DISTANCE', None),
                        'YEAR': flight.get('YEAR', None),
                        'id_samolotu': id_sam,
                        'date': date
                    })
            else:
                print(f'Brak lotów dla samolotu {id_sam} w miesiącu {date}')
        except requests.exceptions.RequestException as e:
            print(f'Błąd podczas przetwarzania {id_sam} dla {date}: {e}')


df = pd.DataFrame(results)

# Zapisanie wyników do pliku CSV
df.to_csv('data/raw/flights.csv', index=False)

print("Dane zapisano do pliku 'flights.csv'.")