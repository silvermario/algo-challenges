# you can use print for debugging purposes, e.g.
# print "this is a debug message"

# Challenge requirements at https://codility.com/programmers/task/wire_burnouts/

def solution(N, A, B, C):
    # write your code in Python 2.7
    #print N,A,B,C
    grid = {}
    #x,y = 0,0

    if N == 1:
        grid[(0,0)] = [(1,0), (0,1)]
        grid[(0,1)] = [(0,0), (1,1)]
        grid[(1,0)] = [(0,0), (1,1)]
        grid[(1,1)] = [(0,1), (1,0)]
    else:
        for x in range(0,N):
            for y in range(0,N):
                if x == N -1 and y== N - 1:
                    grid[(x,y)] = [(N-2, N-1), (N-1, N-2)]
                elif x == 0 and y == 0:
                    grid[(x,y)] = [(0, 1), (1, 0)]
                elif x == 0 and y == N-1:
                    grid[(x,y)] = [(0, y - 1), ( x + 1, y)]
                elif x == N -1 and y == 0:
                    grid[(x,y)] = [(N - 2, 0), (N - 1, 1)]
                elif x == N -1:
                    grid[(x,y)] = [(N - 1, y-1), (N - 1, y + 1), (N-2, y)]
                elif y == N -1:
                    grid[(x,y)] = [(x - 1, y), (x+1, y), (x, y-1)]
                elif x == 0:
                    grid[(x,y)] = [(0, y-1), (0, y+1), (x + 1, y)]
                elif y == 0:
                    grid[(x,y)] = [(x-1, y), (x + 1, y), (x, y+1)]
                else:
                    grid[(x,y)] = [(x-1, y), (x + 1, y), (x, y+1), (x, y-1)]

    # for edge in grid:
    #     print edge, grid[edge]

    edges_to_burn = [] # [(edge_start x, edge_start y), (edge_end x, edge_end y)]
    for a,b,c in zip(A,B,C):
        if c == 0:
            edges_to_burn.append([(a,b),(a,b+1)])
        else:
            edges_to_burn.append([(a+1,b),(a,b)])

    for i,edge in enumerate(edges_to_burn):

        grid[(edge[0])].remove(edge[1])
        grid[(edge[1])].remove(edge[0])

        if not find_path(grid, (0,0), (N-1, N-1)):
            return i + 1

    #print grid
    #print edges_to_burn
    return -1

def find_path(graph, start, end, path=[]):
    path = path + [start]
    #print path
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


print solution(4, [0, 1, 1, 2, 3, 2, 1, 0, 0], [0, 1, 1, 1, 2, 2, 3, 1, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1])
