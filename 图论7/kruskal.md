# kruskal

## 初步思路
kruskal的思路是

排序： 将图中所有的边按照权重（距离）从小到大进行排序。

贪心选择： 依次遍历排序后的边，尝试将其加入到生成树中。

判环： 在加入一条边之前，必须检查这条边连接的两个顶点是否已经连通。如果已经连通，加入这条边就会形成“环”，所以必须舍弃；如果没有连通，则将这条边加入最小生成树，并累加权重。

终止： 当加入了 V - 1条边时（$V$ 为顶点数），所有的岛屿就已经全部连通了，算法结束。

```python 
import sys

# 并查集 (Disjoint Set Union) 数据结构
class DSU:
    def __init__(self, n):
        # 初始化时，每个顶点的父节点是自己（各自独立成一个集合）
        self.parent = list(range(n + 1))
        
    def find(self, i):
        # 查找根节点，并进行“路径压缩”优化，加速后续查找
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        # 尝试合并两个顶点所在的集合
        root_i = self.find(i)
        root_j = self.find(j)
        
        # 如果根节点不同，说明不在同一个集合，不会形成环
        if root_i != root_j:
            self.parent[root_i] = root_j  # 将其中一个集合连接到另一个
            return True  # 返回 True 表示合并成功（可以选用这条边）
        
        # 如果根节点相同，说明已经在同一个集合，加入会形成环
        return False

def solve():
    # 读取所有输入数据
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    V = int(input_data[0])
    E = int(input_data[1])
    
    # 存储所有的边，格式为 (权重, 起点, 终点)
    # 将权重放在元组的第一个位置，方便后续直接调用 sort() 进行排序
    edges = []
    idx = 2
    for _ in range(E):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        weight = int(input_data[idx+2])
        edges.append((weight, u, v))
        idx += 3
        
    # 1. 按照边的权重从小到大排序
    edges.sort()
    
    # 初始化并查集，顶点编号从 1 到 V
    dsu = DSU(V)
    
    min_cost = 0
    edge_count = 0
    
    # 2. 从小到大遍历所有的边
    for weight, u, v in edges:
        # 3. 利用并查集判断是否形成环
        if dsu.union(u, v):
            # 如果没有形成环，采纳这条边
            min_cost += weight
            edge_count += 1
            
            # 4. 优化：如果已经选够了 V - 1 条边，说明最小生成树已完成，提前退出
            if edge_count == V - 1:
                break
                
    print(min_cost)

if __name__ == "__main__":
    solve()
```