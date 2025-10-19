import math


def calculateDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def optimizeRoute(destinations):
    if len(destinations) <= 2:
        return destinations
    
    startPoint = destinations[0]
    otherPoints = destinations[1:]
    
    currentPoint = startPoint
    unvisitedPoints = otherPoints.copy()
    optimalRoute = []
    
    while unvisitedPoints:
        closestPoint = None
        minDistance = float('inf')
        
        for point in unvisitedPoints:
            dist = calculateDistance(currentPoint, point)
            if dist < minDistance:
                minDistance = dist
                closestPoint = point
        

        optimalRoute.append(closestPoint)
        unvisitedPoints.remove(closestPoint)
        currentPoint = closestPoint
    
    return [startPoint] + list(reversed(optimalRoute))

############################################################################

testDestinations = [(0, 0), (2, 3), (4, 1), (1, 4), (3, 5)]
optimalList = optimizeRoute(testDestinations)

print("Original:", testDestinations)
print("Optimal:", optimalList) # Optimal: [(0, 0), (4, 1), (3, 5), (1, 4), (2, 3)]