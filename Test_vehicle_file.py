"""
Here we can test all of the functionality from the parent vehicle class
"""

from vichle_file import Vehicles


car_1 = Vehicles("BMW", "2015", "2018", 0, "ABCD", 0)

print("Car model       | Release date | Purchase date | Money made     | Plate number   | Rent times |")
print(car_1.vehicle_info())
print("Model            | total money    | rent times")
print(car_1.total_money())
print("total money after renting: {}".format(car_1.rent_vehicle(1000)))
