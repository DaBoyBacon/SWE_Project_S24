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
