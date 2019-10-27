"""
Algorithm: the program starts with printing menu that enables omandi to do 12 different operation on his list of
cars and motorbikes. Then, depending on his input, the program runs the operation from either car or moto child classes.
"""

"""
Test cases:
1- For the delete, I am asking the user to choose the number of the car, in case the user input a str or
an int out of index, my code won't crash and will print a message directing the user
2- If the user deleted all of the cars in the store and he tried to choose delete another car from the menu
the code will bring a message saying the are no cars in the store
3- Also if the user to tries to do another operation apart from adding a new car if he deleted all of the cars
the code will return no cars in the store
4- Adding new cars, if the user input some str values in any field the code will treat that and won't crash
5- If the user selected 5 to rent a car and then selected a car out of index or input a str, the code will return a
message guiding him and asking him to select car again
6- After showing the user, our list, if he chooses a number out of range, the program will handle it and ask him
to input another number in the range
7- try to create all of the cars as instances and then call each instance
"""


"""
This file contains the user menu of all operations that the program is capable of
"""
# importing the 3 needed classes
from vichle_file import Vehicles
from moto_class_file import Motorbike
from car_class_file import Car

# storing the cars in lists [model, release_date, purchase_date, money_made, plate_number, rent_times]
car_1 = ["BMW", "2015", "2017", 0, "1234", 0]
car_2 = ["KIA", "2017", "2017", 0, "4567", 0]
car_3 = ["FORD", "2018", "2018", 0, "6789", 0]
car_4 = ["MERCIDES", "2019", "2019", 0, "8901", 0]
car_5 = ["TESLA", "2015", "2015", 0, "1256", 0]
cars_list = [car_1, car_2, car_3, car_4, car_5]

# storing the motorbikes in lists [model, release_date, purchase_date, money_made, plate_number, rent_times, helmets]
motorbike_1 = ["ADB", "2019", "2019", 0, "8901", 0, 2]
motorbike_2 = ["KS", "2015", "2015", 0, "1256", 0, 2]
motorbike_list = [motorbike_1, motorbike_2]

'''
Menu function takes in no arguments and prints the main menu with all of the program functionality 
'''


def menu():
    global action
    try:
        action = input('                   MENU\n'
                       '1. list all Vehicle          2. list cars only\n'
                       '3. list motorbikes only      4. count the total money\n'
                       '5. delete an existing Car    6. delete an existing motorbikes\n'
                       '7. add a new car             8. add a new motorbikes\n'
                       '9. rent a car                10. rent a motorbikes\n'
                       '11. car carbon footprint     12. motorbikes carbon footprint\n'
                       'Select a number: ')
    except ValueError:
        print("Invalid input! Select a number")
        menu()
    print("-----------------------------------------------------------------------------------------------------------")
    main(action)


'''
This function takes in a list and checks whether the given list has elements or not,
 if not return invalid operation, if yes, it lists them for the user to choose an element and return the user input
'''


def vehicles_validation(v_l):
    global selected_vehicle
    if len(v_l) == 0:
        return "E"
    index = 0
    for v in v_l:
        print(str(index) + ". " + v[0])
        index += 1
    try:
        selected_vehicle = int(input("Select a vehicle number: "))
        while selected_vehicle > index:
            print("Select a number in the range of the existing vehicles")
            selected_vehicle = int(input("Select a vehicle number: "))
    except ValueError:
        print("Invalid, Enter a numbers not a word!")
        exit()
    return selected_vehicle


''' 
car_info function takes in a list of cars and prints all of its elements
'''


def car_info(c_list):
    for car in c_list:
        car_item = Car(car[0], car[1], car[2], car[3], car[4], car[5])
        print(car_item.vehicle_info())


''' 
moto_info function takes in a list of motos and prints all of its elements
'''


def moto_info(m_list):
    for moto in m_list:
        moto_item = Motorbike(moto[0], moto[1], moto[2], moto[3], moto[4], moto[5], moto[6])
        print(moto_item.info())


'''
Delete vehicle function takes in a list and calls the vehicle validation to list the cars then delete a car for the user
and return the new list
'''


def delete_vehicles(v_l):
    global del_element
    selected_ele = vehicles_validation(v_l)
    if selected_ele == "E":
        print("Invalid! 0 vehicles to delete!")
        return []
    del v_l[selected_ele]
    return v_l


'''
add_new_vehicle function take in no arguments and it collects some information for any new vehicle that the user want to 
add
'''


def add_new_vehicle():
    model = input("Enter the vehicle model: ")
    release_date = input("Enter the release year: ")
    purchase_date = input("Enter the purchase year: ")
    plate_number = input("Enter the plate number: ")
    return model, release_date, purchase_date, plate_number


'''
rent vehicle function takes in a list and whether the list is for a car or moto and calls the vehicles validation 
function to print all elements in the rest and choose a vehicle to rent with a specified price
'''


def rent_vehicle(v_l, car_or_moto):
    selected_ele = vehicles_validation(v_l)
    if selected_ele == "E":
        print("Invalid! 0 vehicles to rent!")
        return []
    price = int(input("Enter the price in numbers (without $): "))
    if car_or_moto == 1:
        veh = Car(cars_list[selected_ele][0], cars_list[selected_ele][1], cars_list[selected_ele][2],
                  cars_list[selected_ele][3], cars_list[selected_ele][4], cars_list[selected_ele][5])

    else:
        veh = Motorbike(motorbike_list[selected_ele][0], motorbike_list[selected_ele][1],
                        motorbike_list[selected_ele][2],
                        motorbike_list[selected_ele][3], motorbike_list[selected_ele][4],
                        motorbike_list[selected_ele][5],
                        motorbike_list[selected_ele][6])

    total_money = veh.rent_vehicle(price)
    v_l[selected_ele][3] += total_money
    v_l[selected_ele][5] += 1
    print("Rented successfully")
    return v_l


'''
The main function has all of the program functionality when the user chooses any element of the menu, it executes it 
'''


def main(selected_item):
    global cars_list, motorbike_list

    if selected_item == "1":
        print("vehicle model   | Release date | Purchase date | Money made     | plate number   | rent times | Number "
              "of helmets")
        car_info(cars_list)
        moto_info(motorbike_list)

    elif selected_item == "2":
        print("vehicles model  | Release date | Purchase date | Money made     | plate number   | rent times |")
        car_info(cars_list)

    elif selected_item == "3":
        print("vehicle model   | Release date | Purchase date | Money made     | plate number   | rent times | Number "
              "of helmets")
        moto_info(motorbike_list)

    # count the total money
    elif selected_item == "4":
        print("vehicle model    | Money made     | rent times")
        # calling the car details function to provide a report with the details needed
        for car in cars_list:
            car_item = Car(car[0], car[1], car[2], car[3], car[4], car[5])
            print(car_item.total_money())

        for moto in motorbike_list:
            moto_item = Vehicles(moto[0], moto[1], moto[2], moto[3], moto[4], moto[5])
            print(moto_item.total_money())

    # del a car
    elif selected_item == "5":
        cars_list = delete_vehicles(cars_list)
        print("Car deleted successfully")

    # del a motorbike
    elif selected_item == "6":
        motorbike_list = delete_vehicles(motorbike_list)
        print("Motorbike deleted successfully")

    # add new car
    elif selected_item == "7":
        model, release_date, purchase_date, plate_number = add_new_vehicle()
        new_car = Car(model, release_date, purchase_date, 0, plate_number, 0)
        new_car.vehicle_info()
        cars_list.append([model, release_date, purchase_date, 0, plate_number, 0])
        new_car = Car(model, release_date, purchase_date, 0, plate_number, 0)
        print("Car added successfully")
        print("vehicles model  | Release date | Purchase date | Money made     | plate number   | rent times |")
        print(new_car.vehicle_info())

    # add new motorbike
    elif selected_item == "8":
        model, release_date, purchase_date, plate_number = add_new_vehicle()
        new_moto = Motorbike(model, release_date, purchase_date, 0, plate_number, 0, 2)
        new_moto.info()
        motorbike_list.append([model, release_date, purchase_date, 0, plate_number, 0, 2])
        new_moto = Motorbike(model, release_date, purchase_date, 0, plate_number, 0, 2)
        print("Motorbike added successfully")
        print("Motorbike model   | Release date | Purchase date | Money made     | plate number   | rent times | "
              "Number of helmets")
        print(new_moto.info())


    # rent a car
    elif selected_item == "9":
        cars_list = rent_vehicle(cars_list, 1)



    # rent a moto
    elif selected_item == "10":
        motorbike_list = rent_vehicle(motorbike_list, 0)

    # car carbon footprint
    elif selected_item == "11":
        selected_ele = vehicles_validation(cars_list)
        car_obj = Car(cars_list[selected_ele][0], cars_list[selected_ele][1], cars_list[selected_ele][2],
                      cars_list[selected_ele][3], cars_list[selected_ele][4], cars_list[selected_ele][5])
        print(car_obj.car_carbon_footprint())

    # moto carbon footprint
    else:
        selected_ele = vehicles_validation(motorbike_list)
        moto_obj = Motorbike(motorbike_list[selected_ele][0], motorbike_list[selected_ele][1],
                             motorbike_list[selected_ele][2], motorbike_list[selected_ele][3],
                             motorbike_list[selected_ele][4], motorbike_list[selected_ele][5],
                             motorbike_list[selected_ele][6])
        print(moto_obj.moto_carbon_footprint())

menu()

print("---------------------------------------------------------------------------------------------------------------")
run_again = input("Do you want another operation? (type 1 for yes) ")
while run_again == '1':
    menu()
    print(
        "-------------------------------------------------------------------------------------------------------------")
    run_again = input("Do you want to run again? (type 1 for yes) ").lower()
