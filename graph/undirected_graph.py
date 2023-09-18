class Graph:
    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}

    def __str__(self) -> str:
        return str(self.__dict__)

    def add_vertex(self, node):
        self.adjacentlist[node] = []
        self.numberofnodes += 1

    def add_edge(self, node1, node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)

    def showconnection(self):
        for vertex, neighbors in self.adjacentlist.items():
            print("%s --> %s" % (vertex, neighbors))


if __name__ == "__main__":
    myGraph = Graph()
    myGraph.add_vertex("0")
    myGraph.add_vertex("1")
    myGraph.add_vertex("2")
    myGraph.add_vertex("3")
    myGraph.add_vertex("4")
    myGraph.add_vertex("5")
    myGraph.add_vertex("6")
    myGraph.add_edge("3", "1")
    myGraph.add_edge("3", "4")
    myGraph.add_edge("4", "2")
    myGraph.add_edge("4", "5")
    myGraph.add_edge("1", "2")
    myGraph.add_edge("1", "0")
    myGraph.add_edge("0", "2")
    myGraph.add_edge("6", "5")
    print(myGraph)
    myGraph.showconnection()
