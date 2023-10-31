## Code with threading
import threading
import time

start = time.perf_counter()
def doSomething():
    print('Sleep 1 sec')
    time.sleep(1)
    print('Done')

doSomething()
doSomething()
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 3)} secs')