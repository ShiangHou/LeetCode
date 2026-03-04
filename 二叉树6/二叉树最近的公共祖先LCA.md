# 二叉树最近的公共祖先
力扣236

## 初步思路

首先先明白什么是公共祖先

所谓的公共祖先，指的是，对于两个节点q和p，有一个节点x，使得x既是q的祖先，也是p的祖先

所谓的最近，指的是深度最大

一开始还在想什么是深度最大，如果是越往上深度最大的化，那么root是所有人的公共祖先，这题就没有意义了，所以是越往下深度越大

这道题也就是所谓的LCA

LCA问题是very重要的问题，

算了直接看左程云把

## 解法思路

md 看了代码very的巧妙啊我靠


### 流程
先说流程 一个递归函数，入参是root，p，q

如果遇到空、遇到p、遇到q，直接返回root（即返回当前节点）

l = 递归 root.left

r = 递归 root.right

如果l为空，r也为空，直接返回None

如果l也搜到了，r也搜到，返回root

如果l、r一个搜到了一个没搜到，返回不空的那个

### 逻辑
什么逻辑呢，这类问题有两种情况，一种是q和p是包含关系，即一个是公共子祖先

1）包含关系

当我们往下走的时候，如果遇到了q，那么会直接返回它。如果是包含，那么p是在q的下面，由于我们直接返回了q，所以根本走不到p。所以在递归中，我们只会经过

 **如果l、r一个搜到了一个没搜到，返回不空的那个**

 这个流程，所以说最后返回的就是最先遇到的，即公共祖先

 2）不包含关系

 当我们遍历到一个root的时候，如果左边遍历到q，右边遍历到p，那么他们在层层返回的时候会撞在这个root上，此时会走

 **如果l也搜到了，r也搜到，返回root**

 那么再往上就会一直返回这个交汇的root，也就是最终的答案

 所以这题的核心就是理解这个回溯的过程，回溯时交汇的地方就是最后的答案

 ```python 
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root
    l = self.lowestCommonAncestor(root.left,p,q)
    r = self.lowestCommonAncestor(root.right,p,q)

    if not l and not r:
        return None
    elif l and r:
        return root
    return l if not r else r


 ```


