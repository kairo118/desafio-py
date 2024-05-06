import pandas as pd

data = {
'year': [1949, 1949, 1949, 1949, 1949],
'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
'passengers': [112, 118, 132, 129, 121]
}

flights = pd.DataFrame(data)

monthly_passengers = flights.groupby('month').passengers.sum()

max_month = monthly_passengers.idxmax()
max_passengers = monthly_passengers.max()

print(f'O mês com o maior número de passageiros é {max_month} com um total de {max_passengers} passageiros.')

