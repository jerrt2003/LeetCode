# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def flatten(self, root):
#         """
#         Solution: Recursion + Queue
#         Time Complexity: O(n)
#         Space Complexity: O(n)
#         Inspired By: MYSELF!!
#         Thinking Process:
#         - Using Queue
#         - A BETTER WAY is to use pre-order traversal --> MUCH STRAIGHT FORWARD
#         def flatten(self, root):
#             ans=[]
#             if not root: return root
#
#             def helper(root):
#                 if root:
#                     ans.append(root)
#                     helper(root.left)
#                     helper(root.right)
#
#             helper(root)
#             root=ans[0]
#             p=root
#             for i in range(1,len(ans)):
#                 p.left=None
#                 p.right=ans[i]
#                 p=p.right
#         :type root: TreeNode
#         :rtype: void Do not return anything, modify root in-place instead.
#         """
#         if root is None: return
#         starting_queue = [root]
#         self.create_linked_list(starting_queue)
#
#     def create_linked_list(self, queue):
#         while len(queue) != 0:
#             node = queue.pop(-1)
#             # we need to start with right first so that we can pop with left in the next while loop
#             if node.right is not None:
#                 queue.append(node.right)
#             if node.left is not None:
#                 queue.append(node.left)
#             node.left = None
#             if len(queue) != 0:
#                 node.right = queue[-1]
#             else:
#                 node.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        Facebook
        Stack
        Pre-order traversal
        T:O(n) S:O(n)
        Runtime: 48 ms, faster than 7.26% of Python online submissions for Flatten Binary Tree to Linked List.
        Memory Usage: 13.6 MB, less than 54.66% of Python online submissions for Flatten Binary Tree to Linked List.
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return
        stack = []
        if root.right: stack.append(root.right)
        if root.left: stack.append(root.left)
        while stack:
            node = stack.pop()
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            root.left = None
            root.right = node
            root = node

