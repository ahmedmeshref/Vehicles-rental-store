"""
Here we can test all of the functionality from the Car class
"""

from car_class_file import Car

car_1 = Car("BMW", "2015", "2017", 0, "1234", 0)


print("Car model       | Release date | Purchase date | Money made     | plate number   | rent times")
print(car_1.vehicle_info())

print("value carbon footprint= " + car_1.car_carbon_footprint())
