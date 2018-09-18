from forex_python.converter import CurrencyRates, Decimal
c = CurrencyRates()
print(c.convert('USD', 'INR', Decimal('10.45')))
