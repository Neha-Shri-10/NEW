class Solution:
    def longestUniqueSubstr(self, S: str) -> int:
        # A list to collect unique letters for our current window
        current_window = []
        max_length = 0
        
        # Look at each letter in the string one by one
        for letter in S:
            
            # If the letter is already in our window, it's a duplicate!
            while letter in current_window:
                # Remove the oldest letter from the left side
                current_window.pop(0)
                
            # Now that the duplicate is gone, safe to add the new letter
            current_window.append(letter)
            
            # Check if this is the biggest window we have seen so far
            if len(current_window) > max_length:
                max_length = len(current_window)
                
        return max_length