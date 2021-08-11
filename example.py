from pkg.calculate_eps_neighborhood import calculate_eps_neighborhood
from pkg.dbscan_implementation import DbScan
from pkg.point import Point
import random

def example():

    # exemplo dados de entrada

    eps = 1
    minPts = 3
    option_calc_distance = 1

    # exemplo dados formatados

    headers = ['id', 'a', 'b']
    points = (Point('1', [0, 0]), Point('2', [1, 0]), Point('3', [1, 1]), Point('4', [2, 2]), Point('5', [3, 1]),
              Point('6', [3, 0]), Point('7', [0, 1]), Point('8', [3, 2]), Point('9', [6, 3]))

    # calculando distancia e selecionando vizinhos de cada ponto

    for i in range(len(points)):
        calculate_eps_neighborhood(
            points, points[i], eps, option_calc_distance)
        # print('id: {} neighbors: {}'.format(
        #     points[i].id, points[i].get_neighboors()))

    # algoritmo dbscan

    DbScan(points,minPts)


example()
