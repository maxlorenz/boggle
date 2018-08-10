"""Simple stop watch class"""
import time


class StopWatch(object):
    "Measures seconds, can be started and checked"

    def __init__(self, runtime_seconds):
        self.start_time = 0
        self.runtime_seconds = runtime_seconds

    def start(self):
        "Start the timer"
        self.start_time = time.time()

    def seconds_left(self):
        "Returns time left in seconds"
        return self.runtime_seconds - (time.time() - self.start_time)

    def check(self):
        "Returns True if start() was called less then the allowed time ago"
        return self.seconds_left() <= self.runtime_seconds
