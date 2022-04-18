class Solution:
            
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = { i: set() for i in range(n) }
        
        for edge in edges:
            one, two = edge
            graph[one].add(two)
            graph[two].add(one)
            
        q = deque([source])
        visited = []
        
        while q:
            current = q.popleft()
            if current == destination:
                return True
            if current in visited:
                continue
            visited.append(current)
            for node in graph[current]:
                q.append(node)
        
        return False