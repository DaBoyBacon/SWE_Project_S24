import sched, time
class APILimiter:
    incCt = 0

    def __init__(self):
        interval = 60
        self.my_scheduler = sched.scheduler(time.time, time.sleep)
        self.my_scheduler.enter(interval, 1, self.reset, (self.my_scheduler,))
        self.my_scheduler.run()

    def reset(self, scheduler): 
        # schedule the next call first
        scheduler.enter(60, 1, self.reset, (scheduler,))
        print("Doing stuff...")
        self.incCt = 0
        # then do your stuff

    def incCt(self):
        self.incCt = self.incCt + 1
        
    def getinc(self):
        return self.incCt
        
    