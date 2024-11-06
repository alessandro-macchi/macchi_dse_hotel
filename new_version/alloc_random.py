import random
import my_modules

ds_hotel, ds_pref, ds_guests = my_modules.importing()
hotel_df, guests_df, priority_df = my_modules.df_creation(ds_hotel, ds_pref, ds_guests)

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
assigned_guests_random = my_modules.number_of_customers_accommodated(assignment_random)

#the number of rooms occupied
occupied_rooms_random = my_modules.number_of_rooms_occupied(hotel_df)

#the number of different hotels occupied
full_hotels_random = my_modules.number_of_different_hotels_occupied(hotel_df)

#the total volume of business (total earnings of each hotel)
hotel_revenue_random = my_modules.hotel_earnings(assignment_random, guests_df, hotel_df)
total_revenue_random = my_modules.total_volume_of_business1(hotel_revenue_random)

#the degree of customer satisfaction
# RANDOM CASE HAS A SPECIFIC FUNCTION
average_satisfaction_random = my_modules.customer_satisfaction_random(guests_df, assignment_random)