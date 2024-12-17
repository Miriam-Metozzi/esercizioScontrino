#16/12/24

# Programma che visualizza uno scontrino relativo
# all'acquisto di un prodotto con dati:
# nome del prodotto
# quantità desiderata
# prezzo

item = input("Che cosa vuoi comprare? ")
price = input("Quanto costa? ")
qnt = input("Quanti ne compri? ")

#metodo 1 - calcolare il risultato e metterlo in una variabile
tot = round(int(qnt) * float(price), 2)
# print(type(tot))
# print(type(tot))

print("Per comprare " + qnt + " di " + item + " devi pagare " +str(tot) + "€")

#metodo 2 - sfrutto le f-strings
print(F"Per comprare {qnt} di {item} devi pagare {round(int(qnt) * float(price), 2)}€")

# metodo 3 - fare le conversioni all'inizio
item1 = input("Che cosa vuoi comprare? ")
price1 = float(input("Quanto costa? "))
qnt1 = int(input("Quanti ne compri? "))
print(F"Per comprare {qnt} di {item} devi pagare {round(qnt1 * price1, 2)}€")
