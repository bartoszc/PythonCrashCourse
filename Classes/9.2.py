class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('This is my restaurant')

    def open_restaurant(self):
        print('Open from 1 AM to 9 PM')


rest1 = Restaurant('Magia', 'Polish food')
print(rest1.restaurant_name)
print(rest1.cuisine_type)

rest1.describe_restaurant()
rest1.open_restaurant()

rest2 = Restaurant('Habiby', 'Kebab')
print(rest2.restaurant_name)
print(rest2.cuisine_type)

rest2.describe_restaurant()
rest2.open_restaurant()

rest3 = Restaurant('Kartel', 'Mexican food')
print(rest3.restaurant_name)
print(rest3.cuisine_type)

rest3.describe_restaurant()
rest3.open_restaurant()