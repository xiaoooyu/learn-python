# we have 100 cars
cars = 100

# each car carry 4 passengers
space_in_a_car = 4.0

# we have 30 drivers
drivers = 30

# 90 passengers supposed
passengers = 90

# so how many cars do not have driver
cars_not_driven = cars - drivers

# and how many cars do have driver
cars_driven = drivers

# how many capacity do we have so far
carpool_capacity = cars_driven * space_in_a_car

# average passengers in each car 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaiable.";
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transpot", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."