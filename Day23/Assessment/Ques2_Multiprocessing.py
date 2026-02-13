import math
import time
import sys
from multiprocessing import Pool, cpu_count

sys.set_int_max_str_digits(1000000)

numbers = [50000, 60000, 55000, 45000, 70000]

def compute_factorial(n):
    return (n, math.factorial(n))


if __name__ == "__main__":

    # Sequential
    starttime1 = time.time()

    seq_results = []
    for num in numbers:
        result = compute_factorial(num)
        seq_results.append(result)
        print(f"Sequential: Factorial({num}) calculated")

    seqtime = time.time() - starttime1
    print(f"\nSequential Time: {seqtime:.2f} seconds\n")

    # Multiprocessing
    starttime2 = time.time()

    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factorial, numbers)

    paralleltime = time.time() - starttime2
    print(f"Multiprocessing Time: {paralleltime:.2f} seconds\n")

    # Result Summary
    print("Factorial Results Summary:")
    for num, fact in parallel_results:
        print(f"Factorial({num}) has {len(str(fact))} digits")
