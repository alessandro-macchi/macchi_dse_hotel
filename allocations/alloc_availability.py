import sys
sys.path.append('C:/Users/Utente/Desktop/dse/1t/python_project/macchi_dse_hotel')
from modules.my_functions import *

hotel_df, guests_df, priority_df = import_datasets()
hotel_df, guests_df, priority_df = create_dataframes(hotel_df, guests_df, priority_df)

#analogue to alloc_price, it just changes the sorting
hotel_df.sort_values(by = 'initial_rooms', ascending = False, inplace = True)
hotel_df.set_index('name', inplace = True)
guests_df.set_index('name', inplace = True)

assignment_availability = {}
assignment_availability = hotel_wise_allocation(hotel_df, guests_df, assignment_availability)

#number of customers accommodated
assigned_guests_availability = number_of_customers_accommodated(assignment_availability)

#the number of rooms occupied
occupied_rooms_availability = number_of_rooms_occupied(hotel_df)

#the number of different hotels occupied
full_hotels_availability = number_of_different_hotels_occupied(hotel_df)

#the total volume of business (total earnings of each hotel)
hotel_revenue_availability = hotel_earnings(assignment_availability, guests_df, hotel_df)
total_revenue_availability = total_volume_of_business1(hotel_revenue_availability)

# the degree of customer satisfaction 
average_satisfaction_availability = customer_satisfaction(guests_df, assignment_availability)