## Code with threading
import threading
import time
import concurrent.futures

start = time.perf_counter()
def doSomething(secs):
    print(f'Sleep {secs} sec')
    time.sleep(secs)
    return 'Done.....'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(doSomething,1)
    print(f1.result())

# threads=[]
# for _ in range(10):
#     t = threading.Thread(target=doSomething,args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 3)} secs')