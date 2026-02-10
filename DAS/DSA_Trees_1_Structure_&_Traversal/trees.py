from typing import Optional, List, final


class Node:

    def __init__(self,value):
        self.data = value
        self.left = self.right = None



# building a binary search tree

def insert(root, value):
    if root is None:
        return Node(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right,value)
    return root



def build(values:Optional[List[int]])->Optional[Node]:
    root = None
    for item in values:
        root = insert(root, item)
    return root



# building normal binary tree

def build_tree(values:Optional[List[int]])->Optional[Node]:
#     edge case
    if not values:
        return None

#     create each member of values as node
    Nodes = [Node(item) for item in values]


#     connect children
    for idx in range(len(values)):
        left_idx = 2*idx + 1
        right_idx = 2*idx + 2

        if left_idx < len(values):
            Nodes[idx].left = Nodes[left_idx]
        if right_idx < len(values):
            Nodes[idx].right = Nodes[right_idx]
    return Nodes[0]









# inorder traversal

def inorder_traversal(root:Node):
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.data)
        result+=inorder_traversal(root.right)
    return result

# In-order traversal using iterative manner

class pair:

    def __init__(self, root:Optional[Node], state:int):
        self.root = root
        self.state = state



def inorder_traversal_iterative(root:Optional[Node])->List[int]:
    result = []

    if root is None:
        return []

    p = pair(root,0)
    stack = []
    stack.append(p)
    while len(stack) != 0:
        top = stack[-1]
        if top.state == 0:
            top.state += 1
            if top.root.left is not None:
                tp = pair(top.root.left,0)
                stack.append(tp)
        elif top.state == 1:
            top.state += 1
            result.append(top.root.data)
        elif top.state == 2:
            top.state += 1
            if top.root.right is not None:
                tp = pair(top.root.right,0)
                stack.append(tp)
        else:
            stack.pop()

    return result




# ---------------------------------------------------------------------------------------------------------
# LeetCode 663 — Equal Tree Partition
# Given the root of a binary tree, check if it is possible to partition the tree into two trees with
# equal sum by removing exactly one edge.

def get_sum(root):
    if root is None:
        return 0
    return get_sum(root.left) + get_sum(root.right) + root.data

def find(root,target_sum):
    global ans
    if root is None:
        return 0

    left_sum = find(root.left,target_sum)
    right_sum = find(root.right,target_sum)

    if left_sum == target_sum or right_sum == target_sum:
        ans = True

    return left_sum + right_sum + root.data


def tree_partition(root:Optional[Node]):
    if root is None:
        return False
    total_sum = get_sum(root)
    if total_sum % 2 != 0:
        return False
    else:
        return find(root,total_sum//2)

values = [1,2,3,4,5,6,7]
bt = build_tree(values)
ans = False
print(tree_partition(bt))

print(ans)

# values = ['A','B','C','D','E','F','G']

root = build(values)
print(inorder_traversal(root))

print(inorder_traversal(bt))
print(inorder_traversal_iterative(bt))
