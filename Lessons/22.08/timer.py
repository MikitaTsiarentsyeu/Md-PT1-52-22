import time

isStarted = False

def start():
    global start_time
    global isStarted
    isStarted = True
    start_time = time.time()

def stop():
    global isStarted
    if isStarted:
        res = time.time()-start_time
        isStarted = False
        return res
