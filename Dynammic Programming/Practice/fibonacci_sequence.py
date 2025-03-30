import time
from typing import *


class Fibonacci:
    def fib_naive(self, n_term: int) -> int:
        # Base case
        if (n_term == 0) or (n_term == 1):
            return n_term  # Return 0 when 'n_term == 0'. Return 1 when 'n_term == 1'

        # Otherwise, compute the sum of the previous two terms
        result = self.fib_naive(n_term - 2) + self.fib_naive(n_term - 1)
        return result

    # Recursion Depth will be exceeded for relatively large values of 'n_term', as the initial function chain depth of (n) exceeds Python's recursion limit.
    # Memoization does not change the fact that to calculate fib(500) for the very first time, your code must make a chain of calls roughly 500 levels deep (fib(500) -> fib(499) -> ... -> fib(1)) before it can even start returning values and filling the cache.
    def fib_memoized(self, n_term, *, cache: Dict[int, int]):
        # Check if 'n_term' is valid

        # Base cases
        if n_term == 0:
            return 0

        if n_term == 1:
            return 1

        # Check if the result of the 'n_term' is cached
        if n_term in cache:
            return cache[n_term]

        # Otherwise, recursively compute the result
        result = self.fib_memoized(n_term - 2, cache=cache) + self.fib_memoized(n_term - 1, cache=cache)

        # Cache the result of the 'n_term'
        cache[n_term] = result

        return result


# Example:
# sequence:     0, 1, 1, 2, 3, 5, 8
# nth term:     0, 1, 2, 3, 4, 5, 6

def main():
    fib_1 = Fibonacci()
    cache: Dict[int, int] = {}

    start = time.time()
    result = fib_1.fib_memoized(500, cache=cache)
    end = time.time()

    total_time = end - start

    print(f"Total Time: {total_time}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
