# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        if not root:
            return []
        queue= deque([root])

        result=[]

        while queue:
            level_size= len(queue)
            level_nodes=[]

            for nodes in range(level_size):
                node=queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result
        """
        if not root:
            return []

        res=[]
        queue= deque([root])
        
        while queue:
            level_nodes=[]
            for i in range(len(queue)):
                node= queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_nodes)
        return res
