# Problem: Binary Tree to Doubly Linked List
# Description: Given a binary tree, convert it into a doubly linked list (DLL). 
# The order of nodes in the DLL must be the same as the in-order traversal of the binary tree.

class ListNode:
    def __init__(self, val):
        """
        A node for the doubly linked list.
        :param val: The value of the node.
        """
        self.data = val
        self.right = None  # Points to the next node in DLL
        self.left = None   # Points to the previous node in DLL

class Solution:
    def __init__(self):
        """
        Initializes an empty list to store the in-order traversal of the binary tree.
        """
        self.l = []
        
    def inorder(self, root):
        """
        Performs in-order traversal of the binary tree and stores the node values.
        
        :param root: The root node of the binary tree.
        """
        if root:
            self.inorder(root.left)
            self.l.append(root.data)
            self.inorder(root.right)
    
    def bToDLL(self, root):
        """
        Converts a binary tree into a doubly linked list using in-order traversal.
        
        :param root: The root node of the binary tree.
        :return: The head node of the created doubly linked list.
        """
        self.inorder(root)
        
        if not self.l:
            return None
        
        # Create the head of the doubly linked list
        head = ListNode(self.l[0])
        prev = head
        
        # Iterate through the rest of the in-order list and create the DLL
        for i in range(1, len(self.l)):
            newnode = ListNode(self.l[i])
            prev.right = newnode
            newnode.left = prev
            prev = newnode
        
        return head

# Time Complexity: O(n), where n is the number of nodes in the binary tree. We traverse the tree once and create the DLL in linear time.
# Space Complexity: O(n), for storing the in-order traversal of the binary tree and constructing the DLL.

# Example usage:
# root = ListNode(10)  # Creating a binary tree
# solution = Solution()
# dll_head = solution.bToDLL(root)
# # The variable `dll_head` now points to the head of the doubly linked list.
