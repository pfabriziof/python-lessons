import time
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

def do_work(num: int, duration: float = 0.1) -> str:
    """Simulate an I/O bound task.

    Simulates a task that depends on waiting for a response (I/O)
    rather than heavy calculations (CPU)
    """
    time.sleep(duration)
    return f"Task {num} completed"

def do_computation(num: int, iterations: int = 1000000) -> str:
    """Simulate a CPU bound task.

    Simulates a task that depends on heavy CPU operations rather than
    waiting por something to return a response.
    """
    result: int = 0
    for i in range (iterations):
        result += i * i
    return f"Task {num} completed (result: {result})."

async def do_async_work(num: int, duration: float = 0.1) -> str:
    await asyncio.sleep(duration)
    return f"Task {num} completed"


def run_sync(tasks: int) -> list[str]:
    results: list[str] = []
    for i in range(tasks):
        result = do_work(num=i, duration=0.1)
        results.append(result)
    return results

def run_threading(tasks: int, max_workers: int = 5) -> list[str]:
    """Execute tasks with threads.

    Executes I/O-bound tasks on multiple threads. So if a thread
    is idle while waiting for a task to be completed, other
    threads will work on the rest of the tasks.
    """
    results: list[str] = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_work, i, 0.1) for i in range(tasks)]

    for future in as_completed(futures):
        results.append(future.result())
    return results

def run_multiprocessing(tasks: int, max_workers: int = 5) -> list[str]:
    """Execute tasks with multiprocessing

    Executes CPU-bound tasks on multiple processes. Each process has its
    own memory space, which means you can't easily share variables between
    processes (you would need to use special mechanism like queues or shared
    memory). The benefit is that here you use true parallelism.
    """
    results: list[str] = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_computation, i, 1000000) for i in range (tasks)]

    for future in as_completed(futures):
        results.append(future.result())
    return results

async def run_asyncio(tasks: int) -> list[str]:
    """Run tasks with modern I/O-bound approach

    Runs tasks with the modern approach for I/O-bound work. It uses a single
    thread, futures and a scheduled event loop. Most of the time, this is
    preferable to use than multithreading as asyncio is more efficient and
    scalable.
    """
    task_list = [do_async_work(i, 0.1) for i in range(tasks)]
    results = await asyncio.gather(*task_list)
    return list(results)

if __name__ == "__main__":
    start_time = time.perf_counter()
    results = run_sync(tasks=5)
    elapsed_time = time.perf_counter() - start_time
    print("="*70)
    print("Synchronous results:")
    for result in results:
        print(f"  {result}")
    print(f"\nTotal time: {elapsed_time: .2f} seconds")
    print("Note: Tasks ran one after another (synchronous execution)\n")


    start_time = time.perf_counter()
    results = run_threading(tasks=5)
    elapsed_time = time.perf_counter() - start_time
    print("="*70)
    print("Threading results:")
    for result in results:
        print(f"  {result}")
    print(f"\nTotal time: {elapsed_time: .2f} seconds")
    print("Note: Tasks ran in concurrently using threads (I/O-bound tasks)\n")


    start_time = time.perf_counter()
    results = run_multiprocessing(tasks=5)
    elapsed_time = time.perf_counter() - start_time
    print("="*70)
    print("Multiprocessing results:")
    for result in results:
        print(f"  {result}")
    print(f"\nTotal time: {elapsed_time: .2f} seconds")
    print("Note: Tasks ran in parallel using processes (CPU-bound tasks)\n")


    start_time = time.perf_counter()
    results = asyncio.run(run_asyncio(tasks=5))
    elapsed_time = time.perf_counter() - start_time
    print("="*70)
    print("AsyncIO results:")
    for result in results:
        print(f"  {result}")
    print(f"\nTotal time: {elapsed_time: .2f} seconds")
    print("Note: Tasks ran in a single thread with AsyncIO (Modern I/O-bound approach)\n")
