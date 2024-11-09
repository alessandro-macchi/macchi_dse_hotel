from pathlib import Path
import pandas as pd
import numpy as np

def import_datasets(base_path = "C:/Users/Utente/Desktop/dse/1t/python_project/Datasets/"):
    base_path = Path(base_path)
    ds_hotel = pd.read_csv(base_path / "hotels.csv")
    ds_pref = pd.read_csv(base_path / "preferences.csv")
    ds_guests = pd.read_csv(base_path / "guests.csv")
    
    return ds_hotel, ds_pref, ds_guests

def create_dataframes(ds_hotel, ds_pref, ds_guests):
    hotel_df = pd.DataFrame({
        'name': ds_hotel['hotel'],
        'price': ds_hotel['price'],
        'initial_rooms': pd.to_numeric(ds_hotel['rooms'], errors='coerce'),
        'final_rooms': pd.to_numeric(ds_hotel['rooms'], errors='coerce')
    })
    guests_df = pd.DataFrame({
        'name': ds_guests['guest'],
        'discount': pd.to_numeric(ds_guests['discount'], errors='coerce'),
        'preferences': [None] * len(ds_guests)
    })
    priority_df = pd.DataFrame({
        'name': ds_pref['guest'],
        'hotel': ds_pref['hotel'],
        'number': ds_pref['priority']
    })
    
    preferences = {}
    for x, row in ds_pref.iterrows():
        preferences.setdefault(row['guest'], []).append(row['hotel'])
    guests_df['preferences'] = guests_df['name'].map(preferences)
    
    return hotel_df, guests_df, priority_df

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

def hotel_earnings(assignment, guests_df, hotel_df):
    hotel_revenue = {}
    for guest, hotel in assignment.items():
        guest_discount = guests_df.loc[guest, 'discount']
        hotel_price = hotel_df.loc[hotel, 'price']
        guest_price = hotel_price - (hotel_price * guest_discount)
        if hotel in hotel_revenue:
            hotel_revenue[hotel] += guest_price
        else:
            hotel_revenue[hotel] = guest_price
    
    return hotel_revenue

def total_volume_of_business1(hotel_revenue):
    total_revenue = sum(hotel_revenue.values())
    
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

