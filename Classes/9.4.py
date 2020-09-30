class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('This is my restaurant')

    def open_restaurant(self):
        print('Open from 1 AM to 9 PM')

    def set_number_served(self, numb):
        self.number_served = numb

    def increment_number_served(self, numb):
        self.number_served += numb


rest1 = Restaurant('Magia', 'Polish food')
print(rest1.restaurant_name)
print(rest1.cuisine_type)
print(rest1.number_served)
rest1.number_served = 54
print(rest1.number_served)

rest1.set_number_served(66)
print(rest1.number_served)

rest1.increment_number_served(12)
print(rest1.number_served)

