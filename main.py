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

#elimino uno strato della lista degli ospiti
second_guest_list = []
for item in guest_list:
    x = (' '.join(item))
    second_guest_list.append(x)

#elimino uno strato della lista degli hotel
second_hotel_list = []
for item in hotel_list:
    x = (' '.join(item))
    second_hotel_list.append(x)

#stanze disponibili per hotel
n_rooms = pd.to_numeric(ds_hotel.rooms, errors = 'coerce')
rooms_list = [[i] for i in n_rooms]
number_rooms = []

#miglior metodo per convertire una lista di liste in una singola lista
for y in rooms_list:
    for x in y:
        number_rooms.append(x)

hotel_rooms = dict(zip(second_hotel_list, number_rooms))
print(hotel_rooms)


    

sys.exit()
