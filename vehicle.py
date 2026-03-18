class Vehicle:
    def __init__(self, vin, make, model, daily_rate):
        # Initialize properties
        self.vin = vin
        self.make = make
        self.model = model
        self.daily_rate = daily_rate
        self.available = True
    
    def start_rental(self):
        # Check if the vehicle is available
        if self.available:
            # If available, set self.available to False and return True
            self.available = False
            return True
        # If not available, return False
        else:
            return False
    
    def end_rental(self):
        # Set self.available to True
        self.available = True
        # Return True to indicate successful completion
        return True
    
    def __str__(self):
        # Create a status string based on self.available ("Available" or "Not Available")
        status = "Available" if self.available else "Not Available"
        # Return a formatted string 
        return f"{self.make} {self.model} (VIN: {self.vin}) - {status}"


