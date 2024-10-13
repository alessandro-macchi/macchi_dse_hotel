#prima idea
import sys
import random
import pandas as pd

# importo i datasets
ds_hotel = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/hotels.csv")
ds_pref = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/preferences.csv")
ds_guest = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/guests.csv")

#creo una lista di liste con all'interno gli ospiti e gli hotel
guest_list = [[i] for i in ds_guest.guest]
hotel_list = [[i] for i in ds_hotel.hotel]

#creo una funzione per trasformare una lista di liste in una lista singola
def list_cleaner(lista_da_pulire, lista_pulita):
    for j in lista_da_pulire:
        for item in j:
            lista_pulita.append(item)

second_guest_list = []
list_cleaner(guest_list, second_guest_list)

second_hotel_list = []
list_cleaner(hotel_list, second_hotel_list)

#stanze disponibili per hotel
n_rooms = pd.to_numeric(ds_hotel.rooms, errors = 'coerce')
rooms_list = [[i] for i in n_rooms]
number_rooms = []

#pulisco la lista
list_cleaner(rooms_list, number_rooms)

#dizionario con hotel e numero di stanze per ciascuno
hotel_rooms = dict(zip(second_hotel_list, number_rooms))

#creo una lista pulita con il prezzo per hotel
price_list = [[i] for i in ds_hotel.price]
cleaned_price = []
list_cleaner(price_list, cleaned_price)

#creo lista con numero stanze e prezzo di ogni hotel
price_rooms = []
j = 0
for i in cleaned_price:
    price_rooms.append(i)
    price_rooms.append(number_rooms[j])
    j += 1

#dizionario con hotel e prezzo associato
hotel_price = dict(zip(second_hotel_list, cleaned_price))

#riordino il dizionario
ordered_hotel_price = {key: val for key, val in sorted(hotel_price.items(),
                        key = lambda ele: ele[1])}


# setto un'indice che scorre liberamente nella lista delle preferenze dei guest
i = 0
#una lista interna temporanea che si cancella di volta in volta
temporary_list = []
#una lista esterna che raccoglie tutte le liste interne temporanee
pref_list = []

#scorro nella lista dei guest
for x in second_guest_list:
#finchè il guest della lista è uguale a quello del dataset delle preferenze, prendo l'hotel 
#associato e lo unisco alla lista interna
    try:
        while x == ds_pref.guest[i]:
            temporary_list.append(ds_pref.hotel[i])
            i += 1
    except:
        break
    pref_list.append(temporary_list)
    temporary_list = []

#creo un dizionario con gli hotel in ordine di prezzo, ma associati al valore delle stanze
y = 0
ordered_hotel_list = []
for j in ordered_hotel_price: 
    ordered_hotel_list.append(list(ordered_hotel_price.items())[y][0])
    y += 1

#setto gli indici
w = 0
q = 0
risultato = {}
unassigned_hotel = []

#continua all'infinito, bisogna occupare tutte le stanze dell'hotel
for item in ordered_hotel_list:
    guest_number = 1
    
    q = 0
    test = 0
    while test == 0:
        try:
            if item == pref_list[w][q]:
                risultato[item] = guest_number
                hotel_rooms[item] -= 1
                w += 1
                guest_number += 1
                if hotel_rooms[item] == 0:
                    test = 1
            else:
                q += 1
        except:
            w += 1
            guest_number += 1

print(risultato)

#crei un dizionario con values il numero di stanze e il prezzo e riordini per il secondo 
#se non si può fare si crea un dizionario con i prezzi, si riordina secondo questi e poi
#sostituisci il prezzo con il numero di stanze (occhio che cambia l'ordine degli hotel), ma nel
#caso si potrebbe risolvere con due dizionari che vengono fatti comunicare


sys.exit()
