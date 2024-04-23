<<<<<<< HEAD
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
        
    
=======
import threading
import time


class Timer(threading.Thread):

    def __init__(self):
        self._timer_runs = threading.Event()
        self._timer_runs.set()
        super().__init__()

    def run(self):
        while self._timer_runs.is_set():
            self.timer()
            time.sleep(self.__class__.interval)

    def stop(self):
        self._timer_runs.clear()

class someTimer(Timer):
    interval = 60
    inc = 0    
    def __init__(self):
        self.inc = 0
        self.interval = 60

    #func to ex
    def timer(self):
        print("Clear inc:" + self.inc)
        self.inc = 0
        
    def inc(self):
        self.inc = self.inc + 1
        
    def caninc(self) -> bool:
        return True  if self.inc<60 else False

    def getinc(self):
        return self.inc
>>>>>>> fa9bebe213e8349a7337ac6a4c4dd263b62b5854
