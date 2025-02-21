class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def pre_order(root):
    if root==None:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)
root=TreeNode(1)
a1=TreeNode(2)
a2=TreeNode(3)
a3=TreeNode(4)
a4=TreeNode(5)
a5=TreeNode(6)

root.left=a1
root.right=a2
a1.left=a3
a1.right=a4
a2.right=a5
pre_order(root)