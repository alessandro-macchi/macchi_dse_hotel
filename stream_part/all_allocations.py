import sys
sys.path.append('C:/Users/Utente/Desktop/dse/1t/python_project/macchi_dse_hotel')
from modules.my_functions import *
from stream_part.my_graph_st import *
import random

def allocate_random(guests_df, hotel_df):

    hotel_df.set_index('name', inplace = True)
    guests_df.set_index('name', inplace = True)
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
    assigned_guests_random = number_of_customers_accommodated(assignment_random)

    #the number of rooms occupied
    occupied_rooms_random = number_of_rooms_occupied(hotel_df)

    #the number of different hotels occupied
    full_hotels_random = number_of_different_hotels_occupied(hotel_df)

    #the total volume of business (total earnings of each hotel)
    hotel_revenue_random = hotel_earnings(assignment_random, guests_df, hotel_df)
    total_revenue_random = total_volume_of_business1(hotel_revenue_random)

    #the degree of customer satisfaction
    # RANDOM CASE HAS A SPECIFIC FUNCTION
    average_satisfaction_random = customer_satisfaction_random(guests_df, assignment_random)
    
    return assignment_random, assigned_guests_random, occupied_rooms_random, full_hotels_random, total_revenue_random, average_satisfaction_random

def allocate_preferences(guests_df, hotel_df):

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
    
    return assignment_preferences, assigned_guests_preferences, occupied_rooms_preferences, full_hotels_preferences, total_revenue_preferences, average_satisfaction_preferences

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

def allocate_by_availability(guests_df, hotel_df):

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
    
    return assignment_availability, assigned_guests_availability, occupied_rooms_availability, full_hotels_availability, total_revenue_availability, average_satisfaction_availability