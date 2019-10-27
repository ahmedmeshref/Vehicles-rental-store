"""
The Car class has some functionality for the car store, it takes in some information about each car
like the car model, rent times, money made out of it etc..
Then, it can return info about the cars and total money made by each car, and gives the owner the ability to rent a car
"""


class Vehicles(object):
    def __init__(self, model, release_date, purchase_date, money_made, plate_number, rent_times):
        self.model = model
        self.release_date = release_date
        self.purchase_date = purchase_date
        self.money_made = money_made
        self.plate_number = plate_number
        self.rent_time = rent_times

    # getting the cars information
    def vehicle_info(self):
        space_1 = " " * (15 - len(self.model))
        space_2 = " " * (15 - len(str(self.money_made)))
        space_3 = " " * (15 - len(self.plate_number))
        return "{} {}| {}         | {}          | {}{}| {}{}| {}          |".format(
            self.model, space_1, self.release_date, self.purchase_date, self.money_made, space_2, self.plate_number, space_3, self.rent_time
        )

    # getting the total money made out of a car
    def total_money(self):
        space_1 = " " * (15 - len(self.model))
        space_2 = " " * (15 - len(str(self.money_made)))
        return "{} {} | {}{}| {}".format(
            self.model, space_1, self.money_made, space_2, self.rent_time)

    # rent a car
    def rent_vehicle(self, price):
        self.money_made += price
        return self.money_made
