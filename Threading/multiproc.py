## Code with multiprocessing
import time
import multiprocessing

start = time.perf_counter()

def do_something(tm):
    print(f'Sleep {tm} second')
    time.sleep(tm)
    print('Done Sleeping....')

process =[]
for _ in range(10):
    p = multiprocessing.Process(target=do_something,args=[1.5])
    p.start()
    process.append(p)

for procs in process:
    procs.join()


finish = time.perf_counter()

print(f'Completed in {round(finish-start,2)} s')