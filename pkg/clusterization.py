from pkg.calculate_eps_neighborhood import calculate_eps_neighborhood
from pkg.point import Point

def DbScan(points: list, eps: float, distance_metric: int, minPts: int) -> list:
    i = 0
    for point in points:
        if point.cluster_id != None: # point has already been processed
            continue
        point.neighbors = calculate_eps_neighborhood(points, point, eps, distance_metric)
        if len(point.neighbors) < minPts: # if is not a core point
            point.cluster_id = "Noise"
            continue
        i += 1 
        point.cluster_id = f"g{i}"  # if is a core point set a cluster
        seeds = list(point.neighbors)
        seeds.remove(point)
        for seed in seeds: # para cada vizinho adicionar ao cluster se ja processado como (Noise) e é vizinho
            if seed.cluster_id == "Noise":
                seed.cluster_id = point.cluster_id
            if seed.cluster_id != None: # 
                continue
            seed.cluster_id = point.cluster_id
            neighbors = calculate_eps_neighborhood(points, seed, eps, distance_metric)
            if len(neighbors) >= minPts:
                seeds += neighbors


        

