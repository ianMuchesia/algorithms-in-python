class Graph:
    def __init__(self) -> None:
        self.adjacentList = {}
        
        
    def add_vertex(self,vertex):
        if vertex not in self.adjacentList:
            self.adjacentList[vertex] = set()
            
        
    # def remove_vertex(self, vertex):
    #     if vertex not in self.adjacentList or not self.adjacentList[vertex]:
    #         return

    #     for adjacentVertex in self.adjacentList[vertex].copy():  # Use .copy() to avoid modifying the dictionary during iteration
    #         self.removeEdge(vertex, adjacentVertex)

    #     self.adjacentList[vertex].clear()

    def add_edge(self,vertex1,vertex2):
        if vertex1 not in self.adjacentList:
            self.add_vertex(vertex1)  
            
        if vertex2 not in self.adjacentList:
            self.add_vertex(vertex2)  
            
        self.adjacentList[vertex1].add(vertex2)
        self.adjacentList[vertex2].add(vertex1)   
        
    def removeEdge(self,vertex1,vertex2):
        self.adjacentList[vertex1].remove(vertex2)
        self.adjacentList[vertex2].remove(vertex1)

    def hasEdge(self,vertex1,vertex2):
            return vertex2 in self.adjacentList[vertex1] and vertex1 in self.adjacentList[vertex2]

        
    def display(self):
        for key,value in self.adjacentList.items():
            print(key, "->", [*value])
 

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")


graph.add_edge("A","B")
graph.add_edge("B","C")

graph.display()

print(graph.hasEdge("A","B"))
graph.remove_vertex("B")
graph.display()