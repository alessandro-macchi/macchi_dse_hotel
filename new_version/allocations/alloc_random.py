import sys
import random
import pandas as pd

# importing datasets
ds_hotel = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/Python project/Datasets/hotels.csv")
ds_pref = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/Python project/Datasets/preferences.csv")
ds_guest = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/Python project/Datasets/guests.csv")

# create a dictionary for every dataset
hotel = {
    'name': ds_hotel.hotel,
    'price': ds_hotel.price,
    'n_rooms': pd.to_numeric(ds_hotel.rooms, errors = 'coerce')
}
guests = {
    'name': ds_guest.guest,
    'discount': pd.to_numeric(ds_guest.discount, errors = 'coerce')
}

# create a list of the hotels in order of preference for every guest
pref_list = []
i = 0
for guest in guests['name']:
    temporary_list = []
    # iterate until we find hotels for the current guest
    while i < len(ds_pref) and ds_pref.guest[i] == guest:
        temporary_list.append(ds_pref.hotel[i])
        i += 1
    pref_list.append(temporary_list)

preferences = {
    'guest': guests['name'],
    'hotel': pref_list
}

hotel_df = pd.DataFrame(hotel)
guests_df = pd.DataFrame(guests)
preferences_df = pd.DataFrame(preferences)

hotel_df.set_index('name', inplace=True)
random.seed(6) #i want the same random result every time to analyze it
assignment = {}

for guest in guests_df['name']:
    assigned_hotel = None
    while assigned_hotel is None:
        chosen_hotel = random.choice(hotel_df.index)
        row = hotel_df.loc[chosen_hotel]
        if row['n_rooms'] > 0:
            assignment[guest] = chosen_hotel
            hotel_df.loc[chosen_hotel, 'n_rooms'] -= 1
            assigned_hotel = chosen_hotel

print("Guest assigned:", len(assignment)) #all guests have been allocated

print("\nRemaining rooms in hotels:")
print(hotel_df.drop(columns = 'price')) #these are the unassigned rooms per hotel

sys.exit()