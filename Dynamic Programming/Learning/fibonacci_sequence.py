# def fibonacci_sequence(nth_term: int) -> int:
#     # Check if base case is reached (this handles the negative case as well!)
#     if nth_term <= 1:
#         return nth_term
    
#     result = fibonacci_sequence(nth_term - 1) + fibonacci_sequence(nth_term - 2)

#     return result


# ---------------------------------------------------------------------------------------

# Top-Down Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)

# memo: dict[int, int] = {}

# def fibonacci_sequence(nth_term: int) -> int:
#     # Check if the computation for the n-th term already exists in the dictionary
#     if nth_term in memo:
#         return memo[nth_term]

#     if nth_term <= 1:
#         return nth_term
    
#     result = fibonacci_sequence(nth_term - 1) + fibonacci_sequence(nth_term - 2)

#     # Update the dictionary to store the computed value of the current nth term
#     memo[nth_term] = result

#     return result


# ---------------------------------------------------------------------------------------

# Bottom-Up Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)

def fibonacci_sequence(nth_term: int) -> int:
    memo: dict[int, int] = {
        0: 0,
        1: 1
    }

    # Note, the `range()` function includes the 'start' number, but excludes the 'stop' number. It goes up to, but does not include, the limit. Hence, why the value for the 'stop' parameter is 'n + 1'
    for i in range(2, nth_term + 1):
        # Old Way: result = fibonacci_sequence(nth_term - 1) + fibonacci_sequence(nth_term - 2)
        result = memo[nth_term - 1] + memo[nth_term - 2]
        
        memo[i] = result

    return memo[nth_term]