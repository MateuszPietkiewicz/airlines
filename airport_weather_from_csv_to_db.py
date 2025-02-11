import pandas as pd
import sqlalchemy

def load_raw_data(file_name):
    df = pd.read_csv(file_name)
    df.columns = df.columns.str.lower()
    return df

airport_df = load_raw_data("data/raw/airport_weather.csv")

airport_weather_expected_schema = [
       'station', 'name', 'date', 'awnd', 'pgtm', 'prcp', 'snow', 'snwd', 'tavg',
       'tmax', 'tmin', 'wdf2', 'wdf5', 'wsf2', 'wsf5', 'wt01', 'wt02',
       'wt03', 'wt04', 'wt05','wt06', 'wt07','wt08', 'wt09','wesd', 'wt10', 'psun', 'tsun', 'sn32',
       'sx32', 'tobs', 'wt11', 'wt18']
airport_df = airport_df[airport_weather_expected_schema]

print(airport_df.head())

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:naruto1@localhost:5432/loty')

airport_df.to_sql("airport_weather", con=engine, if_exists="append", index=False)