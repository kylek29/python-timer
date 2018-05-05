# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:23:55 2018

@author: kylek
"""

import time


class Timer(object):
    """
    Simple timer object that allows you to start and stop a timer counter. Uses
    the time.time() unix time value to create timer intervals.
    
    Basic Usage:  
        object_name.start() --> Starts a timer interval.
        object_name.stop() --> Stops a timer interval, stores value.
        object_name.timer() --> Returns the current sum of all timers.
            
    """
    
    stored_time = []
    last_timer = None
    start_time = 0
    active = 0
    
    def __init__(self):
        pass
    
    
    def __repr__(self):
        """ Returns the value of timer() """
        return str(self.timer())
    
    
    def start(self):
        """ Stores the current start time. Sets timer to active. """
        if not self.active:
            self.active = 1
            self.start_time = time.time()
        
        
    def stop(self):
        """ Stores current time from start_time in stored_time. """
        if self.active:
            self.stored_time.append(time.time() - self.start_time)
            self.active = 0
            self.start_time = 0
        
        
    def reset(self):
        """ Blanks the stored_time list, sets start_time and active to 0. """
        if self.active:
            self.stop()
        self.last_timer = sum(self.stored_time)
        self.stored_time = []
        self.active = 0
        self.start_time = 0
        
        
    def interval(self):
        """ Returns the current active timer interval value. """
        if self.active:
            return time.time() - self.start_time
        else:
            return "No currently running timer."
    
    
    def timer(self):
        """ Returns the sum of the entire timeset, including any currently running interval. """
        if self.active:
            curr_timer = time.time() - self.start_time
        else:
            curr_timer = 0
        return curr_timer + sum(self.stored_time)
    
    


if __name__ == "__main__":
    times = Timer()
    
    print('Start Timer')
    times.start()
    time.sleep(5) # Sleep for 5 seconds
    times.stop()
    print('Timer Stopped: Sum of all times: {}'.format(times))
    
    print('Start Timer')
    times.start()
    time.sleep(3)
    times.stop()
    print('Stop Timer')
    print('Timer Stopped: Sum of all times: {}'.format(times))
    
    print('Start Timer')
    times.start()
    time.sleep(3)
    print('Current active interval: {}'.format(times.interval()))
    time.sleep(2)
    print('Current active interval: {}'.format(times.interval()))
    time.sleep(2)
    times.stop()
    print('Stop Timer')
    print('Sum of ALL times: {}'.format(times.timer()))
    print('Should be approximately 5s + 3s + 7s = 15s')
    
    
    # Timer --- 
    # .start --> Starts a timer (stores the current unix time)
    # .stop --> Stops a timer (takes current time, subtracts the stored time, and puts it into a list element)
    # .reset --> Blanks the STORED TIME list elements.
    # .time --> Gets the current timer value.
    # print() .. same as .time
    
    
