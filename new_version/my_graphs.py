import matplotlib.pyplot as plt

def revenue_comparison_by_strategy(total_revenue_random, total_revenue_preferences, total_revenue_price, total_revenue_availability):
    strategies = ['Random', 'Preference', 'Price', 'Availability']
    revenues = [total_revenue_random, total_revenue_preferences, total_revenue_price, total_revenue_availability]

    plt.figure(figsize=(8, 4.5))
    plt.bar(strategies, revenues, color=['blue', 'green', 'orange', 'purple'])
    plt.title('Revenue Comparison by Strategy')
    plt.xlabel('Allocation Strategy')
    plt.ylabel('Total Revenue in €')
    plt.show()

def customer_satisfaction_by_strategy(average_satisfaction_random, average_satisfaction_preferences, average_satisfaction_price, average_satisfaction_availability):
    strategies = ['Random', 'Preference', 'Price', 'Availability']
    satisfaction = [average_satisfaction_random, average_satisfaction_preferences, average_satisfaction_price, average_satisfaction_availability]

    plt.figure(figsize=(8, 4.5))
    plt.bar(strategies, satisfaction, color=['blue', 'green', 'orange', 'purple'])
    plt.title('Customer Satisfaction by Strategy')
    plt.xlabel('Allocation Strategy')
    plt.ylabel('Average Satisfaction')
    plt.ylim(0, 1)
    plt.show()
    
def plot_hotel_revenue(assignment, guests_df, hotel_df):
    hotel_revenue = {}
    for guest, hotel in assignment.items():
        discount = guests_df.loc[guest, 'discount']
        price = hotel_df.loc[hotel, 'price']
        revenue = price * (1 - discount)
        hotel_revenue[hotel] = hotel_revenue.get(hotel, 0) + revenue
    
    hotels = list(hotel_revenue.keys())
    revenues = list(hotel_revenue.values())
    
    plt.figure(figsize=(8, 4.5))
    plt.bar(hotels, revenues, color='skyblue')
    plt.xlabel('Hotels')
    plt.ylabel('Revenue')
    plt.title('Revenue by Hotel')
    plt.xticks([])
    plt.tight_layout()
    plt.show()