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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        print('Available flavors: ' + str(self.flavors))


ice = IceCreamStand('Bosko', 'Dessert', ['Orange', 'Chocolate', 'Vanilla'])
ice.print_flavors()



