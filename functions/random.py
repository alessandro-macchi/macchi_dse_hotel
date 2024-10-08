def f_random():
    random_hotel_list = [[i] for i in ds_hotel.hotel]
    random.shuffle(random_hotel_list)
    print(random_hotel_list)