import os 
from multiprocessing import Process #, Queue

# All processes call the same function

def doubler(number):
    result = number * 2
    process = os.getpid()

    print(f"Process ID: {process} doubled {number} to {result}")

if __name__ == "__main__":
    numbers = [0,1,2,3,4,5]
    processes = []

    for i, number in enumerate(numbers):
        p = Process(target=doubler, args=(number,)) # Function name and arguments
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

"""
From output: All processes are running in parallel but there is no guarantee on thier ordering/ sequence.
"""