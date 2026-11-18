import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    heap = [(0, 0)]
    cost = 0

    while heap:
        w, u = heapq.heappop(heap)

        if visited[u]:
            continue

        visited[u] = True
        cost += w

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v))

    return cost

n = int(input("Enter number of vertices: "))
graph = [[] for i in range(n)]

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))

print("Minimum cost:", prim(graph))