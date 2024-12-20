import sys
sys.path.append('C:/Users/Utente/Desktop/dse/1t/python_project/macchi_dse_hotel')
from modules.my_functions import *

hotel_df, guests_df, priority_df = import_datasets()
hotel_df, guests_df, priority_df = create_dataframes(hotel_df, guests_df, priority_df)

hotel_df.set_index('name', inplace = True)
guests_df.set_index('name', inplace = True)
assignment_preferences = {}

for guest in guests_df.index:
    # get the list of preferred hotels for the current guest
    preferences = guests_df.loc[guests_df.index == guest, 'preferences'].values[0]
    # try to allocate the guest based on his preferences
    for chosen_hotel in preferences:
        row = hotel_df.loc[chosen_hotel]
        if row['final_rooms'] > 0:
            assignment_preferences[guest] = chosen_hotel
            hotel_df.loc[chosen_hotel, 'final_rooms'] -= 1
            break

#number of customers accommodated
assigned_guests_preferences = number_of_customers_accommodated(assignment_preferences)

#the number of rooms occupied
occupied_rooms_preferences = number_of_rooms_occupied(hotel_df)

#the number of different hotels occupied
full_hotels_preferences = number_of_different_hotels_occupied(hotel_df)

#the total volume of business (total earnings of each hotel)
hotel_revenue_preferences = hotel_earnings(assignment_preferences, guests_df, hotel_df)
total_revenue_preferences = total_volume_of_business1(hotel_revenue_preferences)

# the degree of customer satisfaction 
average_satisfaction_preferences = customer_satisfaction(guests_df, assignment_preferences)