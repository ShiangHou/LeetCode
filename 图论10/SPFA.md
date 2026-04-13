# SPFA

emmmm,看懂了一点点，但还是直接抄的答案

```python 
import collections

def main():
    n, m = map(int, input().strip().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        src, dest, weight = map(int, input().strip().split())
        edges[src].append([dest, weight])
    
    minDist = [float("inf")] * (n + 1)
    minDist[1] = 0
    que = collections.deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    
    while que:
        cur = que.popleft()
        visited[cur] = False
        for dest, weight in edges[cur]:
            if minDist[cur] != float("inf") and minDist[cur] + weight < minDist[dest]:
                minDist[dest] = minDist[cur] + weight
                if visited[dest] == False:
                    que.append(dest)
                    visited[dest] = True
    
    if minDist[-1] == float("inf"):
        return "unconnected"
    return minDist[-1]

if __name__ == "__main__":
    print(main())

```