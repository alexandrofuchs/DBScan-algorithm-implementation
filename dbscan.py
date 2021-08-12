from pkg.clusterization import DbScan
from pkg.point import Point
import sys

MESSAGE = f"""

Usage: {sys.argv[0]} -k <value> -e <eps_value> -d <option_value> <file_name>.txt

-k : MinPts, Minimum number of points in an Eps-neighbourhood to be a core point(Required*)
-e : Eps, Maximum radius of the neighborhood(default = 1)
-d : Distance Metric, 0 – Supremum distance | 1 – Manhattan distance | 2 – Euclidean distance(default)


"""

def main():

    # valores padrão

    eps = 1 # (-e)
    distance_metric = 2 # (-d)
    minPts = 0 # valor inválido, precisa ser informado(-k)

    # valida numero de argumentos

    if not len(sys.argv) == 8:
        raise SystemExit(""" \n Invalid number of arguments !' {} """.format(MESSAGE))

    arguments = sys.argv[1:7]

    # valida parametros

    print(arguments)

    if not arguments:
        raise SystemExit(MESSAGE)
    
    if not arguments[0] == '-k' or not arguments[1].isnumeric():
        raise SystemExit(""" \n "Invalid '-k' value" !' {} """.format(MESSAGE))
    else:
        minPts = int(arguments[1])

    if arguments[2] == '-e': 
        try:
            eps = float(arguments[3])
        except ValueError:
            raise SystemExit(""" \n 'the values of params need to be a number!!' {} """.format(MESSAGE))    
    else:
        raise SystemExit(MESSAGE)
       
    if arguments[4] == '-d':
        try:
            distance_metric = float(arguments[5])
        except ValueError:
            raise SystemExit(""" \n 'the values of params need to be a number!!' {} """.format(MESSAGE))    

    # valida arquivo

    file_path = sys.argv[7]

    if not file_path:
        raise SystemExit(""" \n Invalid File !' {} """.format(MESSAGE))
    
    try:
        file = open(file_path, 'r')
    except ValueError:
        raise SystemExit(""" \n Invalid File {} """.format(MESSAGE))    

    # transforma dados em points e headers

    headers = file.readline().rstrip('\n')       
    headers = headers.split(' ')
 
    points = []

    for row in file:        
        row = row.strip()
        columns = row.split(' ')
        id = columns[0]
        coordinate = [float(c) for c in columns[1:] if c]     
        points.append(Point(id, coordinate))
    
    file.close()

    # clusterização

    print(f"eps: {eps}")
    print(f"minPoints: {minPts}")
    print(f"distance metric Option: {distance_metric}")

    DbScan(points, eps, distance_metric, minPts)

    # saida

    headers.append('group')
    print("headers: {}".format(headers))

    new_headers = "{}\n".format(" ".join(headers))
    
    arquivo = open('saida.txt', 'w')
    arquivo.writelines(new_headers)
    
    for point in points:
        print(point.format_to_file())
        arquivo.writelines(point.format_to_file()) 
    print (f""" Arquivo "{arquivo.name}" gerado com sucesso! """)
    arquivo.close()
        

main()