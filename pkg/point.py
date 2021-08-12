class Point:
    def __init__(self, id: str, coordinate: list[float]):
        self.id = id
        self.cluster_id = None
        self.coordinate = coordinate
        self.neighbors = list[Point]
        
    def add_to_cluster(self, cluster_id: str):
        self.cluster_id = cluster_id

    def format_to_file(self) -> str :
        return "{} {} {}\n".format(self.id, "".join(str(self.coordinate)), self.cluster_id).replace(',', '').replace('[', '').replace(']', '')

    def __str__(self) -> str:
        return 'id={id}, coordinate={coordinate}'.format(id=self.id, coordinate=self.coordinate)

    def get_neighboors(self) -> str:
        return ' '.join([f'id={item.id}' for item in self.neighbors])


