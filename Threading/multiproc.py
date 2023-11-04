## Code with multiprocessing
import time
import multiprocessing

## context
import concurrent.futures

start = time.perf_counter()

def do_something(tm):
    print(f'Sleep {tm} second ====')
    time.sleep(tm)
    return 'Done sleep'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,sec)for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
# process =[]
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something,args=[1.5])
#     p.start()
#     process.append(p)

# for procs in process:
#     procs.join()

finish = time.perf_counter()

print(f'Completed in {round(finish-start,2)} s')