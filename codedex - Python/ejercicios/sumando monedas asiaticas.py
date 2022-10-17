#Calculando el total de dinero en USD

mensaje = print("Convertidor de dinero extranjero a USD")

yuan_chino = int(input("Ingrese la cantidad de su dinero chino: "))
yen_Japones = int(input("Ingrese la cantidad de su dinero japones: "))
won_surKorea = int(input("Ingrese la cantidad de su dinero SurKoreano: "))

usd_yuan = int(yuan_chino * 0.147978)
usd_yen = int(yen_Japones * 0.00747030)
usd_won = int(won_surKorea * 0.000764302)

total = int(usd_won + usd_yen + usd_yuan)

print(total)