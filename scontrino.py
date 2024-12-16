#16/12/24
# Programma che visualizza uno scontrino relativo all'acquisto di un prodotto con dati:
# nome del prodotto
# quantità desiderata
# prezzo

item = input("Che cosa vuoi comprare? ")
price = input("Quanto costa? ")
qnt = input("Quanti ne compri? ")

#metodo1 - calcolare il risultato e metterlo in una variabile
tot = round(int(qnt) * float(price), 2)
print("Per comprare " + qnt + " di " + item + " devi pagare " +str(round(tot, 2)) + "€")

#metodo2 - sfrutto le f-strings
print(F"Per comprare {qnt} di {item} devi pagare {round(int(qnt) * float(price), 2)}€")
