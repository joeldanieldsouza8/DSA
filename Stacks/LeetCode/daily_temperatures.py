def dailyTemperatures(temperatures: list[int]) -> list[int]:
    # Check if the list is empty
    if not temperatures:
        return []
    
    n = len(temperatures)

    # Create a results list that will store the number of days you have to wait for each i-th day in the 'temperatures' list.
    # Default is 0, because if a day never finds a warmer future, it should remain 0.
    days_wait = [0] * n

    # Create a stack to keep track of the indicies of the days we haven't yet processed
    # The stack keeps a record of the coldest recorded temperature (index position)
    unresolved_days: list[int] = []

    for current_day, current_temp in enumerate(temperatures):
        # If the stack is empty, it means there are no past days waiting. 
        # Check if the current day's temperature is warmer, than the most recent recorded cold day at the of top of the stack
        while (unresolved_days) and (current_temp > temperatures[unresolved_days[-1]]):
            # As a warm day is found, remove the previous day from the stack because it has now been resolved/processed
            previous_day = unresolved_days.pop()

            # Calculate the number of days it took from the first warmer day found, to the day we just popped/removed from the stack
            days_wait[previous_day] = current_day - previous_day

        # Add the current day to the stack.
        # It must now wait in the stack until a future day comes along that is warmer than it.
        unresolved_days.append(current_day)

    return days_wait





print(dailyTemperatures([73,74,75,71,69,72,76,73]))