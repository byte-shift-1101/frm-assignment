
## Descrbing the data
The start and end date of the observations is Jan 1, 2009 to Dec 31, 2022
[[market_Factor_risk_Free.csv]] contains market excess return percentage and the risk free rate for that day
[[Stocks_data.csv]] contains data about several stocks listed in the stock exchange, more spcifically their closing prices on the respective dates
- Some of the stocks weren't present at the start of 2009 and even much later. Hence some of their values are null (which are the values that come first in chronological order). These columns include: `['SBILIFE IS Equity', 'NEST IS Equity', 'LTIM IS Equity', 'COAL IS Equity', 'HDFCLIFE IS Equity']`

Both of the files don't have the same number of rows signifying that some of the dates are missing (in [[market_Factor_risk_Free.csv]]). As the assignment states, we will be not using any dates that aren't present in both the files.

