class Graph:
    def __init__(self, K, V) -> None:
        self._K = K
        self._V = V
        self._graph = {}

    def __str__(self) -> str:
        return str(self._graph)

    def print(self) -> None:
        for key, value in self._graph.items():
            print(f"{key} -> {value}")

    def checkNodeRep(self, node) -> bool:
        return isinstance(node, self._K)

    def checkLabelRep(self, label) -> bool:
        return isinstance(label, self._V)

    def addNode(self, node) -> None:
        if self.checkNodeRep(node):
            self._graph[node] = []
        else:
            raise TypeError(
                f"Unmatching Node Type: expected '{self._K}' vs. actual '{type(node)}'\n\tFor node: '{node}'\n"
            )

    def addEdge(self, parent, child, label) -> None:
        error = ""
        if not self.checkNodeRep(parent):
            error += f"Unmatching Parent Node Type: expected '{self._K}' vs. actual '{type(parent)}'\n\tFor parent node: '{parent}'\n"
        if not self.checkNodeRep(child):
            error += f"Unmatching Child Node Type: expected '{self._K}' vs. actual '{type(child)}'\n\tFor child node: '{child}'\n"
        if not self.checkLabelRep(label):
            error += f"Unmatching Label Type: expected '{self._V}' vs. actual '{type(label)}'\n\tFor label: '{label}'\n"
        if len(error) > 0:
            raise TypeError(error)
        self._graph[parent].append((child, label))

    def getEdgeList(self, node) -> list:
        return self._graph[node]
