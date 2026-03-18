class Rental:
    def __init__(self, rental_id, vehicle, customer_name, days):
        # Initialize properties
        self.rental_id = rental_id
        self.vehicle = vehicle
        self.customer_name = customer_name
        self.days = days
        self.is_active = True
    
    def calculate_cost(self):
        # Calculate and return the total cost by multiplying
        # the vehicle's daily_rate by the number of days
        return self.vehicle.daily_rate * self.days 
    
    def end_rental(self):
        # Check if the rental is active (self.is_active is True)
        if self.is_active == True:
            # If active, set self.is_active to False
            self.is_active = False
            # Call the vehicle's end_rental method
            self.vehicle.end_rental()
            # Return True to indicate successful completion
            return True
        else:
            # If not active, return False
            return False
    
    def __str__(self):
        # Create a status string based on self.is_active ("Active" or "Completed")
        status = "Active" if self.is_active == True else "False"
        # Return a formatted string in the format
        return f"Rental {self.rental_id}: {vehicle.make} {vehicle.model} for {self.customer_name} - {status}"
        

