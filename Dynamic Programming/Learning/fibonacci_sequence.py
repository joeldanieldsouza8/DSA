# def fibonacci_sequence(nth_term: int) -> int:
#     # Check if base case is reached (this handles the negative case as well!)
#     if nth_term <= 1:
#         return nth_term
    
#     result = fibonacci_sequence(nth_term - 1) + fibonacci_sequence(nth_term - 2)

#     return result

memo: dict[int, int] = {}

def fibonacci_sequence(nth_term: int) -> int:
    # Check if the computation for the n-th term already exists in the dictionary
    if nth_term in memo:
        return memo[nth_term]

    if nth_term <= 1:
        return nth_term
    
    result = fibonacci_sequence(nth_term - 1) + fibonacci_sequence(nth_term - 2)

    # Update the dictionary to store the computed value of the current nth term
    memo[nth_term] = result

    return result
