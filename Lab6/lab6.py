import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def solve():
    with open("gamsrv.in", encoding='utf-8') as f:
        lines = f.read().strip().split('\n')

    n, m = map(int, lines[0].split())
    clients = set(map(int, lines[1].split()))

    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = map(int, lines[2 + i].split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    results = []

    for server in range(1, n + 1):
        if server in clients:
            continue

        dist = dijkstra(graph, server, n)

        max_delay = 0
        possible = True
        for c in clients:
            if dist[c] == float('inf'):
                possible = False
                break
            max_delay = max(max_delay, dist[c])

        if possible:
            results.append((max_delay, server))

    results.sort()
    top3 = results[:3]

    with open("gamsrv.out", "w", encoding='utf-8') as f:
        f.write(str(top3[0][0]) + "\n")
        f.write("\nТоп-3 найкращих розміщення сервера:\n")
        for rank, (delay, server) in enumerate(top3, 1):
            f.write(f"  {rank}. Вузол {server} — максимальна затримка: {delay} мс\n")

solve()