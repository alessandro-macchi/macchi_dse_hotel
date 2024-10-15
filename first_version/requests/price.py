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
risultato = {}
unassigned_hotel = []

#dizionario con gli ospiti allocati
for item in ordered_hotel_list:
    guest_number = 0
    for i in pref_list:
        guest_number += 1
        for j in i:
            if guest_number not in risultato.keys():
                if not hotel_rooms[item] == 0:
                    if item == j:
                        risultato[guest_number] = item
                        hotel_rooms[item] -= 1

#stampando la variabile risultato si trovano le persone con gli hotel associati

#lista degli hotel non assegnati
for t in ordered_hotel_list:
    if hotel_rooms[t] > 0:
        unassigned_hotel.append(t)


#numero stanze non assegnate
fin = 0
for y in unassigned_hotel:
    z = hotel_rooms[y]
    fin += z
    
#notiamo che il numero di stanze che eccedono i guests (617) e il numero di guests non assegnati (75)
#coincide con il numero di stanze avanzate in questa situazione (692)

#questo ciclo for va messo prima che le hotel_rooms vengano scalate per assegnarle
tot = 0
for i in hotel_rooms:
    a = hotel_rooms[i]
    tot += a

verifica = (len(second_guest_list) - len(risultato)) + (tot - len(second_guest_list))

sys.exit()
