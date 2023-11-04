## Code with multiprocessing
import time
import multiprocessing

## context
import concurrent.futures

start = time.perf_counter()

def do_something(tm):
    print(f'Sleep {tm} second')
    time.sleep(tm)
    return 'Done sleep'

with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something,1)
    f2 = executor.submit(do_something,2)
    print(f1.result())
    print(f2.result())

# process =[]
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something,args=[1.5])
#     p.start()
#     process.append(p)

# for procs in process:
#     procs.join()

finish = time.perf_counter()

print(f'Completed in {round(finish-start,2)} s')