''' # Name: Adit Hasan Student ID: 1459800
    # Name: QIUFENG DU Student ID: 1439484

    With MinHeap and AdjacencyGraph in the same directory,
    this script can be run from the command line with the
    command: python3 server.py. The server can be interacted
    with sending requests in the format
    R <coordinateA1> <coordinateA2> <coordinateB1> <coordinateB2>
    and then pressing enter. Waypoints would be provided one at a
    time and requires Acknowledgement "A" everytime.
'''

import sys
import csv
import math
from adjacencygraph import AdjacencyGraph
import queue
import heapq
vertex_coord = {}

def read_city_graph(filename):
    '''Takes the provided CSV file containing the information about
        Edmonton map and contructs an Undirected Graph

    Args:
        filename (CSV_file_name): The file containing the data

    Returns:
        g (graph): The undirected graph
    '''

    g = AdjacencyGraph()
    # opens the file to be read
    with open(filename) as csvfile:
        # separates the file into values
        csv_input = csv.reader(csvfile, delimiter=',')
        for row in csv_input:
            # If first character of line is V add vertex
            if row[0] == 'V':
                g.add_vertex(int(row[1]))
            # If first character of line is E add edge
            elif row[0] == 'E':
                g.add_edge((int(row[1]), int(row[2])))
    return g


def read_vertex_coord(filename):
    '''stores all vertex coordinates in a dict file with format
        (vertex ID): (coordinate1, coordinate2)

    Args:
        filename (CSV_file_name): The file containing the data

    Returns:
        vertex_coord (dict): The dictionary containing the coordinates
    '''

    # stores all vertex coordinates in a dict file with format
    # (vertex ID): (coordinate1, coordinate2)
    vertex_coord = dict()
    with open(filename) as csvfile:
        csv_input = csv.reader(csvfile, delimiter=',')
        for row in csv_input:
            if row[0] == 'V':
                vertex_coord[int(row[1])] = (int(float(row[2])*100000), int(float(row[3])*100000))
                vertex_coord [int(row[1])] = (int(float(row[2])*100000), int(float(row[3])*100000))
            else:
                continue
    return vertex_coord

def cost_distance(u, v):
    '''Computes and returns the straight-line distance between the two
    vertices u and v.
    Args:
    u, v: The ids for two vertices that are the start and
    end of a valid edge in the graph.
    Returns:
    numeric value: the distance between the two vertices.
    '''
    term_a = (vertex_coord[u][0]-vertex_coord[v][0])**2
    term_b = (vertex_coord[u][1]-vertex_coord[v][1])**2
    return (term_b + term_a)**(0.5)

def read_street_names(filename):
    '''Stores all edge street names in a dict file with format
    (starting vertex, ending vertex) : Street Name
    Args:
        filename (CSV_file_name): The file containing the data
    Returns:
        vertex_coord (dict): The dictionary containing the coordinates
    '''
    # stores all edge street names in a dict file with format
    # (starting vertex, ending vertex) : Street Name
    street_names = dict()
    with open(filename) as csvfile:
        csv_input = csv.reader(csvfile, delimiter=',')
        for row in csv_input:
            if row[0] == 'E':
                street_names[(int(row[1]), int(row[2]))] = (row[3])
            else:
                continue
    return street_names

g = read_city_graph("edmonton-roads-2.0.1.txt")
street_names = read_street_names("edmonton-roads-2.0.1.txt")
vertex_coord = read_vertex_coord("edmonton-roads-2.0.1.txt")


def least_cost_path(graph, start, dest, cost):
    """Find and return a least cost path in graph from start
    vertex to dest vertex.
    Efficiency: If E is the number of edges, the run-time is
    O( E log(E) ).
    Args:
    graph (Graph): The digraph defining the edges between the
    vertices.
    start: The vertex where the path starts. It is assumed
    that start is a vertex of graph.
    dest:  The vertex where the path ends. It is assumed
    that start is a vertex of graph.
    cost:  A function, taking the two vertices of an edge as
    parameters and returning the cost of the edge. For its
    interface, see the definition of cost_distance.
    Returns:
    list: A potentially empty list (if no path can be found) of
    the vertices in the graph. If there was a path, the first
    vertex is always start, the last is always dest in the list.
    Any two consecutive vertices correspond to some
    edge in graph.
    """
    reached = {}
    runners = [(0,start,start)]
    while len(runners) != 0:
        path = []
        A = heapq.heappop(runners)
        (time,goal,start_inside) = A
        if goal in reached:
            continue
        reached[goal] = (start_inside,time)
        if goal == dest:
            key = dest
            while key != start:
                path.append(key)
                key = reached[key][0]
            path.append(key)
            # return path in right order
            return path[::-1]
        for succ in graph.neighbours(goal):
            heapq.heappush(runners,(time+cost(goal,succ),succ,goal))
    return []


def check_cloest_point(u,v):
    '''check the cloest vertices regards to the request coordinates
    u is the latitude of request point
    v is the longitude of request point
    reutrn cloest id with its coordinates
    '''
    short = len(g.vertices())
    cloest = None
    for w,[x,y] in vertex_coord.items():
        dis = ((x-u)**2+(y-v)**2)**0.5
        if dis < short:
            short = dis
            cloest = w
    return cloest


def connect(g,r):
    '''connect the arduino
    g is the graph read from the csv file
    r is the request sent from arduino
    it should look like a statemachine
    '''
    low_cost = least_cost_path(g, check_cloest_point(r[1],r[2]), check_cloest_point(r[3],r[4]), cost_distance)
    waypoints = len(low_cost)
    print('N',waypoints)
    if input() != 'A':
        print("Acknowledgement not received")
    if waypoints >= 0:
        for v in low_cost:
            print('W',vertex_coord[v][0],vertex_coord[v][1])
            if input() != 'A':
                break
        print('E')

if __name__ == "__main__":
    #state machine
    while True:
        request = input().split()
        if request[0] == 'R':
            if len(request) == 5:
                for i in range(1, 5):
                    request[i] = int(request[i])
                connect(read_city_graph("edmonton-roads-2.0.1.txt"),request)
                break
