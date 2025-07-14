def distinct_artists(song_artists: list[str], max_artists: int):
    # Check if the list is empty
    if not song_artists:
        return 0
    
    # Initialize the start of our sliding window at the first element
    start_pointer = 0

    # Create a dictionary to track the frequency of artists within the current window
    artists_window: dict[str, int] = {}

    # Initialize a variable to store the length of the longest valid playlist found so far. The length should be...
    best_max_distinct_length = 0

    # Iterate through the entire list with the 'end_pointer' (which expands the window to the right), until the end of the list is reached
    for end_pointer in range(len(song_artists)):
        # Get the new artist who is currently entering the window
        entering_artist = song_artists[end_pointer]
        
        # # Check if the current artist doesn't exist in the dictionary
        # if entering_artist not in artists_window:
        #     # Add the current artist to the window
        #     artists_window[entering_artist] = 1

        # # Otherwise, the current artist exists in the dictionary
        # else:
        #     # Increment the frequency of the current artist by 1
        #     artists_window[entering_artist] += 1

        # Add the new artist to our window or increment their count if they already exist
        artists_window[entering_artist] = artists_window.get(entering_artist, 0) + 1

        # Check if the window is now invalid (has more distinct artists than allowed).
        # If so, shrink the window from the left until it becomes valid again.
        while len(artists_window) > max_artists:           
            # Get the artist who is about to leave the window from the left
            departing_artist = song_artists[start_pointer]

            # Decrement the frequency of the departing artist by 1
            artists_window[departing_artist] -= 1

            # Check if the frequency of the artist is 0
            if artists_window[departing_artist] == 0:
                # Delete the key-value pair of the departing artist to keep the distinct artist count accurate
                artists_window.pop(departing_artist)

            # Move the start of the window one step to the right, effectively shrinking it
            start_pointer += 1

        current_length = (end_pointer - start_pointer) + 1          
        best_max_distinct_length = max(best_max_distinct_length, current_length)

    return best_max_distinct_length




print(distinct_artists(song_artists=['ArtistA', 'ArtistB', 'ArtistC', 'ArtistA', 'ArtistC'], max_artists=2))
# Expected Output: 3

print(distinct_artists(song_artists=['Rock', 'Jazz', 'Pop', 'Rock', 'Jazz', 'Jazz', 'Rock'], max_artists=2))
# Expected Output: 4

print(distinct_artists(song_artists=['DJ_A', 'DJ_A', 'DJ_B', 'DJ_C', 'DJ_C', 'DJ_C', 'DJ_A'], max_artists=1))
# Expected Output: 3