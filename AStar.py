#!/usr/bin/env python
""" 
L ist die Anzahl der Ebenen des Labyrinths.
R ist die Länge des Labyrinths, und C die Breite.
"""

from __future__ import annotations
import heapq
import collections
from typing import Protocol, Dict, List, Iterator, Tuple, TypeVar, Optional
T = TypeVar('T')


GridLocation = Tuple[int, int, int]
Location = Tuple[int, int, int]

class SquareGrid:        # Struct of the diagram and the relevant functions
    def __init__(self, width: int, height: int, depth: int):
        self.width = width
        self.height = height
        self.depth = depth
        self.walls: List[GridLocation] = []

    def in_bounds(self, id: GridLocation) -> bool:
        (x, y, z) = id
        return 0 <= x < self.width and 0 <= y < self.height and 0 <= z < self.depth

    def passable(self, id: GridLocation) -> bool:
        if id in self.walls:
            return False
        else:
            return True

    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        (x, y, z) = id
        neighbors = [(x+1, y, z), (x-1, y, z), (x, y-1, z),
                     (x, y+1, z), (x, y, z+1), (x, y, z-1)]
        # E W N S UP DOWN

        results1 = filter(self.passable, neighbors)
        results = filter(self.in_bounds, results1)
        return results

class PriorityQueue:      # The Priority of all elements
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]

def heuristic(a: GridLocation, b: GridLocation) -> float:   #Count the mannhaton distance
    (x1, y1, z1) = a
    (x2, y2, z2) = b
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

def a_star_search(graph, start, goal):  #A* Search
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: Dict[Location, Optional[Location]] = {}
    cost_so_far: Dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1      # graph.cost(current, next) no weight
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

def split(word): # split an input line into characters
    return [char for char in word]


# main loop function till three zeros are input
while True:
    L = int(input("Enter number of levels: ")) 
    R = int(input("Enter number of length: "))
    C = int(input("Enter number of width: "))

    if L==R==C==0:
        break

    arr = [[[0 for col in range(C)]for row in range(R)] for x in range(L)]
    DIAGRAM1_WALLS = []
    start = (0, 0, 0)
    goal = (0, 0, 0)

    for i in range(L):
        print("\nPlease input the " + str(i) + "th Level: ")
        j = 0
        while j < R:
            line = input()
            if line:                                
                arr[i][j][:] = split(line)
                j += 1

                


    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    start = (k, j, i)       
                elif arr[i][j][k] == 'E':
                    goal = (k, j, i)
                elif arr[i][j][k] == '#':
                    DIAGRAM1_WALLS.append((k, j, i))

    g = SquareGrid(C, R, L)
    g.walls = DIAGRAM1_WALLS
    came_from, cost_so_far = a_star_search(g, start, goal)

    try:
        print("Entkommen in " + str(cost_so_far[goal]) + "  Minute(n)!")
    except:
        print("Gefangen :-(")


# TODO: check the existence of S and E; Limit the input of each column;