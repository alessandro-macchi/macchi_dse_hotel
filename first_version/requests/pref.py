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

#creo un indice che scorre, un dizionario vuoto in cui inserire di volta in volta gli ospiti
#sistemati, una lista per gli ospiti senza una stanza e associato agli ospiti un codice sequanziale
#per distinguerli più chiaramente
layer_2 = 0
alloc_pref = {}
unassigned_guest = []
guest_number = 0

#scorro la lista per ogni guest (layer_1) con gli hotel in ordine di preferenza (layer_2), verifico che
#l'hotel abbia ancora stanze disponibili, se così non fosse passa all'elemento successivo della
#lista del guest. Se nessuna stanza è disponibile allora si genera un errore (index out of list)
#che viene risolto con try/except e si ricomincia dal successivo. Il contatore (test) serve per
#uscire dal while quando il guest viene sistemato e viene resettato ogni volta che si passa al guest
#successivo
for layer_1 in pref_list:
    test = 0
    guest_number += 1
    layer_2 = 0
    while test == 0:
        try:
            if hotel_rooms.get(layer_1[layer_2]) > 0:
                alloc_pref[guest_number] = layer_1[layer_2]
                hotel_rooms[layer_1[layer_2]] -= 1
                test = 1
            else:
                layer_2 += 1
        except:
            unassigned_guest.append(guest_number)
            test = 1

#gli ospiti, in ordine di preferenza, vengono allocati in queste stanze
print(alloc_pref)
#le seguenti stanze sono rimaste vuote
print(hotel_rooms)
#i seguenti ospiti sono rimasti senza una stanza
print(unassigned_guest)

sys.exit()
