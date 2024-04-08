import math


class Graph:
    def __init__(self, n: int, edges: list[tuple[int, int, float]]):
        self.n = n
        self.edges = edges
        self.graph: list[list[float]] = [[0 for _ in range(n)] for _ in range(n)]
        for u, v, w in edges:
            self.graph[u][v] = w
            self.graph[v][u] = w

    def dijkstra(self, source: int) -> list[tuple[float, list[int]]]:
        def min_distance() -> int:
            min_dist: float = math.inf
            min_index = -1
            for v in range(self.n):
                if not visited[v] and distances[v] < min_dist:
                    min_dist = distances[v]
                    min_index = v
            return min_index

        distances: list[float] = [math.inf] * self.n
        distances[source] = 0
        visited: list[bool] = [False] * self.n
        path: list[list[int]] = [[] for _ in range(self.n)]
        for _ in range(self.n):
            u: int = min_distance()
            visited[u] = True
            for v in range(self.n):
                if self.graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + self.graph[u][v]:
                    distances[v] = distances[u] + self.graph[u][v]
                    path[v] = path[u] + [u]
        return list(zip(distances, path))


if __name__ == "__main__":
    n = 9
    edges = [
        (0, 1, 6),
        (0, 2, 3),
        (0, 3, 1),
        (1, 2, 2),
        (1, 4, 1),
        (2, 3, 2),
        (3, 4, 6),
        (3, 5, 10),
        (4, 5, 4),
        # (4, 5, 10),
        (4, 6, 3),
        (4, 7, 6),
        (4, 8, 2),
        (5, 6, 2),
        (6, 7, 4),
        (7, 8, 3),
    ]
    graph = Graph(n, edges)
    source = 0
    distances = graph.dijkstra(source)
    for i, (distance, path) in enumerate(distances):
        print(f"Shortest path from v{source} to v{i} is {path + [i]} with distance {distance}")

# Output:（这里v[i]指的是题目中的v[i+1]，下标统一减1了）
# Shortest path from v0 to v0 is [0] with distance 0
# Shortest path from v0 to v1 is [0, 2, 1] with distance 5
# Shortest path from v0 to v2 is [0, 2] with distance 3
# Shortest path from v0 to v3 is [0, 3] with distance 1
# Shortest path from v0 to v4 is [0, 2, 1, 4] with distance 6
# Shortest path from v0 to v5 is [0, 2, 1, 4, 5] with distance 10
# Shortest path from v0 to v6 is [0, 2, 1, 4, 6] with distance 9
# Shortest path from v0 to v7 is [0, 2, 1, 4, 8, 7] with distance 11
# Shortest path from v0 to v8 is [0, 2, 1, 4, 8] with distance 8
