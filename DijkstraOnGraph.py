from collections import deque

'''Input is a where the graph'''

graph =[[0,0, 0, 0,'O',0,0],
        [0,5,'O',0,'O',0,0],
        [0,0,'O',0,'O',0,0],
        [0,0,'O',0,0,10,0],
        [0,0, 0, 0,'O',0,0]]

n = 7
m = 5

adjacency_matrix = {}

for i in range(m):
    for j in range(n):
        #print(i,j)
        adjacency_matrix[(i,j)] = []
        if i+1<m:
            adjacency_matrix[(i,j)].append([i+1,j])
        if i-1>=0:
            adjacency_matrix[(i,j)].append([i-1,j])
        if j-1>=0:
            adjacency_matrix[(i,j)].append([i,j-1])
        if j+1<n:
            adjacency_matrix[(i,j)].append([i,j+1])

startingX = 1
startingY = 1 
finalX = 3
finalY = 5
distance_mat = []
visited = set([])
shorted = deque([])

def calculateShortestPath(xCoordinate,yCoordinate):
    if xCoordinate == startingX and yCoordinate == startingY:
        print(xCoordinate,yCoordinate)
        return
    else:
        print(xCoordinate,yCoordinate,"-----",end = " ")
        adjacent_points = adjacency_matrix[(xCoordinate,yCoordinate)]
        listOfPoinnts = []
        for i in adjacent_points:
            dist = distance_mat[i[0]][i[1]]
            if dist!=-1:
                listOfPoinnts.append([dist,[i[0],i[1]]])
        listOfPoinnts = sorted(listOfPoinnts)
        #print(listOfPoinnts[0][1],"-----",end = " ")
        calculateShortestPath(listOfPoinnts[0][1][0],listOfPoinnts[0][1][1])

def dijkstra(x,y):
    shorted.append([x,y])
    while(len(visited)<m*n):
        
        x,y = shorted.popleft()
        if x == finalX and y == finalY:
            calculateShortestPath(x,y)
            return
        if (x,y) in visited:
            continue
        visited.add((x,y))
        adjacentpoints = adjacency_matrix[(x,y)]
        for i in adjacentpoints:

            if distance_mat[i[0]][i[1]] == -1:
                visited.add((i[0],i[1]))
            elif (i[0],i[1]) not in visited:
                shorted.append([i[0],i[1]])
                if distance_mat[i[0]][i[1]]>distance_mat[x][y]+1:
                    distance_mat[i[0]][i[1]] = distance_mat[x][y]+1
                
    
    



for i in range(m):
    col = []
    for j in range(n):
        col.append(999999)
    distance_mat.append(col)

distance_mat[startingX][startingY] = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'O':
            distance_mat[i][j] = -1

dijkstra(startingX,startingY)
print()
for i in range(m):
    print(*distance_mat[i])
