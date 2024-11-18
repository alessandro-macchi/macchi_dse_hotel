import streamlit as st
import matplotlib.pyplot as plt
 
def plot_hotel_revenue(assignment, guests_df, hotel_df):
    hotel_revenue = {}
    for guest, hotel in assignment.items():
        discount = guests_df.loc[guest, 'discount']
        price = hotel_df.loc[hotel, 'price']
        revenue = price * (1 - discount)
        hotel_revenue[hotel] = hotel_revenue.get(hotel, 0) + revenue
    
    hotels = list(hotel_revenue.keys())
    revenues = list(hotel_revenue.values())
    
    fig = plt.figure(figsize=(8, 4.5))
    plt.bar(hotels, revenues, color='skyblue')
    plt.xlabel('Hotels')
    plt.ylabel('Revenue')
    plt.title('Revenue by Hotel')
    plt.xticks([])
    plt.tight_layout()
    st.pyplot(fig)