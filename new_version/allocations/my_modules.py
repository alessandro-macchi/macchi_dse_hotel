import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

def plot_hotel_revenue(assignment, guests_df, hotel_df):
    # Calculate revenue for each hotel based on assigned guests
    hotel_revenue = {}
    for guest, hotel in assignment.items():
        discount = guests_df.loc[guest, 'discount']
        price = hotel_df.loc[hotel, 'price']
        revenue = price * (1 - discount)
        hotel_revenue[hotel] = hotel_revenue.get(hotel, 0) + revenue
    
    # Plotting
    hotels = list(hotel_revenue.keys())
    revenues = list(hotel_revenue.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(hotels, revenues, color='skyblue')
    plt.xlabel('Hotels')
    plt.ylabel('Revenue')
    plt.title('Revenue by Hotel')
    plt.xticks(rotation=45)
    plt.tight_layout()

def importing():
    # Import datasets
    ds_hotel = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/python_project/Datasets/hotels.csv")
    ds_pref = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/python_project/Datasets/preferences.csv")
    ds_guests = pd.read_csv("C:/Users/Utente/Desktop/dse/1t/python_project/Datasets/guests.csv")
    return ds_hotel, ds_pref, ds_guests

def df_creation(ds_hotel, ds_pref, ds_guests):  # Make sure these parameters are here
    # Create dictionaries for each dataset
    a = {
        'name': ds_hotel['hotel'],
        'price': ds_hotel['price'],
        'initial_rooms': pd.to_numeric(ds_hotel['rooms'], errors='coerce'),
        'final_rooms': pd.to_numeric(ds_hotel['rooms'], errors='coerce')
    }
    b = {
        'name': ds_guests['guest'],
        'discount': pd.to_numeric(ds_guests['discount'], errors='coerce'),
        'preferences': ""
    }
    c = {
        'name': ds_pref['guest'],
        'hotel': ds_pref['hotel'],
        'number': ds_pref['priority']
    }
    
    # Create list of preferred hotels for each guest
    pref_list = []
    i = 0
    for guest in b['name']:
        temporary_list = []
        while i < len(ds_pref) and ds_pref['guest'][i] == guest:
            temporary_list.append(ds_pref['hotel'][i])
            i += 1
        pref_list.append(temporary_list)
    
    # Create DataFrames from dictionaries
    hotel_df = pd.DataFrame(a)
    guests_df = pd.DataFrame(b)
    priority_df = pd.DataFrame(c)
    
    # Add preferences to guests_df
    guests_df['preferences'] = pref_list
    
    return hotel_df, guests_df, priority_df

def number_of_customers_accommodated(assignment):
    assigned_guests = len(assignment)
    return assigned_guests

def number_of_rooms_occupied(hotel_df):
    initial_rooms = hotel_df['initial_rooms'].to_numpy()
    final_rooms = hotel_df['final_rooms'].to_numpy()
    occupied_rooms = np.sum(initial_rooms - final_rooms)
    return occupied_rooms

def number_of_different_hotels_occupied(hotel_df):
    full_hotels = 0
    for hotel in hotel_df.index:
        if hotel_df.loc[hotel, 'final_rooms'] == 0:
            full_hotels += 1
    return full_hotels

def total_volume_of_business1(assignment, guests_df, hotel_df):
    total_revenue = 0
    for guest, hotel in assignment.items():
        guest_discount = guests_df.loc[guest, 'discount']
        hotel_price = hotel_df.loc[hotel, 'price']
        guest_price = hotel_price - (hotel_price * guest_discount)
        total_revenue += guest_price
    return total_revenue

#second method (NumPy)
def total_volume_of_business2(assignment, guests_df, hotel_df):
    guests = np.array(list(assignment.keys()))
    hotels = np.array(list(assignment.values()))
    discounts = guests_df.loc[guests, 'discount'].values
    prices = hotel_df.loc[hotels, 'price'].values
    guest_prices = prices - (prices * discounts)
    total_revenue = np.sum(guest_prices)
    return total_revenue

def customer_satisfaction_random(guests_df, assignment_random):
    total_satisfaction_random = float(0)
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
        total_satisfaction_random += g_satisfaction

    average_satisfaction_random = total_satisfaction_random / len(guests_df)
    return average_satisfaction_random

def customer_satisfaction(guests_df, assignment):
    total_satisfaction = float(0)
    for guest in guests_df.index:
        if guest in assignment.keys():
            preference_position = 0
            hotel_pref = guests_df.loc[guest, 'preferences']
            for i, preferred_hotel in enumerate(hotel_pref):
                if preferred_hotel == assignment[guest]:
                    preference_position = i
                    break
            g_satisfaction = (len(hotel_pref) - preference_position) / len(hotel_pref)
        else:
            g_satisfaction = 0
        total_satisfaction += g_satisfaction

    average_satisfaction = total_satisfaction / len(guests_df)
    return average_satisfaction

def hotel_wise_allocation(hotel_df, guests_df, assignment):
    for hotel_name, row in hotel_df.iterrows():
        # create a vector with the guests that have the hotel_name in their preferences
        guests_vector = guests_df[guests_df['preferences'].apply(lambda x: hotel_name in x)].index
        for guest_name in guests_vector:
            if row['final_rooms'] > 0 and guest_name not in assignment:
                assignment[guest_name] = hotel_name
                hotel_df.loc[hotel_name, 'final_rooms'] -= 1
            # stop the iteration on the guests when there are no more rooms available
            if hotel_df.loc[hotel_name, 'final_rooms'] <= 0:
                break
    return assignment
