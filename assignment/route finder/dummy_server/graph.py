class Graph:
    '''Representing a directed graph.

    Attributes:
        vertices (set): Identifiers of vertices of the graph.
        edges (list): Pairs of vertex identifiers of the graph.

    Invariant:
        Every identifier mentioned in an edge either as a source or a target
        must be in vertices.
    '''

    def __init__(self):
        self.vertices = set()
        self.edges = list()

    def add_vertex(self, v):
        '''Adds a vertex represented by identifier v to the graph.

        Args:
            v (hashable): Identifier of the vertex to be added.
        '''
        self.vertices.add(v)
        # return self

    def is_vertex(self, v):
        '''Returns True if v is a vertex of the graph.

        Args:
            v (hashable): Identifier to be checked.
        '''
        return v in self.vertices

    def add_edge(self, e):
        '''Adds an edge to the graph.

        Args:
            e (pair of vertices): Specifies the edge pointing from e[0] to e[1]
                to be added to the graph.

        Raises:
            RuntimeError when either e[0] or e[1] is not a vertex of the graph.
        '''
        if len(e) != 2:
            raise RuntimeError(
                "Illegal argument: len(e)=={}, should be 2.".format(len(e)))
        if e[0] not in self.vertices:
            raise RuntimeError(
                "Illegal argument: e[0]={} is not a vertex.".format(e[0]))
        if e[1] not in self.vertices:
            raise RuntimeError(
                "Illegal argument: e[0]={} is not a vertex.".format(e[1]))
        self.edges.append(e)

    def check_invariant(self):
        '''Checks the invariants that objects of class Graph have to maintain.

        For details, see the class documentation.

        Returns:
            bool: True when self satisfies the invariants.
        '''
        for e in self.edges:
            if e[0] not in self.vertices:
                return False
            if e[1] not in self.vertices:
                return False
        return True


def is_walk(graph, vertices):

    if not vertices:
        return False

    for x in range(len(vertices)):
        if not graph.is_vertex(vertices[x]):
            return False
        if x > 0 and x < len(vertices):
            if (vertices[x], vertices[x+1]) not in graph.edges:
                return False

    return True


def is_path(graph, vertices):
    '''Checks whether the vertices mentioned form a path in the graph.

    Recall that a path is a walk with no repeated vertices.

    Args:
        graph (Graph): the graph to check against.
        vertices (Iterable): identifiers that define the supposed path.

    Returns
        bool: True when vertices specifies a path in graph.
    '''
    return False
