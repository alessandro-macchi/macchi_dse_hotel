import sys
import random
import pandas as pd


ds_hotel = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/hotels.csv")
ds_pref = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/preferences.csv")
ds_guest = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/guests.csv")


guest_list = [[i] for i in ds_guest.guest]
hotel_list = [[i] for i in ds_hotel.hotel]
big_hotel_list = []

n_rooms = pd.to_numeric(ds_hotel.rooms, errors = 'coerce')

count_rooms = 0
i = 0
for x in hotel_list:
    while count_rooms < n_rooms[i]:
        big_hotel_list.append(x)
        count_rooms = count_rooms + 1
    count_rooms = 0
    i = i + 1

#elimino uno strato della lista degli hotel
second_big_hotel_list = []
for item in big_hotel_list:
    x = (' '.join(item))
    second_big_hotel_list.append(x)

#elimino uno strato della lista degli ospiti
second_guest_list = []
for item in guest_list:
    x = (' '.join(item))
    second_guest_list.append(x)

# alcune stanze rimangono vuote
len_check = len(big_hotel_list) == len(guest_list)
 #print(len_check)

#mischio le stanze, altrimenti non sarebbe random
random.shuffle(second_big_hotel_list)

#creo un dizionario con le allocazioni casuali
random_allocation = dict(zip(second_guest_list, second_big_hotel_list))
print(random_allocation)

sys.exit()
