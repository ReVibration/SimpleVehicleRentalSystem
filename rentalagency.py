class RentalAgency:
    def __init__(self, name):
        # Initialize properties
        self.name = name
        self.vehicles = {}  # Dictionary to store vehicles (key: VIN, value: Vehicle object)
        self.rentals = {}   # Dictionary to store rentals (key: rental_id, value: Rental object)
        self.next_rental_id = 1
    
    def add_vehicle(self, vehicle):
        # Add the vehicle to the vehicles dictionary using its VIN as the key
        self.vehicles[vehicle.vin] = vehicle
        # Return True to indicate successful completion
        return True
    
    def rent_vehicle(self, vin, customer_name, days):
        # Check if the vehicle with the given VIN exists in self.vehicles
        if vin in self.vehicles.keys():
            # Get the vehicle object from self.vehicles
            vehicle = self.vehicles[vin]
            # Check if the vehicle is available
            if vehicle.available():
                # Create a rental_id string in the format "R{self.next_rental_id}"
                rental_id = "R{self.next_rental_id}"
                # Increment self.next_rental_id
                self.next_rental_id += 1
                # Create a new Rental object with the rental_id, vehicle, customer_name, and days
                rental = Rental(rental_id,vehicle,customer_name,days)
                # Call the vehicle's start_rental method
                vehicle.start_rental()
                # Add the rental to self.rentals using rental_id as the key
                self.rentals[rental_id] = rental
                # Return the rental_id
                return rental_id
            else:
                # If not available, return None
                return None
        else:
            # If not, return None
            return None  
    
    def return_vehicle(self, rental_id):
        # Check if the rental with the given rental_id exists in self.rentals
        if rental_id in self.renatls.key():
            # Get the rental object from self.rentals
            rental = self.rentals[rental_id]
            # Check if the rental is active
            if rental.active:
                # Call the rental's end_rental method and return its result
                return rental.end_rental()
            else:
                # If not active, return False
                return False
        else:
            # If not, return False
            return False
    
    def available_vehicles(self):
        # Return a list of all vehicles in self.vehicles.values() where vehicle.available is True
        return [vehicle for vehicle in self.vehicles.values() if vehicle.available]
        new_list = [expression for item in iterable if condition]



