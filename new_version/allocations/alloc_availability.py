import sys
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

hotel_df.sort_values(by = 'n_rooms', ascending = False, inplace = True)
hotel_df.set_index('name', inplace = True)
assignment = {}

for hotel_name, row in hotel_df.iterrows():
    # create a vector with the guests that have the hotel_name in their preferences
    guests_vector = preferences_df[preferences_df['hotel'].apply(lambda x: hotel_name in x)]['guest']
    for guest_name in guests_vector:
        if row['n_rooms'] > 0 and guest_name not in assignment:
            assignment[guest_name] = hotel_name
            hotel_df.loc[hotel_name, 'n_rooms'] -= 1
        # interrupt the iteration on the guests when there are no more rooms available
        if hotel_df.loc[hotel_name, 'n_rooms'] <= 0:
            break

print("Guest assigned:", len(assignment)) #not all guests have been allocated

allocated_guests = set(assignment.keys())
all_guests = set(guests_df['name'])
unassigned_guests = all_guests - allocated_guests
print("Guest not assigned:", len(unassigned_guests)) #these are the unassigned guests

print("\nRemaining rooms in hotels:")
print(hotel_df.drop(columns = 'price')) #these are the unassigned rooms per hotel

sys.exit()