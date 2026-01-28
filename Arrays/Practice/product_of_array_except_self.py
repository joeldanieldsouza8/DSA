def productExceptSelf(nums: list[int]) -> list[int]:
    # Check if the list is empty
    if not nums:
        return []
    
    # Length of the list
    n = len(nums)

    # Initialise the 'answer' list the same size as the input list, with '1' initialised as the value at each index position.
    # '1' because any number multiplied by '1' is unchanged.
    answers  = [1] * n

    # Iterate through the list once from left --> right
    # Initialise the start index position with '1' because we ignore "self" (i.e., the current element we are looking at in the list)
    prefix = 1
    for i in range(n):
        answers[i] = prefix

        prefix *= nums[i]

    # Iterate through the list once from right --> left
    postfix = 1
    for i in range(n - 1, -1, -1):
        answers[i] *= postfix

        postfix *= nums[i]

    return answers



print(productExceptSelf([1,2,3,4]))