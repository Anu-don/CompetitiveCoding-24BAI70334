
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


def valid_path(n, edges, source, destination):
    print(f" Number of islands {n}, routes are {edges}. \n Starting from {source} To destination is {destination}", end=" is ")
    dsu = DSU(n)
    for u, v in edges:
        dsu.union(u, v)
    return dsu.find(source) == dsu.find(destination)


if __name__ == "__main__":
    # Test Case 1
    print(valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # Expected: True
    print()

    # Test Case 2
    print(valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # Expected: False
    print()

    # Test Case 3
    print(valid_path(1, [], 0, 0))  # Expected: True
    print()
