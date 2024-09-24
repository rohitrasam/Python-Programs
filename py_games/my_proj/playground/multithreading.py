import time

""" Older way """
# from threading import Thread
# def do_something(seconds: int):
#     print(f"Sleeping for {seconds} sec(s)")
#     time.sleep(seconds)
#     print(f"Done sleeping for {seconds} sec(s)...")

# start = time.perf_counter()

# threads = []

# for second in range(5, 0, -1):
#     t = Thread(target=do_something, args=[second])
#     t.start()
#     threads.append(t)
#     # not using join immediately because it would result in the same output as running the program w/o thread

# # Instead run join separately
# for thread in threads:
#     thread.join()

# end = time.perf_counter()
# print(f"Finished in {round(end-start, 2)} sec(s)")


""" Newer way """
# from concurrent.futures import ThreadPoolExecutor, as_completed

# def do_something(seconds: int) -> str:
#     print(f"Sleeping for {seconds} sec(s)")
#     time.sleep(seconds)
#     return f"Done sleeping for {seconds} sec(s)..."

# start = time.perf_counter()

# with ThreadPoolExecutor() as exec:    # Context manager
#     # results = [exec.submit(do_something, second) for second in range(5, 0, -1)]
    
#     # for f in as_completed(results):
#     #     print(f.result())

#     secs = list(range(5, 0, -1))
#     # """ map returns result in the order that they were started and not like the submit() """
#     results = exec.map(do_something, secs)  # runs the func with every value in the 2nd arg and it returns the result and not the Future object
#     # for f in results:
#     #     print(f.result())
    
#     [print(result) for result in results]

# end = time.perf_counter()

# print(f"Finished in {round(end-start, 2)} sec(s)")

from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed

def makeCoffee():
    print("Adding coffee...")
    time.sleep(1)
    print("Adding milk...")
    time.sleep(1)
    print("Blending coffee")
    time.sleep(2)
    print("Coffee is readyy!!")

def cookEggs():
    print("Heat pan...")
    time.sleep(2)
    print("Spread butter...")
    time.sleep(1)
    print("Break egg...")
    time.sleep(1)
    print("Cooking egg...")
    time.sleep(3)
    print("Egg is ready!!!")

start = time.perf_counter()

t1 = Thread(target=cookEggs)
t2 = Thread(target=makeCoffee)

t1.start()
t2.start()
t1.join()
t2.join()

# with ThreadPoolExecutor() as exec:
#     f1 = exec.submit(makeCoffee)
#     f2 = exec.submit(cookEggs)

#     for f in as_completed([f1, f2]):
#         print(f.result())

end = time.perf_counter()
    
print(f"Finished making breakfast in {round(end - start, 2)} sec(s)")
    