# Problem: Minimum Difference Between Heights II
# Description: Given an array of integers representing heights and a number `k`, 
# the goal is to minimize the difference between the maximum and minimum heights after modifying each element by adding or subtracting `k`.

class Solution:
    def getMinDiff(self, arr, k):
        """
        This function calculates the minimum possible difference between the highest and lowest 
        elements in the array after modifying each element by adding or subtracting a given number k.

        :param arr: List[int] - a list of integers representing the heights
        :param k: int - the maximum value that can be added or subtracted from each element
        :return: int - the minimized difference between the maximum and minimum heights
        """
        n = len(arr)
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize the difference as the current difference
        ans = arr[n - 1] - arr[0]
        
        # Step 3: Initialize temporary minimum and maximum heights
        tempmin = arr[0]
        tempmax = arr[n - 1]
    
        for i in range(1, n):
            if arr[i] < k:
                continue  # Skip if the adjustment would make the height negative
                
            # Step 4: Calculate new minimum and maximum heights after adjusting by k
            tempmin = min(arr[0] + k, arr[i] - k)
            tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
            
            # Step 5: Update the answer with the minimum difference found
            ans = min(ans, tempmax - tempmin)
    
        return ans

# Time Complexity: O(n log n), due to sorting the array.
# Space Complexity: O(1), as the space used is constant.
#
# Example Usage:
# solution = Solution()
# print(solution.getMinDiff([1, 5, 8, 10], 2))
# Output: 5
