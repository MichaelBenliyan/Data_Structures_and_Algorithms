from turtle import distance

from sqlalchemy import null


class UndirectedGraph: 
    def __init__(self, vertex_list=[], edges=[]) -> None:
        self.vertices = vertex_list
        self.adjacency_list = {}
        for vertex in self.vertices: 
            self.adjacency_list[vertex] = set()
        for edge in edges: 
            self.adjacency_list[edge[0]].add(edge[1])
            self.adjacency_list[edge[1]].add(edge[0])
            
    def add_vertex(self, vertex): 
        self.vertices.append(vertex)
        self.adjacency_list[vertex] = set()
        
    def add_edge(self, edge): 
        self.adjacency_list[edge[0]].add(edge[1])
        self.adjacency_list[edge[1]].add(edge[0])
        
    def share_edge(self, vertex_1, vertex_2): 
        return vertex_2 in self.adjacency_list[vertex_1]
    
    def all_edges(self, vertex): 
        return self.adjacency_list[vertex]
    
    def remove_vertex(self, vertex): 
        self.vertices.remove(vertex)
        del self.adjacency_list[vertex]
        for key in self.adjacency_list: 
            self.adjacency_list[key].discard(vertex)
    
    def remove_edge(self, edge):
        self.adjacency_list[edge[0]].discard(edge[1])
        self.adjacency_list[edge[1]].discard(edge[0])    
        
    def all_reachable(self, vertex): 
        pass
    
    def is_reachable(self, vertex_1, vertex_2): 
        pass
    
    def shortest_paths(self, start_vertex): 
        vertices_set = set(self.vertices)
        distance = {}
        previous = {}
        to_check = set()
        for vertex in self.vertices: 
            distance[vertex] = 9999
            to_check.add(vertex)
        distance[start_vertex] = 0
        
        while len(vertices_set) > 0: 
            min = 99999
            for vertex in vertices_set: 
                if distance[vertex] < min: 
                    min = distance[vertex]
                    min_vertex = vertex
            vertices_set.discard(min_vertex)
            for end in self.adjacency_list[min_vertex]: 
                if end in vertices_set: 
                    current = distance[min_vertex] + 1
                if current < distance[end]: 
                    distance[end] = current
                    previous[end] = min_vertex
        return distance.items()
            
            
        
        
            
        
    
vertex_list = ["a", "b", "c", "d", 'e', 'f', 'g', 'h']
edge_list = ['ac', 'cg', 'gh', 'hf', 'fb', 'be', 'eh', 'hd', 'da', 'ab']
my_graph = UndirectedGraph(vertex_list, edge_list)
print(my_graph.adjacency_list)
print(my_graph.vertices)
print("__________________________________")
print(my_graph.shortest_paths('a'))
print(my_graph.share_edge("a", "d"))
print(my_graph.share_edge("b", 'h'))
print(my_graph.all_edges("b"))
my_graph.remove_edge('hf')
print(my_graph.adjacency_list)
my_graph.remove_vertex('a')
print(my_graph.adjacency_list)
print(my_graph.vertices)


        

    
    