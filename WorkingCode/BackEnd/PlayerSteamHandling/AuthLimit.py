import threading    

class AuthLimiter:
    num = 0
    timer = 0
    
    def __init__(self):
        self.StartTimer()

    def inc(self):
        self.num += 1
        
    def StartTimer(self):
        self.timer = threading.Timer(60, self.ClearNum())
        self.timer.start()
        #do stuff

    def ClearNum(self):
        self.num = 0
        print("Resetting the counter")
        
    def CanCall(self):
        if (self.num < 60):  return True
        else: return False
        
c = AuthLimiter()
c.inc()
c.inc()