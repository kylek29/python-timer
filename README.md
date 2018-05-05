# python-timer
Timer Object for Python to easily track duration. Made for a wider project as a learning experiment.


#USAGE:

The class stores the UNIX time (in seconds) at time of being called with .start() method (not initialization) and will give back the current time since then when prompted (duration). Usage case scenario would be if you're doing a lot of timers for a RaspberryPI script (e.g. LED) and don't want to use sleep delays.

If you want a singular timer object that can be started and stopped (paused) linearly, just use one timer object. If you need 
multiple timers that have differing start/stops (overlapping), create multiple objects, like:
timer_A = Timer()
timer_B = Timer()

You can reset the timer object with object_name.reset(). The last sum of timer intervals will be stored in object_name.last_timer for future referencing.


# Methods
.start --> Starts a timer (stores the current unix time)
.stop --> Stops a timer (takes current time, subtracts the stored time, and puts it into a list element)
.reset --> Blanks the STORED TIME list elements.
.time --> Gets the current timer value.
print() .. same as .time
