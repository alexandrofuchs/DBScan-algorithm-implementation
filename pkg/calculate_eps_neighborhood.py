from .distance_functions import euclidean_distance, supremun_distance, manhattan_distance
from .point import Point

def calculate_eps_neighborhood(dataset: list,  p: Point, eps: float, distance_metric: int) -> list:
    if(distance_metric == 0):
        neighbors = [point for point in dataset if supremun_distance(p.coordinate, point.coordinate) <= eps]
        return neighbors
    elif(distance_metric == 1):
        neighbors = [point for point in dataset if manhattan_distance(p.coordinate, point.coordinate) <= eps]
        return neighbors
    elif(distance_metric == 2):
        neighbors = [point for point in dataset if euclidean_distance(p.coordinate, point.coordinate) <= eps]
        return neighbors
    else:
        raise SystemExit(
"""    
    Invalid distance metric option! 
    usage: -d (Supremum distance | 1 – Manhattan distance | 2 – Euclidean distance(default))

""")