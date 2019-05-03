def reConstructBinaryTree(self,pre,tin):
    if len(pre)==0:
        return None
    if len(pre)==1:
        return TreeNode(pre[0])
    else:
        root=TreeNode(pre[0])
        pos=tin.index(pre[0])
        root.left=self.reConstructBinaryTree(pre[1:pos+1],tin[:pos])
        root.right=self.reConstructBinayTree(pre[pos+1:],tin[pos+1:])
    return root
    
