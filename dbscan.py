import random
import sys

MESSAGE = f"Usage: {sys.argv[0]} -k <min_points_neighbors> -d (0 – Supremum distance | 1 – Manhattan distance | 2 – Euclidean distance ) <file_name>.txt"

def main():
    if not len(sys.argv) == 6:
        raise SystemExit(MESSAGE)

    arguments = sys.argv[1:5]

    if not arguments:
        raise SystemExit(MESSAGE)

    file_path = sys.argv[5]

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
            row.split(' ')
            columns = row.split(' ')
            point = [float(c) for c in columns[1:] if c]        
            points.append(point)
        
        print(points)
        print('randon point: {}'.format(random.choice(points)))
        
        file.close()

main()