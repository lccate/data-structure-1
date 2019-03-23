# cate
# 19.3.23
# 用python实现二叉树

class Node(object):
    def __init__(self,index):
        self.index = index
        self.left_child = None
        self.right_child = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = root

    #前序遍历
    def pre_travel(self,node):
        if not node:
            return
        print(node.index)
        # 使用递归方法分别打印出左子树和右子树
        self.pre_travel(node.left_child)
        self.pre_travel(node.right_child)


node_dict = {}
for i in range(1,10):
    node_dict[i] = Node(i)
node_dict[1].left_child = node_dict[2]
node_dict[1].right_child = node_dict[3]
node_dict[2].left_child = node_dict[5]
node_dict[2].right_child = node_dict[6]
node_dict[3].left_child = node_dict[7]
node_dict[7].left_child = node_dict[8]
node_dict[7].right_child = node_dict[9]

tree = BinaryTree(node_dict[1])
tree.pre_travel(tree.root)

