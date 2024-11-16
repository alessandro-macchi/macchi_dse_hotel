import sys
import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from modules.my_functions import *
from allocations.st_alloc_random import allocate_random
from allocations.st_alloc_pref import allocate_preferences
from allocations.st_alloc_price import allocate_by_price
from allocations.st_alloc_availability import allocate_by_availability
sys.path.append('C:/Users/Utente/Desktop/dse/1t/python_project/macchi_dse_hotel')

hotel_df, guests_df, priority_df = import_datasets()
hotel_df, guests_df, priority_df = create_dataframes(hotel_df, guests_df, priority_df)

# Streamlit App
st.title("Hotel Allocation Strategies")

# Strategy Selection
strategy = st.selectbox("Choose Allocation Strategy", ["Random", "Preferences", "Price", "Availability"])

# Execute Allocation Based on Strategy
if st.button("Run Allocation"):
    if strategy == "Random":
        allocation, assigned_guests, occupied_rooms, full_hotels, total_revenue, average_satisfaction = allocate_random(guests_df, hotel_df)
    elif strategy == "Preferences":
        allocation, assigned_guests, occupied_rooms, full_hotels, total_revenue, average_satisfaction = allocate_preferences(guests_df, hotel_df)
    elif strategy == "Price":
        allocation, assigned_guests, occupied_rooms, full_hotels, total_revenue, average_satisfaction = allocate_by_price(guests_df, hotel_df)
    elif strategy == "Availability":
        allocation, assigned_guests, occupied_rooms, full_hotels, total_revenue, average_satisfaction = allocate_by_availability(guests_df, hotel_df)
    else:
        st.error("Invalid Strategy Selected")
        sys.exit()

    # Display Allocation Results
    st.subheader(f"Results for {strategy} Allocation")
    
    # Guest-Hotel Assignments
    st.subheader("Guest-Hotel Assignments")
    assignments_df = pd.DataFrame(list(allocation.items()), columns=["Guest", "Hotel"])
    st.dataframe(assignments_df)

    # Metrics
    st.subheader("Metrics")
    st.write(f"Guests Accommodated: {assigned_guests}")
    st.write(f"Rooms Occupied: {occupied_rooms}")
    st.write(f"Hotels Fully Occupied:{full_hotels}")
    st.write(f"Total Strategy Revenue: {total_revenue}")
    st.write(f"Average Satisfaction: {average_satisfaction}")