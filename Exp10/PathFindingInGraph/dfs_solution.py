
def valid_path(n, edges, source, destination):
    displayg(n, edges, source, destination)

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n

    def dfs(node):
        if node == destination:
            return True
        visited[node] = True
        for nxt in adj[node]:
            if not visited[nxt]:
                if dfs(nxt):
                    return True
        return False

    return dfs(source)

def displayg(n, edges, source, destination):
    print(f" Graph nodes {n}, routes are {edges}. \n Starting from {source} To destination is {destination}", end=" is ")


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
