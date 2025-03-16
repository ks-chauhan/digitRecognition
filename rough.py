from timeit import default_timer
import time
import multiprocessing
start_time=default_timer()
def do_something():
    print("sleeping for 1 second")
    time.sleep(1)
    print("done sleeping")
do_something()
end_time=default_timer()
print(f"finished sleeping in {round(end_time-start_time)} seconds")