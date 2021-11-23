#!/usr/bin/env python3
"""The main controller of the ground station.

TODO:
- Read in config?
- Set up sat tracking
"""

import time
import signal
import sys


class GroundStation():
    def __init__(self):
        self.running = False
        signal.signal(signal.SIGINT, self.clean_up)
        signal.signal(signal.SIGTERM, self.clean_up)

    def start(self):
        self.running = True

        self.run()

    def clean_up(self, signal, frame):
        print("Cleaning up")
        sys.exit(0)

    def run(self):
        while(self.running):
            print("Running")
            time.sleep(1)
