import sys
import pandas as pd
import random
from collections import Counter

ds_hotel = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/hotels.csv")
ds_pref = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/preferences.csv")
ds_guest = pd.read_csv("C:/Users/Utente/Desktop/dse/ds py/guests.csv")


guest_list = [ds_guest.guest]
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

# alcune stanze rimangono vuote
len_check = len(big_hotel_list) == len(guest_list)
print(len_check)

#bisogna mischiare e assegnare

sys.exit()
