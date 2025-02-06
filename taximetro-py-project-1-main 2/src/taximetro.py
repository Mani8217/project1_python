class TaxiMeter:
    
    # Initial Attributes
    def __init__(self , total_cost = 0 , start_time = None , is_moving = False):
        self.total_cost = total_cost
        self.start_time = start_time
        self.is_moving = is_moving
        
    # Methods
    def start_trip(self):
        self.start_time = time.time()
        self.total_cost = 0.0
        print("trip started")
        
    def stop_trip(self):
        trip_time = time.time() - self.start_time
        self.total_cost = trip_time * 0.02
        print(f"the trip is over and the total cost is: {self.total_cost}")
        
    def moving_state(self):
        self.is_moving = True
        print("state : moving..")
    
    def stop_state(self):
        self.is_moving = False
        print("state: : stopped")
        
        
 