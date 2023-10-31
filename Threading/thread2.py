## Code with threading
import threading
import time

start = time.perf_counter()
def doSomething():
    print('Sleep 1 sec')
    time.sleep(1)
    print('Done')

t1 = threading.Thread(target=doSomething)## dont put the()
t2 = threading.Thread(target=doSomething)## dont put the()

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 3)} secs')