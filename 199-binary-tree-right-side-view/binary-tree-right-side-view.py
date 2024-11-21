class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        q = deque([root])
        rightside = []

        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if node:
                # if it's the rightmost element
                    if i == level - 1:
                        rightside.append(node.val)

                    # add child nodes in the queue
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        return rightside