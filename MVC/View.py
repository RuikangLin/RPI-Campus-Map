from MVC.Model import Model
import plotly.graph_objects as go
import base64


class View:
    def __init__(self) -> None:
        self._campus_model = Model()

    def showGraph(self) -> None:
        # initialize filtered data
        graph_nodes = self._campus_model.getNodes()

        # initialize campus map image and get sizing
        image_source = "./resources/RPI_campus_map_2024_small.png"
        image = base64.b64encode(open(image_source, "rb").read())

        w, h = 2057, 1921

        # create edges
        edge_x = []
        edge_y = []
        for edge in self._campus_model.getEdges():
            # edge is ('id1', 'id2')
            x0, y0 = self._campus_model.getCoord(edge[0])
            x1, y1 = self._campus_model.getCoord(edge[1])
            # add offsets
            edge_x.append(x0 - 48)
            edge_x.append(x1 - 48)
            edge_x.append(None)
            edge_y.append(1921 - y0 + 67)
            edge_y.append(1921 - y1 + 67)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=2, color="#8B0000"),
            hoverinfo="none",
            mode="lines",
        )

        # added pixel offset
        node_x = [item[2] - 48 for item in graph_nodes]
        node_y = [1921 - item[3] + 67 for item in graph_nodes]

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers",
            hoverinfo="text",
            marker=dict(
                # showscale=True,
                # colorscale options
                #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale="Greys",
                reversescale=False,
                color=[],
                size=10,
                # colorbar=dict(
                #     thickness=15,
                #     title='Node Connections',
                #     xanchor='left',
                #     titleside='right'
                # ),
                line_width=2,
            ),
        )

        # color node points
        node_adjacencies = [
            self._campus_model.getDegree(item[1]) for item in graph_nodes
        ]
        node_text = [
            f"{item[1]}<br>{item[0]}<br># degrees: {self._campus_model.getDegree(item[1])}"
            for item in graph_nodes
        ]

        node_trace.marker.color = node_adjacencies
        node_trace.text = node_text

        # create network graph
        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title="<br>Network graph made with Python",
                titlefont_size=16,
                showlegend=False,
                hovermode="closest",
                margin=dict(b=60, l=5, r=5, t=60),
                annotations=[
                    dict(text="", showarrow=False, xref="x", yref="y", x=0, y=0)
                ],
                xaxis=dict(
                    showgrid=True,
                    zeroline=True,
                    showticklabels=True,
                    gridwidth=1,
                    gridcolor="black",
                    linewidth=1,
                    linecolor="black",
                    mirror=True,
                ),
                yaxis=dict(
                    showgrid=True,
                    zeroline=True,
                    showticklabels=True,
                    gridwidth=1,
                    gridcolor="black",
                    linewidth=1,
                    linecolor="black",
                    mirror=True,
                ),
            ),
        )

        # add campus map image in background
        fig.add_layout_image(
            dict(
                source="data:image/png;base64,{}".format(image.decode()),
                xref="x",
                yref="y",
                x=0,
                y=h,
                sizex=w,
                sizey=h,
                xanchor="left",
                yanchor="top",
                sizing="stretch",
                opacity=0.8,
                layer="below",
            )
        )

        # adjust range
        fig.update_layout(
            xaxis_range=[0, w], yaxis_range=[0, h], template="plotly_white"
        )

        fig.show(config={"displayModeBar": False})

    def getGraph(self) -> str:
        # initialize filtered data
        graph_nodes = self._campus_model.getNodes()

        # initialize campus map image and get sizing
        image_source = "./resources/RPI_campus_map_2024_small.png"
        image = base64.b64encode(open(image_source, "rb").read())

        w, h = 2057, 1921

        # create edges
        edge_x = []
        edge_y = []
        for edge in self._campus_model.getEdges():
            # edge is ('id1', 'id2')
            x0, y0 = self._campus_model.getCoord(edge[0])
            x1, y1 = self._campus_model.getCoord(edge[1])
            # add offsets
            edge_x.append(x0 - 48)
            edge_x.append(x1 - 48)
            edge_x.append(None)
            edge_y.append(1921 - y0 + 67)
            edge_y.append(1921 - y1 + 67)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=2, color="#8B0000"),
            hoverinfo="none",
            mode="lines",
        )

        # added pixel offset
        node_x = [item[2] - 48 for item in graph_nodes]
        node_y = [1921 - item[3] + 67 for item in graph_nodes]

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers",
            hoverinfo="text",
            marker=dict(
                # showscale=True,
                # colorscale options
                #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale="Greys",
                reversescale=False,
                color=[],
                size=10,
                # colorbar=dict(
                #     thickness=15,
                #     title='Node Connections',
                #     xanchor='left',
                #     titleside='right'
                # ),
                line_width=2,
            ),
        )

        # color node points
        node_adjacencies = [
            self._campus_model.getDegree(item[1]) for item in graph_nodes
        ]
        node_text = [
            f"{item[1]}<br>{item[0]}<br># degrees: {self._campus_model.getDegree(item[1])}"
            for item in graph_nodes
        ]

        node_trace.marker.color = node_adjacencies
        node_trace.text = node_text

        # create network graph
        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title="<br>Network graph made with Python",
                titlefont_size=16,
                showlegend=False,
                hovermode="closest",
                margin=dict(b=60, l=5, r=5, t=60),
                annotations=[
                    dict(text="", showarrow=False, xref="x", yref="y", x=0, y=0)
                ],
                xaxis=dict(
                    showgrid=True,
                    zeroline=True,
                    showticklabels=True,
                    gridwidth=1,
                    gridcolor="black",
                    linewidth=1,
                    linecolor="black",
                    mirror=True,
                ),
                yaxis=dict(
                    showgrid=True,
                    zeroline=True,
                    showticklabels=True,
                    gridwidth=1,
                    gridcolor="black",
                    linewidth=1,
                    linecolor="black",
                    mirror=True,
                ),
            ),
        )

        # add campus map image in background
        fig.add_layout_image(
            dict(
                source="data:image/png;base64,{}".format(image.decode()),
                xref="x",
                yref="y",
                x=0,
                y=h,
                sizex=w,
                sizey=h,
                xanchor="left",
                yanchor="top",
                sizing="stretch",
                opacity=0.8,
                layer="below",
            )
        )

        # adjust range
        fig.update_layout(
            xaxis_range=[0, w], yaxis_range=[0, h], template="plotly_white"
        )

        fig.to_html(config={"displayModeBar": False, "full_html": False})