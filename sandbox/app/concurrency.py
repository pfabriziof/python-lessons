import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def do_work(num: int, duration: float = 0.1) -> str:
    """Simulate an I/O bound task.

    Simulates a taks that depends on waiting for being completed (I/O)
    rather than heavy calculations (CPU)
    """
    time.sleep(duration)
    return f"Taks {num} completed"

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


if __name__ == "__main__":
    start_time = time.perf_counter()
    results = run_sync(tasks=5)
    finish_time = time.perf_counter() - start_time

    print("="*70)
    print("Synchronous results:")
    for result in results:
        print(f"  {result}")

    print(f"\nTotal time: {finish_time: .2f} seconds")
    print("Note: Tasks ran one after another (synchronous execution)\n")

    start_time = time.perf_counter()
    results = run_threading(tasks=5)
    finish_time = time.perf_counter() - start_time

    print("="*70)
    print("Threading results:")
    for result in results:
        print(f"  {result}")

    print(f"\nTotal time: {finish_time: .2f} seconds")
    print("Note: Tasks ran in concurrently using threads (I/O-bound tasks)\n")

