import threading

class AuthTimer:
    
    #Literally will never run. This avoids the "t doesn't exist" bs
    def nothin(self):
        print("literally nothing")

    #IncrVal goes up with every API Call
    incrVal = 0
    #max IncrVal
    maxIncrVal = 60
    #Interval is how many seconds before clearing incrVal
    interval = 60

    #t is the threading timer
    t = threading.Timer(interval, nothin)

    #Resets the incrVal
    def reset(self): 
        # Do the stuff
        #print("Resetting inc...") #debugging
        self.incrVal = 0
        
        #then reschedule (and re-start) the timer
        self.t = threading.Timer(self.interval, self.reset)
        self.t.start()

    #Initialize our timer
    def __init__(self):
        self.incrVal = 0
        self.maxIncrVal = 60
        self.interval = 60
        self.reset()
        
    #Getter for incrVal
    '''Returns the # of api calls made in the last minute
        Returns:
            incrementValue (int): Int value of # of calls made in the minute
    '''
    def getInc(self) -> int:
        return self.incrVal
    
    #If incrval < 60 every min, then True; if no more API allowed in the minute, return False
    '''Returns True or false wether another API call can be made
        Returns:
            #incrementValue < 60 ? Y: True ; N: False
    '''
    def canInc(self) -> bool:
        if self.incrVal < self.maxIncrVal: 
            self.incrVal = self.incrVal+1
            return True
        else:
            return False
    
