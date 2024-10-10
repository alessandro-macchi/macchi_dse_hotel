import sys
import random
import pandas as pd

# importo i datasets
ds_hotel = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/hotels.csv")
ds_pref = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/preferences.csv")
ds_guest = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/guests.csv")

#creo due liste di liste con all'interno gli hotel e gli ospiti
guest_list = [[i] for i in ds_guest.guest]
hotel_list = [[i] for i in ds_hotel.hotel]
big_hotel_list = []

# creo una variabile con il numero di stanze per hotel
n_rooms = pd.to_numeric(ds_hotel.rooms, errors = 'coerce')

#modifico la lista con gli hotel per fare in modo che gli hotel vengano ripetuti tante volte volte
#quante sono le stanze dello stesso
ROOMS_COUNT = 0
i = 0
for x in hotel_list:
    while ROOMS_COUNT < n_rooms[i]:
        big_hotel_list.append(x)
        ROOMS_COUNT = ROOMS_COUNT + 1
    ROOMS_COUNT = 0
    i = i + 1

#creo una funzione per trasformare una lista di liste in una lista singola
def list_cleaner(lista_da_pulire, lista_pulita):
    for j in lista_da_pulire:
        for item in j:
            lista_pulita.append(item)

second_big_hotel_list = []
list_cleaner(big_hotel_list, second_big_hotel_list)

second_guest_list = []
list_cleaner(guest_list, second_guest_list)

# alcune stanze rimangono vuote
len_check = len(big_hotel_list) == len(guest_list)
 #print(len_check)

#mischio le stanze, altrimenti non sarebbe random
random.shuffle(second_big_hotel_list)

#creo un dizionario con le allocazioni casuali
random_allocation = dict(zip(second_guest_list, second_big_hotel_list))
print(random_allocation)

sys.exit()
