# 17/12/24
# Esercizi su metodi e funzioni delle stringhe

# M I R I A M
# 0 1 2 3 4 5

nome = input("Come ti chiami? ")
pippo = input("scrivi qualcosa ")

# carattere di escape - \ (il carattere successivo ha un valore letterale e non funzionale)
print("le doppie virgolette che delimitano la stringa hanno una funzione sintattica")
print('le doppie virgolette possono essere sostituite dai singoli apici')
print("l'albero fa le mele")
# metodo furbo
print('Manzoni ha scritto i "Promessi "Sposi"')
# metodo serio
print("Manzoni ha scritto i \"Promessi Sposi\"")

#stampa numero caratteri (funzione)
print(len(nome))
# prima occorrenza di una substring (metodo)
print(nome.find("ia"))
# quando non è presente stampa -1 (metodo)
print(nome.find("M"))
# prima occorrenza di un singolo carattere (metodo)
print(nome.find("i"))
# ultima occorrenza di un singolo carattere (metodo)
print(nome.rfind("m"))
# prima occorrenza di un sa substring (metodo)
print(nome.rfind("am"))
# trasforma in MAIUSCOLO (metodo)
print(nome.upper())
# trasforma in minuscolo (metodo)
print(nome.lower())
# trasforma l'iniziale in maiuscolo
print(nome.capitalize())
print(nome.capitalize () + " " + pippo.capitalize())
# controlla se sono tutte lettere
print(nome.isalpha())
print(pippo.isdigit())
# controlla substring iniziale
print(nome.startswith("Mi"))
# controlla substring finale
print(nome.endswith("am"))
# conta il numero di occorrenze di una substring
print(nome.count("i"))
# conta il numero di spazi nella stringa
print(pippo.count("  "))
# sostituisce una substring con un'altra
print(nome.replace("i", "o"))
print(pippo.replace(" ", "-"))
# rimuove gli spazi all'inizio e alla fine della stringa
print(nome)
print(nome.strip())
# rimuove una substring dall'inizio e dalla fine della stringa
print(nome)
print(nome.strip("m"))

# visualizza tutte le informazioni sui metodi delle stringhe
print(help(str))