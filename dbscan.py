from pkg.calculate_eps_neighborhood import calculate_eps_neighborhood
from pkg.point import Point
import sys

MESSAGE = f"""

Usage: {sys.argv[0]} -k <value> -e <eps_value> -d <option_value> <file_name>.txt

-e : Eps, Maximum radius of the neighborhood
-d : Distance Function, 0 – Supremum distance | 1 – Manhattan distance | 2 – Euclidean distance
-k : MinPts, Minimum number of points in an Eps-neighbourhood

"""

def validade_args(args: list[str]):
    if not args[0] == '-k' or not args[1].isnumeric():
        raise SystemExit(MESSAGE)
    if not args[2] == '-e' or not args[3].isnumeric():
        raise SystemExit(MESSAGE)
    if not args[4] == '-d' or not args[5].isnumeric():
        raise SystemExit(MESSAGE)

def main():

    # valida numero de argumentos

    if not len(sys.argv) == 8:
        raise SystemExit(MESSAGE)

    arguments = sys.argv[1:7]

    # valida parametros

    if not arguments:
        raise SystemExit(MESSAGE)
    validade_args(arguments) 

    # valida arquivo

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
        points = []
        for row in file:
            columns = row.split(' ')
            id = columns[0]
            coordinate = [float(c) for c in columns[1:] if c]        
            points.append(Point(id, coordinate))
        
        # dados formatados 
        
        print("headers: {}".format(headers))

        for point in points:
            print(point)

        file.close()

main()