## Code with threading
import threading
import time

start = time.perf_counter()
def doSomething(secs):
    print(f'Sleep {secs} sec')
    time.sleep(secs)
    print('Done')

threads=[]
for _ in range(10):
    t = threading.Thread(target=doSomething,args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 3)} secs')