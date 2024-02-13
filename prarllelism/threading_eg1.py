from concurrent.futures import ThreadPoolExecutor as Executor

import time
def worker(data):
    time.sleep(1)

with Executor(max=10) as exce:
    pass