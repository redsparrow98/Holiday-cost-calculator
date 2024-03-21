#================   Functions   ================

def city_list():
    """Prints out the cities that a customer can choose from"""
    print("Our choice of cities for the season:")
    print("We only offer up to 10 days stay!")
    for key in costs_list["cities"]:
        print(key)

def hotel_cost(no_nights):
    """takes the number of nights input by the user and returns the 
    hotel_cost value of that amount of nights, if the nights are over what the agency offers
    it lets the user know"""
    return costs_list["hotel day"][no_nights]

def plane_cost(city):
    """takes the city input from use and returns the plane_cost value of flight for that
    city, if the city is not in the offer it lets the user know"""
    return costs_list["cities"][city]

def car_rental(no_days):
    """takes the number of car rental days input by the user and returns the 
    car_rental value of that amount of days, if the days are over what the agency offers
    it lets the user know"""
    return costs_list["car days"][no_days]

def holiday_cost(hotel, plane, car):
    """gets all the costs of the hotel, flight and car and sums it all together
    then prints out the cost of each item and the final sum cost of the holiday"""
    total_cost = hotel + plane + car
    print(f"the flight cost: £{plane}\nThe hotel cost: £{hotel}\nThe car cost: £{car}")
    print(f"The total holiday cost is: £{total_cost}")

#================   Final Code   ================

# a dictionary of all the prices and offers the agency does

costs_list = {
    "cities": 
    {
        "Amsterdam": 100,
        "Berlin": 50,
        "Paris": 75,
        "Prague": 68,
        "Rome": 70,    
    },
    "car days":
    {
        "0": 0,
        "1": 10,
        "2": 15,
        "3": 20,
        "4": 25,
        "5": 30,
        "6": 35,
        "7": 40,
        "8": 45,
        "9": 50,
        "10": 55,
    },
    "hotel day":
    {
        "0": 0,
        "1": 30,
        "2": 50,
        "3": 70,
        "4": 90,
        "5": 110,
        "6": 130,
        "7": 150,
        "8": 170,
        "9": 190,
        "10": 210,
    },
}

# initialise the program and print out the cities that the user can choose from
print("Welcome to holiday cost calculator")
print("We offer up 10 day packages!")
city_list()

# Sets up a variable for the while loop to be changed when the condition is met
city_on_list = False

# Sets up a condition for a while loop
while city_on_list is False:
    # Tries to take user input for the city by calling ask_city func tries to get the plane cost with user input if user input is not in the dictionary it produces a KeyError in which case it loops trough requesting the input again until the city is in the dictionary then it exits the loop
    try:
        city_flight = input("What city are you flying to?: ").title()
        # Calls the plane_cost func and stores the result in to flight variable
        flight = plane_cost(city_flight)
        city_on_list = True
    except KeyError:
        print("We dont offer that city")

# Sets up a variable for the while loop to be changed when the condition is met
nights_in_offer = False

# Sets up a condition for a while loop
while nights_in_offer is False:
    # Tries to take user input for the nights of stay by calling ask_night func tries to get the hotel cost with user input if user input is not in the dictionary it produces a KeyError in which case it loops trough requesting the input again until the number of nights is in the dictionary the it exits the loop
    try:
        num_nights = input("How many nights are you staying? (1-10): ")
        # Calls the hotel_cost func and stores the result in to nights variable	
        nights = hotel_cost(num_nights)
        nights_in_offer = True
    except KeyError:
        print("We dont offer that many nits")

# Sets up a variable for the while loop to be changed when the condition is met
car_days_in_offer = False

# Sets up a coition for a while loop
while car_days_in_offer is False:
    # Tries to take user input for the days of car rental by calling ask_car_days func tries to get the car rental cost with user input if user input is not in the dictionary it produces a KeyError in which case it loops trough requesting the input again until the number of days is in the dictionary then it exits the loop
    try:
        rental_days = input("How many days are you renting a car for?(1-10): ")
        # Calls the car_rental func and stores the result in to days variable
        days = car_rental(rental_days)
        car_days_in_offer = True
    except KeyError:
        print("We dont offer that many days for the car")

# call on to the holiday function and enters the variables that have been calculated
# while asking for user input for each section
holiday_cost(plane= flight, hotel= nights, car=days)