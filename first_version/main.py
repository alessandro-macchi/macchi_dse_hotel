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

#creo una lista pulita con il prezzo per hotel
price_list = [[i] for i in ds_hotel.price]
cleaned_price = []
list_cleaner(price_list, cleaned_price)

#provare a creare un dizionario con tutte le info per ogni hotel e prenderle quando necessario
#(tipo per scalare il numero di stanze di volta in volta)
#cambiare ordine!!
Hotel = {}
temp = {}
prova = 1
w = 0
for i in second_hotel_list, number_rooms, cleaned_price:
    temp['name'] = second_hotel_list[w]
    temp['rooms'] = number_rooms[w]
    temp['price'] = cleaned_price[w]
    Hotel[prova] = temp
    prova += 1
    w += 1
    temp = {}
    
    
Hotel['name'] = second_hotel_list
Hotel['rooms'] = number_rooms
Hotel['price'] = cleaned_price
print(Hotel)

sys.exit()
