import finnhub
import pandas as pd

tickers = ["META", "AMZN", "AMGN", "BMY", "GOOGL", "BA", "CMCSA", "MO", "LMT", "FDX", "ORCL", "CHTR", "GM", "GD", "CVX", "TMUS", "VZ", "MSFT", "JNJ", "T", "HON", "MRK", "GILD", "NEE", "AAPL", "SNY", "V", "CI", "QCOM", "PRU", "WMT", "NOC", "INTU", "INTC", "DELL", "TM", "CVS", "UNH", "OXY", "XOM", "DAL", "AFL", "ABBV", "UPS", "AEP", "AAL", "ELV", "BUD", "DUK", "TXT", "WFC", "MS", "HII", "DVA", "IHRT", "ABT", "CEG", "VRTX", "COIN", "C", "FOX", "BAC", "PFE", "TAK", "LUMN", "IBM", "HQY", "CNC", "X", "JPM", "CAT", "MA", "GRAL", "NBIX", "COF", "PEP", "CARR", "NVO", "GE", "UAL", "CPNG", "DISH", "ARDX", "HD", "MCD", "BIIB", "CSCO", "BLK", "CSX", "ACI", "HUM", "ALLY", "EBAY", "UBER", "KO", "UNP", "AZN", "MCK", "HPQ", "HIG", "EMN", "MTCH", "ACN", "BABA", "ALL", "MU", "GS", "COP", "AMAT", "COR", "HPE", "AEE", "THC", "TSM", "ETR", "ALK", "ALB", "IDCC", "ATGE", "NDAQ", "SEM", "LYV", "MPC", "SVF", "EBS", "MSI", "EXC"]

finnhub_client = finnhub.Client(api_key="ct16su1r01qkcukbnh90ct16su1r01qkcukbnh9g")

for i in range(len(tickers)):
    finn = finnhub_client.stock_lobbying(f"{tickers[i]}", "1990-01-01", "2024-11-24")
    expenses = []
    income = []
    year = []
    period = []
    df = pd.DataFrame(columns=['expenses','income', 'year','period']) 
    for j in range(len(finn['data'])):
        expenses.append(finn['data'][j]['expenses'])
        income.append(finn['data'][j]['income'])
        year.append(finn['data'][j]['year'])
        period.append(finn['data'][j]['period'])
    df['expenses'] = expenses
    df['income'] = income
    df['year'] = year
    df['period'] = period
    clean = df.groupby(['year', 'period'], as_index=False).sum()
    clean.to_csv(f"{tickers[i]}.csv")
