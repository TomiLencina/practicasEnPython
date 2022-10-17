from forex_python.converter import CurrencyRates

c = CurrencyRates()

monto = int(input("Ingrese el monto a convertir: "))
de_moneda = input("De la moneda: ").upper()
a_moneda = input("Moneda a la que quiere hacer la conversion: ").upper()

print(de_moneda, "A", a_moneda, monto)
result = c.convert(de_moneda, a_moneda, monto)
print (result)
