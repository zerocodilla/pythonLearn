import restaurant

restaurant_2 = restaurant.Restaurant('BarBQ', 'european')
restaurant_2.describe_restaurant()
restaurant_2.customers_served()
restaurant_2.number_served = 199
restaurant_2.customers_served()
restaurant_2.set_number_served(201)
restaurant_2.customers_served()
restaurant_2.increment_number_served(100)
restaurant_2.customers_served()
restaurant_2.increment_number_served(-9)
restaurant_2.customers_served()

favorite_restaurant = restaurant.Restaurant('TomYum', 'asian')
restaurant_0 = restaurant.Restaurant('Victoria', 'european')
restaurant_1 = restaurant.Restaurant('Happy', 'european')
restaurant_1.describe_restaurant()

gelato = restaurant.IceCreamStand('Gelato', 'asian', ['lemon', 'chocolate', 'vanilla', 'strawberry'])
gelato.display_flavors()

rests = [favorite_restaurant, restaurant_0, restaurant_1]
for rest in rests:
    rest.describe_restaurant()