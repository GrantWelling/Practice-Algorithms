class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def breadthFirstSearch(self, start):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.pop(0)
            print(start, end=" ")
            for i in self.graph[start]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True


# Test code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
g.breadthFirstSearch(2)
print()

