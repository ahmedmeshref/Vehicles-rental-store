"""
Here we can test all of the functionality from the Motobike class
"""

from moto_class_file import Motorbike


moto = Motorbike("KS", "2015", "2015", 0, "1256", 0, 2)

print("value carbon footprint= " + moto.moto_carbon_footprint())
print("Number of helmets=", moto.number_of_helmets())
print("Car model       | Release date | Purchase date | Money made     | Plate number   | Rent times | Number of "
      "helmets")
print(moto.info())

