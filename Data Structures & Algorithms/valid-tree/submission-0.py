class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Constrains:
        # n >= 1
        # Nodes are labeled from 0 to n-1
        # no duplicate edges or self-loops

        '''
        Step 1: Build an adjacency list
        Step 2: run dfs from node 0 to detect cycles
        step 3: check connectivity
        '''
        graph = []
        for _ in range(n):
            graph.append([])

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n