# You are tasked with building a Vehicle Rental Management System to help a car rental company manage different types of vehicles (Cars and Bikes) and 
# calculate their rental charges for billing purposes. 
# Requirements:

# 1. Create a base class Vehicle to store common vehicle details.
# Attributes (protected, not private):
#      _vehicle_id: A string representing the unique vehicle identifier (e.g., "CAR001", "BIKE001").
#      _base_rate: A float representing the base daily rental rate (e.g., 100.00).
# Include a constructor to initialize _vehicle_id and _base_rate.
# Provide a method display_details() to return a string with the vehicle ID and base rate.
# Include a method rental_charge() that returns a placeholder value (0.0) to be overridden by subclasses.x

class Vehicle:
    def __init__(self,vehicleId,baseRate):
        self._vehicle_id = vehicleId
        self._base_rate = baseRate
    def display_details(self):
        return f"Vehicle Id: {self._vehicle_id}, Base Rate: {self._base_rate}"
    def rental_charge(self):
        return 0.0

# 2. Create a subclass Car that inherits from Vehicle:
#     Add an attribute num_seats (integer, e.g., 4 for a sedan).
#      Override the rental_charge() method to calculate the daily rental charge as _base_rate * num_seats.

class Car(Vehicle):
    def __init__(self,vehicleId,baseRate,numSeats):
        Vehicle.__init__(self,vehicleId,baseRate)
        self.num_seats = numSeats
    def rental_charge(self):
        return f"the daily rental charge : {self._base_rate * self.num_seats}"


# 3. Create a subclass Bike that inherits from Vehicle:
#      Add an attribute bike_type (string, e.g., "Scooter", "Motorcycle").
#      Override the rental_charge() method to calculate the daily rental charge as _base_rate * 0.5.
class Bike(Vehicle):
    def __init__(self, vehicleId, baseRate,bikeType):
        Vehicle.__init__(self,vehicleId,baseRate)
        self.bike_type = bikeType
    def rental_charge(self):
        return f"the daily rental charge : {self._base_rate * 0.5 }"


#4.  Write a function calculate_rental that accepts a Vehicle object and calls its rental_charge() method to return the rental charge. 
# This demonstrates polymorphism by working with any vehicle type

def calculate_rental(vehicle: Vehicle):
    return vehicle.rental_charge()

car1 = Car("CAR001", 100.0, 4)
bike1 = Bike("BIKE001", 100.0, "Scooter")

print(car1.display_details())  
print("Car Rental Charge:", calculate_rental(car1))

print(bike1.display_details())  
print("Bike Rental Charge:", calculate_rental(bike1))