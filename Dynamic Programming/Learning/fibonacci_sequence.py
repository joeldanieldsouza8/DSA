"""
Naive recursive implementation

Time Complexity: O(2^n)

Space complexity: O(n) - Depends on the number of items on the call stack
"""

from typing import Dict, List


def naive_fibonnaci_sequence(n: int) -> int:
    # Check for base cases to prevent calculating negative numbers
    if n <= 1:
        return n

    result: int = naive_fibonnaci_sequence(n - 1) + naive_fibonnaci_sequence(n - 2)

    return result


"""

Memoization using dictionary (Top-Down Approach)

It's a top-down approach because we start from the top (n th term) and recursively work our way down, saving the results of each n th term along the way.

For example, if n = 5, we start at the top fib(5) and work our way down to the bottom fib(0). 

Time Complexity: O(n):
    Ignoring the recursive calls in the function, the actual WORK DONE inside a single function call (the additions, the dictionary lookups/writes) is constant, or O(1).
    
    The total work done for all recursive function calls: (Number of unique sub-problems) x (Work per sub-problem) = n * O(1) = O(n).
    
    For example, if n = 6, the total work done = 6 * O(1) = O(6).

    Hence, the total time complexity is O(n).

Space Complexity: O(n): 
    The space complexity for this algorithm is determined based on:
        The recursion stack space.
        The memoization cache space.

    The recursion stack space:
        The number of functions waiting on the call stack will be (n-1).

        For example, if n = 5
            fib(5) is called. It waits. (Stack: [fib(5)])
        
            It calls fib(4). It waits. (Stack: [fib(5), fib(4)])
        
            It calls fib(3). It waits. (Stack: [fib(5), fib(4), fib(3)])
        
            It calls fib(2). It waits. (Stack: [fib(5), fib(4), fib(3), fib(2)])
        
            It calls fib(1). fib(1) is a base case and returns immediately.

        The maximum number of functions waiting on the stack at any single point in time was 4 (or n-1). 

        Hence, the recursion stack space requires O(n) space.

    The memoization cache space:
        This is the 'memo' dictionary. For every unique sub-problem solved an entry is made to the dictionary.

        For example, if n = 5
            The entries made in the dictionary are fib(5), fib(4), fib(3), fib(2), fib(1)

        The number of keys in our memo dictionary at the end of the calculation will be (n-1).

        Hence, the cache stack space requires O(n) space.

    Total Space Used = (Space for Recursion Stack) + (Space for Memo Cache) = O(n) + O(n) = O(2n) = O(n) as we drop the constants and only care about the overall growth rate.

"""

memo: Dict[int, int] = {
    0: 0,
    1: 1,
}


def memoization_fibonnaci_sequence(n: int) -> int:
    # Check for base cases to prevent calculating negative numbers
    if n <= 1:
        return n

    # Time Complexity: O(1) - Constant lookup time in dictionary
    if n in memo:
        return memo[n]

    # Time Complexity: O(1) - Constant time for addition operation
    result: int = memoization_fibonnaci_sequence(
        n - 1
    ) + memoization_fibonnaci_sequence(n - 2)

    # Time Complexity: O(1) - Constant time for dictionary write
    memo[n] = result

    return result


"""
Tabulation (Bottom-Up Approach)

This is called Tabulation because we are filling up a table of results from the bottom up.

A pre-defined list size of size n is used. This is because the value at fib(n) is calculated immediately after the value at fib(n - 1). This perfectly mirrors how a list works. A list is an ordered collection of elements where each element has a numerical index: 0, 1, 2, 3, ....

For example, if n = 5, we start by calculating in the order:
    fib(0) --> fib(1) --> fib(2) --> fib(3) --> fib(4) --> fib(5)

Time Complexity: O(n) - Linear. We have a single for loop that runs from 2 to n. The work inside is constant time. 

Space Complexity: O(n) - Linear. We need to create a table (our list) of size n+1 to store all the intermediate results.

"""


def tabulation_fibonnaci_sequence(n: int) -> int:
    # Check for base cases
    if n <= 1:
        return n

    # Initialise a list the size of n
    # Each index in the list is initialised with the value 0. We initialise a total of n + 1 indexs because a list is 0-based index.
    table: List[int] = [0] * (n + 1)

    # Account for the base case 1. Note, the base case 0 is already accounted for in the initialisation of the list above.
    table[1] = 1

    # Begin iterating through the list from index position 2 onwards, as the base cases 0 and 1 have already been accounted for above. We stop iterating at n + 1 because we account for the list being 0-based index.
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    # The final answer for calculating the value of fib(n) is at the end of the list
    return table[n]


"""

Optimised Approach

This is the most optimised approach because we don't keep a record of all the terms from 0 to n in a data structure. We only iterate to the point where we have fib(n - 1) and fib(n - 2) terms to then calculate the value fib(n).

Time Complexity: O(n) - Linear. As we still need to iteratively reach the point of fib(n - 1) and fib(n - 2). There is no other way to magically arrive at the point to calculate the value of fib(n - 1) and fib(n - 2) without iterating up to n.

Space Complexity: O(1) - Constant. No extra data structure is used to store the computed values of the fib(i) term's.

"""

def optimised_fibonnaci_sequence(n: int) -> int:
    # Check base case
    if n <= 1:
        return n
    
    # Initialise the first two numbers in the fibonnaci sequence
    # second_prev = fib(n - 2)
    # first_prev = fib(n - 1)
    second_prev , first_prev = 0, 1
    
    # Iterate
    for _ in range(2, n):
        
        second_prev, first_prev = first_prev, first_prev + second_prev

    return second_prev + first_prev


# result = optimised_fibonnaci_sequence(10)
# print(result)

# result = tabulation_fibonnaci_sequence(10)
# print(result)