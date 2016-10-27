# coding: UTF-8

import signal
import sys

def destroy(signum, frame):
    print ('destroy is called')
    raise

signal.signal(signal.SIGHUP, destroy)
signal.signal(signal.SIGTERM, destroy)
signal.signal(signal.SIGINT, destroy)

def main():
    while True:
        pass

if __name__ == '__main__':
    main()

