import random
import sys

MESSAGE = f"Usage: {sys.argv[0]} -k (0 – supremum distance | 1 – manhattan distance | 2 – Euclidean distance ) -d <number-of-neighboring> <file-name>.txt"

def distance_function(op: int):
    print("distance functions")

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