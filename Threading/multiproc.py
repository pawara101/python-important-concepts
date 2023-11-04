## Code with multiprocessing
import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print('Sleep 1 second')
    time.sleep(1)
    print('Done Sleeping....')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

## To run
p1.start()
p2.start()

## Processes will finish then move to below lines
p1.join()
p2.join()

finish = time.perf_counter()

print(f'Completed in {round(finish-start,2)} s')