class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.hashmap = {}
        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i
        
        self.pre_idx = 0  # zeigt auf das nächste unverarbeitete preorder-Element
        
        def dfs(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_val = self.preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            m = self.hashmap[root_val]
            root.left = dfs(in_left, m - 1)
            root.right = dfs(m + 1, in_right)
            return root
        
        return dfs(0, len(inorder) - 1)