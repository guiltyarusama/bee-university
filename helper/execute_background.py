import asyncio
from concurrent.futures import ThreadPoolExecutor
import time


def execute_background(max_worker, job):
    executor = ThreadPoolExecutor(max_workers=max_worker)
    loop = asyncio.get_event_loop()
    boo = asyncio.ensure_future(loop.run_in_executor(executor, job))
    # loop.run_forever()
    # loop.close()


def test():
    time.sleep(2)
    print('hihi')


def example():
    execute_background(max_worker=5, job=test)
    print('done')

# example()
