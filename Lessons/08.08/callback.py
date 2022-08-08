import time, threading

def show_text():
    print("showing some ad here")

def show_symbols():
    print("@@#$$%%^&&**()))(*&^%$#@#$%^&*&^%$#@")

def timer(t, count, callback):
    while count:
        callback()
        time.sleep(t)
        print(f"sleeping for {t} seconds")
        count -= 1

def threading_timer(t, count, callback):
    while count:
        threading.Timer(t, callback).start()
        print(f"sleeping for {t} seconds")
        count -= 1

# timer(3, 10, show_symbols)
threading_timer(1, 1000, show_symbols)