# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        Q = deque([q])
        P = deque([p])
        


        # level by level -> popleft -> add left and right 
        level = 0
        while Q and P:
            
            for i in range(len(Q)):
                nodeP = P.popleft()
                nodeQ = Q.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                P.append(nodeP.left)
                P.append(nodeP.right)
                Q.append(nodeQ.left)
                
                Q.append(nodeQ.right)

        
        return True