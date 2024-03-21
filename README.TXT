#===============  functions use  =================
create a function to initialize the offer list for cities

create functions for calculating costs of flight/hotel/car
that take user inputs as arguments
plane_cost(city)
hotel_cost(nights)
car_cost(days)

create a function to calculate the full cost of holiday and Prints
out the individual parts cost as well as the total_cost
holiday_cost()


Create a dictionary with menu of
cities/hotel/car options and prices

=================== Functionality of the code ===============

Prints out options that the user can choose from

requests user input for city
it stores input to a flight variable
calls on to the plane_cost() using flight variable as an argument to get price of flight
if the user enters an input that isn't in the offer
system lets the user know and requests input again

requests user for input for nights of stay in hotel
it stores input to a nights variable
calls on to the hotel_cost() using nights variable as an argument to get price of hotel
If the user input is not in the dictionary the program
lets the user know and requests input again

requests user for input for days of car rental
it stores input in to days variable
calls on to the car_cost() using days variable as an argument to get price of hotel
then stores it in to 
If the user input is not in the dictionary the program
lets the user know and requests input again

calls on to the holiday_cost() and inputs the variables for each section(flight/nights/days)
as arguments
prints out cost of each aspect and final cost of holiday