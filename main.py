import pandas as pd
from datetime import datetime

STOCK_DATA = "stock_data_cleaned.csv"
FACTOR_DATA = "stock_data_cleaned.csv"

stock_df = pd.read_csv(STOCK_DATA)
factor_df = pd.read_csv(FACTOR_DATA)

returns = stock_df.pct_change(fill_method=None)

start_date = datetime(day=1, month=1, year=2009)
final_date = datetime(day=31, month=12, year=2022)
formation_window_period = pd.Period(freq="M")

window_idx = 0
windows = []

while True:
    formation_start = start_date + formation_window_period