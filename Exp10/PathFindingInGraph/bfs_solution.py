from collections import deque


def valid_path(n, edges, source, destination):

    displayg(n, edges, source, destination)

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    if source == destination:
        return True

    visited = [False] * n
    queue = deque([source])
    visited[source] = True

    while queue:
        node = queue.popleft()
        for nxt in adj[node]:
            if nxt == destination:
                return True
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    return False

def displayg(n, edges, source, destination):
    print(f" Graph nodes {n}, routes are {edges}. \n Starting from {source} To destination is {destination}", end=" is ")


if __name__ == "__main__":
    # Test Case 1
    print(valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2),end=" \n\n")  # Expected: True

    # Test Case 2
    print(valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # Expected: False
    print()

    # Test Case 3
    print(valid_path(1, [], 0, 0))  # Expected: True
    print()
