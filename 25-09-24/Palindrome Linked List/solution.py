# Problem: Check if a Linked List is a Palindrome
# Description: Given the head of a singly linked list, determine if the linked list is a palindrome.
# The function should return True if the linked list is a palindrome, and False otherwise.

class Solution:
    def isPalindrome(self, head):
        """
        Checks if a singly linked list is a palindrome.

        :param head: ListNode, the head of the linked list.
        :return: bool, True if the linked list is a palindrome, False otherwise.
        """
        if not head or not head.next:
            return True
            
        # Initialize two pointers
        fast = head
        slow = head
        
        # Move fast pointer twice as fast as the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        second_half = slow
        prev = None
        
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
            
        # Compare the first half and the reversed second half
        first_half = head
        
        while prev:  # Compare reversed second half with the first half
            if first_half.data != prev.data:
                return False
            first_half = first_half.next
            prev = prev.next
        
        return True

## Time Complexity: O(N), where N is the number of nodes in the linked list.
## Space Complexity: O(1), as only a constant amount of extra space is used.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)
# solution = Solution()
# print(solution.isPalindrome(head))  # Expected output: True
