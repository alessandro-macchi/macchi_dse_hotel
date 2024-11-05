import my_modules

ds_hotel, ds_pref, ds_guests = my_modules.importing()
hotel_df, guests_df, priority_df = my_modules.df_creation(ds_hotel, ds_pref, ds_guests)

#analogue to alloc_availability, it just changes the sorting
hotel_df.sort_values(by = 'price', ascending = True, inplace = True)
hotel_df.set_index('name', inplace = True)
guests_df.set_index('name', inplace = True)

assignment_price = {}
assignment_price = my_modules.hotel_wise_allocation(hotel_df, guests_df, assignment_price)

#number of customers accommodated
assigned_guests_price = my_modules.number_of_customers_accommodated(assignment_price)

#the number of rooms occupied
occupied_rooms_price = my_modules.number_of_rooms_occupied(hotel_df)

#the number of different hotels occupied
full_hotels_price = my_modules.number_of_different_hotels_occupied(hotel_df)

#the total volume of business (total earnings of each hotel)
total_revenue_price = my_modules.total_volume_of_business1(assignment_price, guests_df, hotel_df)

# the degree of customer satisfaction 
average_satisfaction_price = my_modules.customer_satisfaction(guests_df, assignment_price)

#Grafici