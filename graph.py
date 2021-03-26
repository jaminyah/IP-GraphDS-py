from vertex import Vertex

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
    
    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
    
    def get_adjacent(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    
    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def dfs(self, start):
        visted, stack = set(), [start]
        adjacent = set()

        while stack:
            vertex = stack.pop()
            if vertex not in visted:
                print(f"dfs: {vertex}")
                visted.add(vertex)
                node = self.vert_dict[vertex]
                
                for n in node.get_connections():
                    adjacent.add(n.get_id())
                stack.extend(adjacent - visted)
        return visted

    def bfs(self, start):
        visted, queue = set(), [start]
        adjacent = set()
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visted:
                print(f"bfs - {vertex}")
                visted.add(vertex)
                node = self.vert_dict[vertex]

                for n in node.get_connections():
                    adjacent.add(n.get_id())
                queue.extend(adjacent - visted)
        return visted


if __name__ == "__main__":

    g = Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 0)
    g.add_edge('a', 'c', 0)
    g.add_edge('b', 'd', 0)
    g.add_edge('b', 'e', 0)
    g.add_edge('e', 'f', 0)
    g.add_edge('f', 'c', 0)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print(f"({vid}, {wid}, {v.get_weight(w)})")
    
    for v in g:
        print(f"g.vert_dict[{v.get_id()}] = {g.vert_dict[v.get_id()]}")
    
    print("depth first search")
    print(g.dfs('a'))

    print("breath first: ")
    print(g.bfs('a'))