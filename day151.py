from dijkstra import dijkstra
from readfromfile import readfromfile
#rl = ['1163751742', '1381373672', '2136511328', '3694931569', '7463417111',
#      '1319128137', '1359912421', '3125421639', '1293138521', '2311944581']
rl = readfromfile("day151.txt")
rows = len(rl)
cols = len(rl[0])
tl = (0, 0)
br = (rows - 1, cols - 2)
total = 0

RIGHT = lambda row, col: True if col < cols - 1 else False
DOWN = lambda row, col: True if row < rows - 1 else False
graph = {}

def creategraph():
    for i in range(rows):
        for j in range(cols):
            connections = []
            point = (i, j)
            if RIGHT(i, j):
                connections.append(((i, j + 1),int(rl[i][j+1])))
            if DOWN(i, j):
                connections.append(((i + 1, j),int(rl[i+1][j])))
            graph[point] = connections

creategraph()
print(graph)
total = dijkstra(graph,tl,br)
print(total)
#og["s"] = [("t", 10), ("y", 5)]

print(RIGHT(0,0))