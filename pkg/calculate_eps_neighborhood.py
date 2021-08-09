from .distance_functions import euclidean_distance, supremun_distance, manhattan_distance
from .point import Point

def calculate_eps_neighborhood(dataset: list[Point],  p: Point, eps: float, option_fun_distance: int) -> list[Point]:
    if(option_fun_distance == 0):
        neighbors = [point for point in dataset if supremun_distance(p.coordinate, point.coordinate) <= eps]
        p.neighbors = neighbors
    elif(option_fun_distance == 1):
        neighbors = [point for point in dataset if manhattan_distance(p.coordinate, point.coordinate) <= eps]
        p.neighbors = neighbors
    elif(option_fun_distance == 2):
        neighbors = [point for point in dataset if euclidean_distance(p.coordinate, point.coordinate) <= eps]
        p.neighbors = neighbors
    else:
        raise SystemExit('invalid distance function option! usage: -d (0 | 1 | 2)')