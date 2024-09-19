# Problem: Balanced Parentheses
# Description: Given a string `x` containing only the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.

class Solution:
    def ispar(self, x: str) -> bool:
        """
        This function checks if the given string of parentheses is balanced or not.

        :param x: str - A string containing parentheses ('(', ')', '{', '}', '[', ']')
        :return: bool - True if the parentheses are balanced, False otherwise
        """
        stack = []
        
        # Step 1: Traverse through each character in the string
        for i in x:
            if i in '({[':  # Check for opening brackets
                stack.append(i)
            else:
                # Step 2: If closing bracket, check for the matching opening bracket
                if not stack:  # If no opening bracket for a closing bracket
                    return False
                if (i == ')' and stack[-1] == '(') or \
                   (i == ']' and stack[-1] == '[') or \
                   (i == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False  # Mismatch found
        
        # Step 3: Ensure all brackets were closed
        return len(stack) == 0

# Time Complexity: O(n), where n is the length of the input string.
# Space Complexity: O(n), due to the stack used to store the opening brackets.
#
# Example Usage:
# solution = Solution()
# print(solution.ispar("{[()]}"))  # Output: True
# print(solution.ispar("{[(])}"))  # Output: False
