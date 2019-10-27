"""
Car class is a child of the Vehicles class, it has new method for a car in the store which is
car_carbon_footprint that returns the carbon footprint.
"""

from vichle_file import Vehicles


class Car(Vehicles):
    def car_carbon_footprint(self):
        value_carbon_footprint = (2019 - int(self.release_date)) * 1200 * 9 * 15
        return str(value_carbon_footprint)
