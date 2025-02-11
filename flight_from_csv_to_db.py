import pandas as pd
import sqlalchemy

def load_raw_data(file_name):
    df = pd.read_csv(file_name)
    df.columns = df.columns.str.lower()
    return df

airport_df = load_raw_data("data/raw/flights.csv")




print(airport_df.head())

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:naruto1@localhost:5432/loty')

airport_df.to_sql("flight", con=engine, if_exists="append", index=False)