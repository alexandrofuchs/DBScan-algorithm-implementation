class Point:
    def __init__(self, id: str, coordinate: list[float]):
        self.id = id
        self.coordinate = coordinate
        self.neighbors = list[Point]

    def __str__(self) -> str:
        return 'id={id}, coordinate={coordinate}'.format(id=self.id, coordinate=self.coordinate)

    def get_neighboors(self) -> str:
        return ' '.join([f'id={item.id}' for item in self.neighbors])
