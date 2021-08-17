from types import coroutine
from pkg.clusterization import DbScan
from pkg.point import Point
import sys
import re

MESSAGE = f"""

Usage: {sys.argv[0]} -k <k_value> [ -e <eps_value> ] [ -d <distance_option_value> ] <file_name>.txt

-k : MinPts, Minimum number of points in an Eps-neighbourhood to be a core point(Required*)
-e : Eps, Maximum radius of the neighborhood(default = 1)
-d : Distance Metric: 0 – Supremum distance | 1 – Manhattan distance | 2 – Euclidean distance(default)


"""

def distance_metric_options(opt: int):
    if opt == 0:
        return 'Supremun'
    elif opt == 1:
        return 'Manhattan'
    elif opt == 2:
        return 'Euclidean'
    

def main():

    # valores padrão

    eps = 1 # (-e)
    distance_metric = 2 # (-d)
    minPts = 0 # valor inválido, precisa ser informado(-k)

    arguments = sys.argv[1:]

    # valida parametros

    if not arguments:
        raise SystemExit(MESSAGE)

    if not '-k' in arguments:
        raise SystemExit("""\nMessage:'-k' param is required! {} """.format(MESSAGE))
    else:
        index = arguments.index('-k') + 1
        if(arguments[index].isnumeric()):
            minPts = int(arguments[index])
        if not minPts > 0:                
            raise SystemExit("""\nMessage: Invalid '-k' value! Needs to be an integer number' {} """.format(MESSAGE))

    if '-e' in arguments: 
        index = arguments.index('-e') + 1
        try:
            eps = float(arguments[index])
        except ValueError:
            raise SystemExit("""\nMessage: values of params need to be a number! {} """.format(MESSAGE))    
       
    if '-d' in arguments: 
        index = arguments.index('-d') + 1
        try:
            distance_metric = int(arguments[index])
        except ValueError:
            raise SystemExit("""\nMessage: values of params need to be a number!! {} """.format(MESSAGE))    

    # valida arquivo

    file_path = [x for x in arguments if x.endswith('.txt')]
   
    if len(file_path) != 1:
        raise SystemExit("""\nMessage: Invalid file!' {} """.format(MESSAGE))
    try:
        file = open(file_path[0], 'r')
    except FileNotFoundError:
        raise SystemExit("""\nMessage: File Not found ! {} """.format(MESSAGE))    
    except ValueError:
        raise SystemExit("""\nMessage: Invalid File! {} """.format(MESSAGE))    

    # transforma dados em points e headers

    headers = file.readline().strip('\n').strip(None)       
    headers = headers.split(' ') 
    points = []


    for row in file:        
        row = row.strip()
        columns = row.split()
        id = columns[0]
        try:
            coordinate = [float(c) for c in columns[1:] if len(c) > 0 and not c.isalpha() ] 
            # print(coordinate)
            points.append(Point(id, coordinate))
        except ValueError:
            raise SystemExit('The values of dataset need to be numeric')
    
    file.close()

    print(
    f"""    
File: {file_path[0]}
Eps(range): {eps}
Min Points(core point): {minPts}
Distance Metric Option: {distance_metric_options(distance_metric)}
    """)

    # clusterização

    DbScan(points, eps, distance_metric, minPts)

    # saida

    headers.append('group')
    headers.append('\n')

    print("{}".format(" ".join(headers)))
    new_headers = "{}".format(" ".join(headers))
    
    saida = open('saida.txt', 'w')
    saida.writelines(new_headers)
    
    for point in points:
        print(point.format_to_file())
        saida.writelines(point.format_to_file()) 
    print (f""" 
Input Data: {file.name}
Output Data: {saida.name}
Eps(range): {eps}
Min Points(core point): {minPts}
Distance Metric Option: {distance_metric_options(distance_metric)}

Output file has been generated!!
    
    """)
    saida.close()

main()