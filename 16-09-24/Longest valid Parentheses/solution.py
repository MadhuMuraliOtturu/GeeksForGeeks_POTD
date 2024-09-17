# Problem: Longest Valid Parentheses
# Description: Given a string containing just the characters '(' and ')', find the length of the longest 
# valid (well-formed) parentheses substring.

class Solution:
    def maxLength(self, s: str) -> int:
        """
        This function calculates the length of the longest valid (well-formed) parentheses substring.
        
        :param s: str - the input string containing only '(' and ')'
        :return: int - the length of the longest valid parentheses substring
        """
        # Initialize a stack to store indices of '(' characters
        stack = []  
        # Variable to store the length of the longest valid parentheses substring
        max_length = 0
        # Index of the last unmatched ')' character
        last_invalid_index = -1
        
        # Iterate through each character in the string
        for i, char in enumerate(s):
            if char == '(':
                # If it's an opening bracket, push the index onto the stack
                stack.append(i)
            else:  
                # If it's a closing bracket
                if stack:
                    # If there is a matching '(' in the stack, pop it
                    stack.pop()
                    if stack:
                        # Calculate the length of the valid substring
                        max_length = max(max_length, i - stack[-1])
                    else:
                        # If the stack is empty, calculate the length from the last unmatched index
                        max_length = max(max_length, i - last_invalid_index)
                else:
                    # Update the last unmatched ')' index
                    last_invalid_index = i
        
        return max_length

# Time Complexity: O(n), where n is the length of the string. We traverse the string once.
# Space Complexity: O(n), since in the worst case, the stack will store all the indices of '(' characters.
#
# Example Usage:
# solution = Solution()
# print(solution.maxLength(")()())"))
# Output: 4
