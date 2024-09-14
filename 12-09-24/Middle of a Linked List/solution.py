## USING TOTAL NO OF NODES IN A LINKED LIST(COUNTING) ##


# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    # Function to return data of middle node. If linked list is empty, then -1
    def getMiddle(self, head):
        """
        Find the data of the middle node in a linked list.

        If the linked list is empty, the function returns -1.

        Args:
        head (Node): The head node of the linked list.

        Returns:
        int: The data of the middle node, or -1 if the linked list is empty.

        Time Complexity:
        O(n): The function traverses the list twice to find the middle node.
        
        Space Complexity:
        O(1): The function uses a constant amount of extra space.
        """
        # Edge case: If the list is empty
        if not head:
            return -1

        # First pass: Count the number of nodes
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        # Calculate the middle index
        middle_index = count // 2

        # Second pass: Find the middle node
        temp = head
        for _ in range(middle_index):
            temp = temp.next

        return temp.data

# Sample Usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    # Creating an object of Solution class
    obj = Solution()
    
    # Getting the data of the middle node
    middle_data = obj.getMiddle(head)
    
    # Print the data of the middle node
    print("Data of the middle node:", middle_data)





## TWO POINTER APPROACH - OPTIMAL APPROACH ##


# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    # Function to return data of middle node. If linked list is empty, then -1
    def getMiddle(self, head):
        """
        Find the data of the middle node in a linked list.

        If the linked list is empty, the function returns -1. 

        Args:
        head (Node): The head node of the linked list.

        Returns:
        int: The data of the middle node, or -1 if the linked list is empty.

        Time Complexity:
        O(n): The function traverses the list once to find the middle node.
        
        Space Complexity:
        O(1): The function uses a constant amount of extra space.
        """
        # If the list is empty
        if not head:
            return -1
        
        slow = head
        fast = head
        
        # Traverse the list with two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Return the data of the middle node
        return slow.data

# Sample Usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    # Creating an object of Solution class
    obj = Solution()
    
    # Getting the data of the middle node
    middle_data = obj.getMiddle(head)
    
    # Print the data of the middle node
    print("Data of the middle node:", middle_data)
