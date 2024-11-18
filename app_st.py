import sys
import streamlit as st
import pandas as pd
from modules.my_functions import *
from stream_section.my_graph_st import *
from stream_section.all_allocations import *

sys.path.append('C:/Users/Utente/Desktop/dse/1t/python_project/macchi_dse_hotel')

hotel_df, guests_df, priority_df = import_datasets()
hotel_df, guests_df, priority_df = create_dataframes(hotel_df, guests_df, priority_df)

st.title("🏨 Hotel Allocation Strategies")

st.sidebar.header("Allocation Options")
strategy = st.sidebar.selectbox("Choose Allocation Strategy", ["Random", "Preferences", "Price", "Availability"])

if st.sidebar.button("Run Allocation"):
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

    st.header(f"📋 Results for {strategy} Allocation")
    st.success("Allocation completed successfully!")

    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Guests Accommodated", f"{assigned_guests}")
    col2.metric("Rooms Occupied", f"{occupied_rooms}")
    col3.metric("Hotels Fully Occupied", f"{full_hotels}")

    col4, col5 = st.columns(2)
    col4.metric("Total Revenue", f"€{round(total_revenue, 2)}")
    col5.metric("Average Satisfaction", f"{round(average_satisfaction * 100, 2)}%")

    st.subheader("🛏️ Guest-Hotel Assignments")
    assignments_df = pd.DataFrame(list(allocation.items()), columns=["Guest", "Hotel"])
    st.dataframe(assignments_df.reset_index(drop = True))

    unassigned_guests = list(set(guests_df.index) - set(assignments_df["Guest"]))

    if unassigned_guests:
        st.warning(f"⚠️ {len(unassigned_guests)} Guests Could Not Be Assigned")
        unassigned_df = pd.DataFrame(unassigned_guests, columns=["Unassigned Guests"])
        st.dataframe(unassigned_df.reset_index(drop = True), height=200)
    else:
        st.success("🎉 All guests have been successfully assigned!")

    st.subheader("📈 Revenue Distribution by Hotel")
    plot_hotel_revenue(allocation, guests_df, hotel_df)