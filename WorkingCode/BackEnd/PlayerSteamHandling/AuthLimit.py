import threading, time

class AuthTimer:
    
    #Literally will never run. This avoids the "t doesn't exist" bs
    def nothin(self):
        print("literally nothing")

    #IncrVal goes up with every API Call
    incrVal = 0
    #Interval is how many seconds before clearing incrVal
    interval = 60

    #t is the threading timer
    t = threading.Timer(interval, nothin)

    #Resets the incrVal
    def do_something(self): 
        # Do your stuff
        print("Resetting inc...")
        self.incrVal = 0
        
        #then reschedule (and re-start) your timer
        self.t = threading.Timer(self.interval, self.do_something)
        self.t.start()

    #Initialize our timer
    def __init__(self):
        self.incrVal = 0
        self.interval = 60
        self.do_something()
        
    #Getter for incrVal
    def getinc(self):
        return self.incrVal
    
    #If incrval < 60 every min, then True; if no more API allowed in the minute, return False
    def canInc(self):
        return True if self.incrVal < 60 else False
    
    # increments incrVal
    def inc(self):
        self.incrVal += 1
    
