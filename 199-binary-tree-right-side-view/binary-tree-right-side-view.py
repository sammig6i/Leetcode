class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        q = deque([root, None])
        rightside = []
        
        curr = root
        while q:
            prev, curr = curr, q.popleft()
            while curr:
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                prev, curr = curr, q.popleft()
            rightside.append(prev.val)
            if q:
                q.append(None)

        return rightside