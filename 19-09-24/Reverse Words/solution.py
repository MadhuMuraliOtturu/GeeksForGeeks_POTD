# Problem: Reverse Words in a String
# Description: Given a string `s` containing words separated by dots ('.'), reverse the words.
# The dots are used as delimiters, and the words should maintain their original order within the reversed sequence.

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        This function reverses the words in a given string, where words are separated by dots.

        :param s: str - A string of words separated by dots ('.')
        :return: str - The string with the words reversed in order
        """
        # Step 1: Split the string into words based on the dot delimiter
        rev = s.split('.')
        
        # Step 2: Reverse the order of words
        rev = rev[::-1]
        
        # Step 3: Join the words back into a string with dots separating them
        return '.'.join(rev)

# Time Complexity: O(n), where n is the length of the string `s`.
# Space Complexity: O(n), for storing the split words and the reversed string.
#
# Example Usage:
# solution = Solution()
# print(solution.reverseWords("i.like.this.program.very.much"))  # Output: "much.very.program.this.like.i"
# print(solution.reverseWords("hello.world"))  # Output: "world.hello"
