class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def in_order(root):
    if root==None:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)
root=TreeNode(10)
a1=TreeNode(2)
a2=TreeNode(13)
a3=TreeNode(1)
a4=TreeNode(5)
a5=TreeNode(6)
root.left=a1
root.right=a2
a1.left=a3
a1.right=a4
in_order(root)