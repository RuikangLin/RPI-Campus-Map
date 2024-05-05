import heapq
from ADT.Graph import Graph
from MVC.CampusParser import CampusParser


class Model:
    def __init__(self) -> None:
        # node: building id, label: euclidean distance from building to building
        self._campus_graph = Graph(str, float)

        # key/value: building/id (strings)
        self._BuildingToID = {}
        self._IDToBuilding = {}

        # parallel arraylist of x, y coordinates of index ids (integer)
        self._x = []
        self._y = []

        # edges information in list of tuples like the csv file
        self._csv_edges = []

        # create graph
        CampusParser.readNodes(
            "data/RPI_map_data_Nodes.csv",
            self._x,
            self._y,
            self._BuildingToID,
            self._IDToBuilding,
            self._campus_graph,
        )
        CampusParser.readEdges(
            "data/RPI_map_data_Edges.csv",
            self._x,
            self._y,
            self._BuildingToID,
            self._IDToBuilding,
            self._csv_edges,
            self._campus_graph,
        )
    
    def getX(self) -> list[int]:
        return self._x.copy()
    
    def getY(self) -> list[int]:
        return self._y.copy()
    
    # return a node's edge euclidean distance
    def getDistance(self, parent: str, child: str) -> float:
        for path in self._campus_graph.getEdgeList(parent):
            if path[0] == child:
                return path[1]
        return -1

    # return a node's outgoing edges
    def getDegree(self, node: str) -> int:
        return len(self._campus_graph.getEdgeList(node))
        
    # return a coord (x,y) of a str id
    def getCoord(self, node: str) -> tuple[int, int]:
        return (self._x[int(node)], self._y[int(node)])

    # return list of nodes like csv format (name, id, x, y)
    def getNodes(self) -> list[tuple[str, str, int, int]]:
        return [(k, v, self._x[int(v)], self._y[int(v)]) for k, v in self._BuildingToID.items()]

    # return list of edges like csv format
    def getEdges(self) -> list[tuple[str,str]]:
        return self._csv_edges.copy()

    def findPath(self, id1: str, id2: str) -> list[tuple[str,float]]:
        active = []
        heapq.heapify(active)
        finished = []

        init_path = []
        init_path.append((id1, 0.0))
        heapq.heappush(active, MinPath(init_path))

        while len(active) > 0:
            min_path = heapq.heappop(active)
            min_dest = min_path[len(min_path) - 1][0]

            if min_dest == id2:
                return min_path
            
            if min_dest in finished:
                continue

            paths = self._campus_graph.getEdgeList(min_dest)
            for i in range(len(paths)):
                child = (paths[i][0], paths[i][1])

                if not child[0] in finished:
                    new_path = min_path.copy()
                    new_path.append(child)

                    heapq.heappush(active, MinPath(new_path))
            
            finished.append(min_dest)
        
        return init_path
    
class MinPath(list):
    def __lt__(self, other):
        sum1 = 0.0
        for i in range(len(self)):
            sum1 += self[i][1]
        sum2 = 0.0
        for i in range(len(other)):
            sum2 += other[i][1]
        return sum1 < sum2