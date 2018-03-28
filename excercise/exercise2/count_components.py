import bfs
import adjacencygraph
import queue
import csv
def count_components(g):
    '''Discovers all components in graph g and returns
    the components number. If graph g do not have vertices
    and edges, returns zero.

    Args:
        g (graph): Graph to claculate in.

    Returns:
        int: Integer number which is the components number of the graph g
        Components number initially sets to zero.
    '''
    todolist = g.vertices()
    count = 0
    while todolist:
        u = todolist.pop()
        for reached in bfs.breadth_first_search(g,u):
            todolist.discard(reached)
        count += 1
    return count


def read_city_graph(filename):
    '''Read all lines in csv file 'filename' and build
    a graph according to the read csv file. Return the
    builted graph. This csv file is specifically
    edmonton graph.

    Args:
        filename (:obj:`char`,name of csv file): csv
            file to read and graph.

    Returns:
        graph: undirected graph whose vertices are IDs of vertices listed
            in edmonton graph, and edges are connection of two IDs in edmonton
            graph.
    '''
    g = adjacencygraph.UndirectedAdjacencyGraph()
    with open(filename,'r')as f: #f = open('Some.csv')
        reader = csv.reader(f,delimiter=',')
        for row in reader: # reaads a line, or "row"
            if row[0] == 'V':
                g.add_vertex(row[1])
            if row[0] == 'E':
                g.add_edge((row[1],row[2]))
    return g
# number of components in Edmonton graph = 648
