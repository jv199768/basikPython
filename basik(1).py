import concurrent.futures
import time
import random

def task(name):
    print(f' Task {name} starting')
    sleep_time = random.randint(1, 5)
    time.sleep(sleep_time)
    print(f' Task {name} name completed after {sleep_time} seconds')
    return sleep_time

    with concurrent.futures.ThreadPoolExecutor(max_works=3) as executor:
        future_to_task = {executor.submit(task, i): i for i in range(5)}
       
        for future in concurrent_future_as_completed(future_to_task):
            task_name = future_to_task[future]
           
            try:
                result = future.result()
                print(f"Task{task_name} name completed successfully with result {result}")
            except Exception as e:
                print(f"Task{task_name} generated an exception: {e}")
print(task(3))
