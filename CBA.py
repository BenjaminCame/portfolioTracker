import csv
import pandas as pd
from sqlalchemy import create_engine, URL

url_object = URL.create(
    "postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="Portfolio",
    port="5432"
)

df = pd.DataFrame(pd.read_csv('Transactions_2859397_01072016_08072024.csv'))
engine = create_engine(url_object)

with engine.connect() as conn:
    df.to_sql(name='portfolio', con=engine)




