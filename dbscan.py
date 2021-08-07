import random
import sys

MESSAGE = f"""

Usage: {sys.argv[0]} -k <value> -e <eps_value> -d <option_value> <file_name>.txt

-e : Eps, Maximum radius of the neighborhood
-d : Distance Function, 0 – Supremum distance | 1 – Manhattan distance | 2 – Euclidean distance
-k : MinPts, Minimum number of points in an Eps-neighbourhood

"""

def distance_function(option: int, p: list[float], q:list[float]):
    if(option == 0):
        print(" steps... ")
    if(option == 1):
        print(" steps... ")
    if(option == 1):
        print(" steps... ")

def DbScan(dataset: list, choose_point: list, eps: float, minPts: int):
    print("alg steps...")

def validade_args(args: list[str]):
    if not args[0] == '-k' or not args[1].isnumeric():
        raise SystemExit(MESSAGE)
    if not args[2] == '-e' or not args[3].isnumeric():
        raise SystemExit(MESSAGE)
    if not args[4] == '-d' or not args[5].isnumeric():
        raise SystemExit(MESSAGE)

def main():
    if not len(sys.argv) == 8:
        raise SystemExit(MESSAGE)

    arguments = sys.argv[1:7]

    if not arguments:
        raise SystemExit(MESSAGE)
    validade_args(arguments)

    file_path = sys.argv[7]

    if not file_path:
        raise SystemExit(MESSAGE)        
    
    try:
        file = open(file_path, 'r')

    except TypeError:
        raise SystemExit(MESSAGE)

    if not file:
        raise SystemExit(MESSAGE) 
    else:
        headers = file.readline()
        print(headers)
        points = []
        for row in file:
            columns = row.split(' ')
            point = [float(c) for c in columns[1:] if c]        
            points.append(point)
        
        print("points: {}".format(points))

        minPts = arguments[1]
        eps = arguments[3]
        distance_function = arguments[5]
        
        core_points = []
        border_points = []
        noise = []

        DbScan(points, random.choice(points), eps, minPts)

        file.close()

main()