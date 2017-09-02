import math

def getX(index):
    return int(index) % 15
def getY(index):
    return int(index) / 15

def AStarSearch(start, end, map):
    closedList = [0]*300
    openSet = []
    openSet.append(start)
    cameFrom = [-1]*300

