import timer

timer.start()

for i in range(100000):
    i = i*i

time = timer.stop()
print(time)