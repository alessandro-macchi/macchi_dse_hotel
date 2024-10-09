import sys
import pandas as pd

# importo i datasets
ds_hotel = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/hotels.csv")
ds_pref = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/preferences.csv")
ds_guest = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/guests.csv")

#creo una lista di liste con all'interno gli ospiti e gli hotel
guest_list = [[i] for i in ds_guest.guest]
hotel_list = [[i] for i in ds_hotel.hotel]

#creo una funzione per trasformare una lista di liste in una lista singola
def list_cleaner(x, y):
    for j in x:
        for i in j:
            y.append(i)

second_guest_list = []
list_cleaner(guest_list, second_guest_list)

second_hotel_list = []
list_cleaner(hotel_list, second_hotel_list)

#stanze disponibili per hotel
n_rooms = pd.to_numeric(ds_hotel.rooms, errors = 'coerce')
rooms_list = [[i] for i in n_rooms]
number_rooms = []

list_cleaner(rooms_list, number_rooms)

#dizionario con hotel e numero di stanze per ciascuno
hotel_rooms = dict(zip(second_hotel_list, number_rooms))



# setto un'indice che scorre nella lista delle preferenze dei guest
i = 0
#una lista interna temporanea che si cancella di volta in volta
inner = []
#una lista esterna che raccoglie tutte le liste interne temporanee
outer = []

#scorro nella lista dei guest
for x in second_guest_list:
#finchè il guest della lista è uguale a quello del dataset delle preferenze, prendo l'hotel associato
#e lo unisco alla lista interna
    while x == ds_pref.guest[i]:
        inner.append(ds_pref.hotel[i])
        i += 1
    outer.append(inner)
    i = 0
    inner = []
print(outer)

#perchè funziona solo se resetto il contatore a zero e non se lo lascio libero???


sys.exit()
