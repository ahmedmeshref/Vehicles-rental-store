"""
Motorbike class is a child of the Vehicles class, it has new methods for a motobike in the store such as
moto_carbon_footprint that returns the carbon footprint, also it adds a new feature to the moto which is the
number of helmets
"""

from vichle_file import Vehicles


class Motorbike(Vehicles):
    def __init__(self, model, release_date, purchase_date, money_made, plate_number, rent_times, helmets):
        # inheriting all of the main features from the vehicles class
        super().__init__(model, release_date, purchase_date, money_made, plate_number, rent_times)
        # defining the number of helmets feature
        self.helmets = helmets

    def moto_carbon_footprint(self):
        value_carbon_footprint = (2019 - int(self.release_date)) * 10000 * 2 * 9
        return str(value_carbon_footprint)

    def number_of_helmets(self):
        return self.helmets

    def info(self):
        return super(Motorbike, self).vehicle_info() + " {}  ".format(self.helmets)
