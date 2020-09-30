class Employee:

    def __init__(self, name, lastname, year_revenue):
        self.name = name
        self.lastname = lastname
        self.year_revenue = year_revenue

    def give_raise(self, increase=5000):
        self.year_revenue += increase
