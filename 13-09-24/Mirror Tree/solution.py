# User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Your task is to complete this function

class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        """
        Convert a binary tree into its mirror tree.

        A mirror tree of a binary tree is a tree where the left and right children
        of all nodes are swapped.

        Args:
        root (Node): The root node of the binary tree.

        Returns:
        Node: The root node of the mirror tree.

        Time Complexity:
        O(n): Each node is visited once.
        
        Space Complexity:
        O(h): The space complexity is determined by the height of the tree due to recursion stack.
        """
        if root:
            # Swap the left and right children
            root.left, root.right = root.right, root.left
            # Recursively mirror the left and right subtrees
            self.mirror(root.left)
            self.mirror(root.right)
        return root

# Sample Usage
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    # Creating an object of Solution class
    obj = Solution()
    
    # Converting the binary tree to its mirror
    mirror_root = obj.mirror(root)
    
    # Function to print tree (for verification)
    def print_inorder(node):
        if node:
            print_inorder(node.left)
            print(node.data, end=" ")
            print_inorder(node.right)
    
    # Print inorder traversal of the mirrored tree
    print("Inorder traversal of the mirrored tree:")
    print_inorder(mirror_root)
