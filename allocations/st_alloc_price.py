import sys
sys.path.append('C:/Users/Utente/Desktop/dse/1t/python_project/macchi_dse_hotel')
from modules.my_functions import *
from modules.my_graph_st import *

def allocate_by_price(guests_df, hotel_df):

    #analogue to alloc_availability, it just changes the sorting
    hotel_df.sort_values(by = 'price', ascending = True, inplace = True)
    hotel_df.set_index('name', inplace = True)
    guests_df.set_index('name', inplace = True)

    assignment_price = {}
    assignment_price = hotel_wise_allocation(hotel_df, guests_df, assignment_price)

    #number of customers accommodated
    assigned_guests_price = number_of_customers_accommodated(assignment_price)

    #the number of rooms occupied
    occupied_rooms_price = number_of_rooms_occupied(hotel_df)

    #the number of different hotels occupied
    full_hotels_price = number_of_different_hotels_occupied(hotel_df)

    #the total volume of business (total earnings of each hotel)
    hotel_revenue_price = hotel_earnings(assignment_price, guests_df, hotel_df)
    total_revenue_price = total_volume_of_business1(hotel_revenue_price)

    # the degree of customer satisfaction 
    average_satisfaction_price = customer_satisfaction(guests_df, assignment_price)
    
    return assignment_price, assigned_guests_price, occupied_rooms_price, full_hotels_price, total_revenue_price, average_satisfaction_price