from psycopg2 import connect
import pandas as pd
import sqlalchemy


cnx = connect(user="postgres",
              password="naruto1",
              host="localhost",
              database="loty")
cursor = cnx.cursor()
# sql="SELECT * FROM aircraft"
# cursor.execute(sql)

# airport_df = pd.read_csv("data/raw/airport_list.csv")


def load_raw_data(file_name):
    df = pd.read_csv(file_name)
    df.columns = df.columns.str.lower()
    return df
airport_df = load_raw_data("data/raw/airport_list.csv")

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:naruto1@localhost:5432/loty')

airport_df.to_sql("airport_list", con=engine, if_exists="append", index=False)
cnx.close()