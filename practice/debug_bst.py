class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def height_of_tree(root):
    if root is None:
        return 0
    else:
        left_height = height_of_tree(root.left)
        right_height = height_of_tree(root.right)

        # Choose the maximum height between left and right subtrees
        return max(left_height, right_height) + 1



def is_balanced(root):
     return abs(height_of_tree(root.left) - height_of_tree(root.right))
# Create the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8)
root.right.left = TreeNode(6)

# Find the height of the tree
tree_height = is_balanced(root)
print("Height of the tree:", tree_height)
