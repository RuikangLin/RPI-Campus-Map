import csv, math
from ADT.Graph import Graph


class CampusParser:
    @staticmethod
    def readNodes(
        filename: str,
        x_data: list[int],
        y_data: list[int],
        BuildingToID: dict[str, str],
        IDtoBuilding: dict[str, str],
        graph: Graph,
    ) -> None:
        try:
            with open(filename, newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                count = 1
                for row in reader:
                    if len(row) != 4:
                        raise IOError(
                            f"Invalid Row Length: expected '4' vs. actual '{len(row)}'"
                        )

                    # row formatted by csv and delimiter
                    name = row[0]
                    id = row[1]
                    x = int(row[2])
                    y = int(row[3])

                    # NOTE that blank names in the csv file are intersections
                    if len(name) == 0:
                        name = f"Intersection {id}"

                    # skips ids that does not exist
                    # NOTE that x&y list requires the csv file to be sorted by id ascending
                    while count <= int(id):
                        x_data.append(-1)
                        y_data.append(-1)
                        count += 1

                    # allocate values
                    x_data.append(x)
                    y_data.append(y)
                    BuildingToID[name] = id
                    IDtoBuilding[id] = name
                    graph.addNode(id)

                    count += 1

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    @staticmethod
    def readEdges(
        filename: str,
        x_data: list[int],
        y_data: list[int],
        BuildingToID: dict[str, str],
        IDtoBuilding: dict[str, str],
        csv_edges: list[tuple[str,str]],
        graph: Graph,
    ) -> None:
        try:
            with open(filename, newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for row in reader:
                    if len(row) != 2:
                        raise IOError(
                            f"Invalid Row Length: expected '2' vs. actual '{len(row)}'"
                        )

                    # row formatted by csv and delimiter
                    id1 = row[0]
                    id2 = row[1]

                    # if building id doesn't exist, continue
                    if not id1 in IDtoBuilding or not id2 in IDtoBuilding:
                        continue

                    # calculate euclidean distances
                    delta_x_sqr = (x_data[int(id2)] - x_data[int(id1)]) * (
                        x_data[int(id2)] - x_data[int(id1)]
                    )
                    delta_y_sqr = (y_data[int(id2)] - y_data[int(id1)]) * (
                        y_data[int(id2)] - y_data[int(id1)]
                    )
                    dist = math.sqrt(delta_x_sqr + delta_y_sqr)

                    # add bidirectional edges
                    graph.addEdge(id1, id2, dist)
                    graph.addEdge(id2, id1, dist)

                    # store row/edge for easier access later
                    csv_edges.append(row)

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
