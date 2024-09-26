# Problem: Count Buildings that Can See Sunlight
# Description: Given a list of building heights, count how many buildings can see sunlight if the sunlight 
# comes from the left. A building can see sunlight if there is no taller building to its left.

class Solution:
    def countBuildings(self, height):
        """
        Counts the number of buildings that can see sunlight from the left.

        :param height: List[int], a list of building heights.
        :return: int, the count of buildings that can see sunlight.
        """
        # Initialize left_max with the height of the first building
        left_max = height[0]
        co = 0
        # Loop through the heights of buildings from the second one onwards
        for h in height[1:]:
            if h > left_max:
                co += 1
            # Update left_max to be the maximum height encountered so far
            left_max = max(left_max, h)
        # Add 1 to the count for the first building, which always sees sunlight
        return co + 1

## Time Complexity: O(N), where N is the number of buildings in the list.
## Space Complexity: O(1), since no extra space is used beyond the input list.

# Example usage:
# solution = Solution()
# print(solution.countBuildings([7, 4, 8, 2, 9]))  # Expected output: 4, as buildings with heights 7, 8, and 9 can see sunlight.
