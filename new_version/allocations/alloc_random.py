import sys
import random
import pandas as pd
from tabulate import tabulate

# importing datasets
ds_hotel = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/python_project/Datasets/hotels.csv")
ds_pref = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/python_project/Datasets/preferences.csv")
ds_guest = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/python_project/Datasets/guests.csv")

# create a dictionary for every dataset
hotel = {
    'name': ds_hotel.hotel,
    'price': ds_hotel.price,
    'initial_rooms': pd.to_numeric(ds_hotel.rooms, errors = 'coerce'),
    'final_rooms': pd.to_numeric(ds_hotel.rooms, errors = 'coerce')
}
guests = {
    'name': ds_guest.guest,
    'discount': pd.to_numeric(ds_guest.discount, errors = 'coerce'),
    'preferences': ""
}
priority = {
    'name': ds_pref.guest,
    'hotel': ds_pref.hotel,
    'number': ds_pref.priority
    
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

hotel_df = pd.DataFrame(hotel)
guests_df = pd.DataFrame(guests)
priority_df = pd.DataFrame(priority)

guests_df['preferences'] = pref_list

hotel_df.set_index('name', inplace = True)
guests_df.set_index('name', inplace=True)
random.seed(6) #i want the same random result every time to analyze it
assignment_random = {}

for guest in guests_df.index:
    assigned_hotel = None
    while assigned_hotel is None:
        chosen_hotel = random.choice(hotel_df.index)
        row = hotel_df.loc[chosen_hotel]
        if row['final_rooms'] > 0:
            assignment_random[guest] = chosen_hotel
            hotel_df.loc[chosen_hotel, 'final_rooms'] -= 1
            assigned_hotel = chosen_hotel

#number of customers accommodated
assigned_guests_random = len(assignment_random)

#the number of rooms occupied
occupied_rooms_random = (hotel_df['initial_rooms'].sum() - hotel_df['final_rooms'].sum())

#the number of different hotels occupied
full_hotels_random = 0
for hotel in hotel_df.index:
    if hotel_df.loc[hotel, 'final_rooms'] == 0:
        full_hotels_random += 1

#the total volume of business (total earnings of each hotel)
revenue_random = 0
for hotel in hotel_df.index:
    rooms_hotel = hotel_df.loc[hotel, 'initial_rooms']
    hotel_revenue = hotel_df.loc[hotel, 'price'] * (hotel_df.loc[hotel, 'initial_rooms'] - hotel_df.loc[hotel, 'final_rooms'])
    revenue_random += hotel_revenue


total_satisfaction = float(0)
for guest in guests_df.index:
    preference_position = 0
    hotel_pref = guests_df.loc[guest, 'preferences']
    if assignment_random[guest] in hotel_pref:
        for i, preferred_hotel in enumerate(hotel_pref):
            if preferred_hotel == assignment_random[guest]:
                preference_position = i
                break
        g_satisfaction = (len(hotel_pref) - preference_position) / len(hotel_pref)
    else:
        g_satisfaction = 0
    total_satisfaction += g_satisfaction

average_satisfaction = total_satisfaction / len(guests_df)
print("Average customer satisfaction:", average_satisfaction)
    


#(calculated according to the location of the hotel assigned to them with respect to their preferences)

sys.exit()