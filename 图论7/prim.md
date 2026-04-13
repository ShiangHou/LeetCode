# 寻宝

https://kamacoder.com/problempage.php?pid=1053

## 题目描述
题目说，我们现在有很多的岛屿，然后岛屿上有很多的宝藏，现在需要在岛屿之间修建高速公路

问如何可以以最短的高速公路将所有的岛屿全部连起来？

所以这个图是，首先是无向的，因为路可以相互走，然后是带有权重的，因为路有成本，并且需要连通

## 最小生成树

所谓的最小生成树就是“用最小的成本使其全部链接”

所谓最小，就是不能有冤枉路，即这个图不能有环（有环的话，从A到C就不知有一条路可以走了）所以说是一颗树

其次不能有死角，就是一定要都连起来

最后是要构成一个图

这就是所谓的最小生成树

那么在一个图里面求解最小生成树，有两个方法，一个是Prim，一个是kruskal

先说Prim，它的过程是这样的，就是贪心！

假设我有A B C D E五个点

我现在先选A点，然后去看A和剩下那些点连的成本花费的是最少的

正如厚米所说

开局： 我们站在数据中心 A。现在我们的“已连通帝国”里只有 A。

向外看： A 看看外面的世界，发现连 B 要花 4 块钱，连 C 要花 2 块钱。

贪心选择： 显然连 C 最划算！我们花 2 块钱修路，把 C 拉进帝国。现在帝国里有 {A, C}。

继续向外看： 现在 A 和 C 是一伙的了。A 连 B 要 4 块钱；C 连 B 只要 1 块钱，C 连 D 要 8 块钱，C 连 E 要 10 块钱。

再次贪心： 所有跨出帝国的路里，C 连 B（花 1 块钱）最便宜！修它！把 B 拉进来。现在帝国有 {A, C, B}。

重复循环： 只要还有孤立的点，我们就站在整个帝国所有已知节点的边界上，挑一条最便宜的向外的路，拉新节点入伙，前提是这条路连向的新节点不能是已经在帝国里的人（否则就成了白花钱的环）。

此外要注意的一点是，我这个图已经是建好的！，只是需要从中找到最小生成树就行


```python 
import heapq

def solve():
    # 读取输入，处理可能的多行输入情况
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    V = int(input_data[0])
    E = int(input_data[1])
    
    # 构建邻接表
    adj = [[] for _ in range(V + 1)]
    idx = 2
    for _ in range(E):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        weight = int(input_data[idx+2])
        adj[u].append((weight, v))
        adj[v].append((weight, u))
        idx += 3
        
    # in_mst 记录节点是否已被加入最小生成树
    in_mst = [False] * (V + 1)
    
    # 最小堆，存储格式为 (weight, node)
    pq = [(0, 1)]  # 从顶点 1 开始，初始权重为 0
    
    min_cost = 0
    nodes_added = 0
    
    while pq and nodes_added < V:
        weight, u = heapq.heappop(pq)
        
        # 如果节点已经在树中，说明是冗余边，直接跳过
        if in_mst[u]:
            continue
            
        # 标记加入生成树，累加权重
        in_mst[u] = True
        min_cost += weight
        nodes_added += 1
        
        # 遍历邻居节点，把通向未访问节点的边加入堆中
        for next_weight, v in adj[u]:
            if not in_mst[v]:
                heapq.heappush(pq, (next_weight, v))
                
    print(min_cost)

if __name__ == "__main__":
    solve()


```
