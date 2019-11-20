from collections import deque
import socket
import asyncio


class DijkstraGraph:

    def __init__(self,starting,ending,obstacles):
        self.row = 30
        self.column = 40
        self.startingX = starting[0]
        self.startingY = starting[1]
        self.finalX = ending[0]
        self.finalY = ending[1]
        self.obstacles = obstacles
        self.complete = 0

        self.adjacency_matrix = {}
        self.distance_mat = []
        self.visited = set([])
        self.shorted = deque([])
        self.shortestPath = []

        for i in range(self.row):
            for j in range(self.column):

                self.adjacency_matrix[(i,j)] = []
                if i+1<self.row:
                    self.adjacency_matrix[(i,j)].append([i+1,j])
                if i-1>=0:
                    self.adjacency_matrix[(i,j)].append([i-1,j])
                if j-1>=0:
                    self.adjacency_matrix[(i,j)].append([i,j-1])
                if j+1<self.column:
                    self.adjacency_matrix[(i,j)].append([i,j+1])

        self.distance_mat = [[9999999]*self.column for i in range(self.row)]

        self.distance_mat[self.startingX][self.startingY] = 0

        for i in range(self.row):
            for j in range(self.column):
                if [i,j] in self.obstacles:
                    self.distance_mat[i][j] = -1

        self.dijkstra(self.startingX,self.startingY)

    def calculateShortestPath(self,xCoordinate,yCoordinate):
        if xCoordinate == self.startingX and yCoordinate == self.startingY:
            self.shortestPath.append([xCoordinate,yCoordinate])
            return
        else:
            self.shortestPath.append([xCoordinate,yCoordinate])
            adjacent_points = self.adjacency_matrix[(xCoordinate,yCoordinate)]
            listOfPoinnts = []
            for i in adjacent_points:
                dist = self.distance_mat[i[0]][i[1]]
                if dist!=-1:
                    listOfPoinnts.append([dist,[i[0],i[1]]])
            listOfPoinnts = sorted(listOfPoinnts)
            self.calculateShortestPath(listOfPoinnts[0][1][0],listOfPoinnts[0][1][1])

    def dijkstra(self,x,y):
        self.shorted.append([x,y])
        while(len(self.visited)<self.row*self.column):
            
            if len(self.shorted) == 0:
                return
            x,y = self.shorted.popleft()
            if x == self.finalX and y == self.finalY:
                self.complete = 1
                self.calculateShortestPath(x,y)
                return
            if (x,y) in self.visited:
                continue
            self.visited.add((x,y))
            adjacentpoints = self.adjacency_matrix[(x,y)]
            
            for i in adjacentpoints:
                
                if self.distance_mat[i[0]][i[1]] == -1:
                    self.visited.add((i[0],i[1]))
                elif (i[0],i[1]) not in self.visited:
                    self.shorted.append([i[0],i[1]])
                    if self.distance_mat[i[0]][i[1]]>self.distance_mat[x][y]+1:
                        self.distance_mat[i[0]][i[1]] = self.distance_mat[x][y]+1

#obj = DijkstraGraph([1,1],[3,5],[[0,3],[1,3],[2,3],[3,3]])