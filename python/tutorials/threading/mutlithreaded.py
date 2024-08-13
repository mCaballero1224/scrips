#!/usr/bin/python

# Source: https://www.pythontutorial.net/python-concurrency/python-threading/

from time import sleep, perf_counter
from threading import Thread


def task(id: int):
    print(f'Starting task (id: {id})...')
    sleep(1)
    print(f'Task {id} completed...')


start_time = perf_counter()

threads = []  # array to hold threads

# create new threads
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)  # add thread to array and start
    t.start()

# wait for the threads to complete
for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')
