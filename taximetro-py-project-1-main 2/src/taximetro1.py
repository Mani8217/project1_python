import time 

class Taximeter:

    def __init__(self , total_cost = 0 , trip_active = False , last_time = None):
        self.total_cost = total_cost
        self.trip_active = trip_active
        self.last_time = last_time

    def start_trip(self):
        # start a trip
        if self.trip_active:
            time.sleep(2)
            print("new trip is started , please reset the Taximeter")

            return  
        print("""
                 .--------.
                / .------. \\
               | /        \\ |
               | |  TAXI  | |
           ____| |________| |____
          '-----(o)------(o)-----'
           """)    
        self.total_cost = 0 
        self.trip_active = True 
        self.last_time = time.time() 
        print("trip starts")
           

    def update_cost(self, moving=True):
        # update the fare according to time
        if not self.trip_active:
            print("The trip is not active")
            return
        
        now_time = time.time()
        passed_time = now_time - self.last_time  # calculate passed time
        self.last_time = now_time # determine new time

        rate = 0.05 if moving else 0.02 
        self.total_cost += passed_time * rate

    def stop_trip(self):
        # trip is finished , show the cost
        if not self.trip_active:
            print("there is no trip to be stopped")
            return

        self.update_cost(moving = False) # last calculation befor stop
        self.trip_active = False
        print(f"🚕 trip is ended and the fare is: {self.total_cost:.2f} Euro ")




taxi = Taximeter()

while True:
    command = input("\n Your order (start, move, stop, exit): ").strip().lower()

    if command == "start":
        taxi.start_trip()
    elif command == "move":
        taxi.update_cost(moving=True)
        print(f"💨 current cost: {taxi.total_cost:.2f} Euro ")
    elif command == "stop":
        taxi.stop_trip()
    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("⛔ undefined order , please try again")
