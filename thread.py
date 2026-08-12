import threading
import time

sem = threading.Semaphore(3)

def task(number):
    with sem:
        print("Thread", number, "entered")
        time.sleep(2)
        print("Thread", number, "leaving")

threads = []

for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished")