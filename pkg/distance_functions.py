import math

def euclidean_distance(p: list[float], q: list[float]):
    if(len(p) != len(q)):
        raise SystemExit("Invalid points")
    sum = 0
    for i in range(len(p)):
        sum += abs(p[i]-q[i]) ** 2
    return math.sqrt(sum)

def manhattan_distance(p: list[float], q: list[float]):
    if(len(p) != len(q)):
        raise SystemExit("Invalid points")
    sum = 0
    for i in range(len(p)):
        sum += abs(p[i]-q[i])
    return math.sqrt(sum)

def supremun_distance(p: list[float], q: list[float]):
    if(len(p) != len(q)):
        raise SystemExit("Invalid points")
    distances = []
    for i in range(len(p)):
        distances.append(abs(p[i]-q[i]))
    if(len(distances) > 0):
        return max(distances)
    else:
        raise SystemExit("Invalid points")