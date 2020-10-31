#!/usr/bin/python3
import argparse
import sys
from random import randrange

def print_1(G):
    for x in range(len(G)):
        buf = ""
        for y in range(len(G[x])):
            buf += str(G[x][y]) + " "
        buf = buf[:-1]
        print(buf)

# function: generates a directed graph with V vertices, E edges, where each vertex has indegree I
# params: vertices,edges,indegree
def generate_graph_1(V,E,I):
    G = [[0 for x in range(V)] for y in range(V)]

    # add edges to meet indegree constraint 
    E1 = 0
    for x in range(V):
        xdeg = 0
        while xdeg < I:
            y = randrange(V)
            if y != x and G[y][x] != 1:
                E1 += 1
                G[y][x] = 1
                xdeg += 1

    # add more edges to reach E 
    while E1 < E:
        x = randrange(V)
        y = randrange(V)
        if G[x][y] != 1:
            G[x][y] = 1
            E1 += 1

    print_1(G)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('--indegree' , type=int, help='indegree of each node')
    parser.add_argument('--vertices' , type=int, help='number of vertices for the graph')
    parser.add_argument('--edges'    , type=int, help='number of edges for the graph')
    args = parser.parse_args(sys.argv[1:])
    generate_graph_1(int(args.vertices),int(args.edges),int(args.indegree))


