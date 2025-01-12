class Graph:
    def bfs_path(self, start, end):
        
        visited = []
        to_visit = [start]
        path = {start: None}
        
        while to_visit:
            current_vertex = to_visit.pop(0)
            visited.append(current_vertex)

            if current_vertex == end:
                shortest_path = []
                while current_vertex is not None:
                    shortest_path.append(current_vertex)
                    current_vertex = path[current_vertex]
                shortest_path.reverse()
                return shortest_path
            
            neighbors = sorted(self.graph[current_vertex])
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    path[neighbor] = current_vertex
        return None

# first solution
#    def bfs_path(self, start, end):
#        
#        reached = []
#        to_reach = [start]
#        paths = [[start]]
#        
#        while end not in to_reach and len(to_reach) > 0:
#        
#            just_reached = to_reach.pop(0)
#            reached.append(just_reached)
#            neighbors = sorted(self.graph[just_reached])
#
#            for path in paths:
#                if path[-1] == just_reached:
#                    for neighbor in neighbors:
#                        if neighbor not in path:
#                            newpath = path.copy()
#                            newpath.append(neighbor)
#                            paths.append(newpath)
#                    paths.remove(path)
#
#            for neighbor in neighbors:
#                if neighbor not in reached and neighbor not in to_reach:
#                    to_reach.append(neighbor)
#
#        for path in paths:
#            if path[0] == start and path[-1] == end:
#                return path


    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

