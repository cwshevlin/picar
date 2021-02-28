

class Grid():
    def __init__(self, width, height):
        self.width: int = width
        self.height: int = height
        self.obstacles: List[Tuple] = []
        self.costs: Dict[Tuple, float] = {} 

    def neighbors_for_point(self, x, y) -> List:
        return [
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
                (x, y - 1)
                ]

    def cost(self, from_node: GridLocation, to_node: GridLocation) -> float:
        return self.weights.get(to_node, 1)

    def point_has_clearance(self, x, y) -> bool:
        has_clearance = True
        for i in range(3)):
            has_clearance = (x + i, y) not in self.obstancles and (x, y + i) not in self.obstancles
            if not has_clearance return False
        return has_clearance

    def point_is_in_bound(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height


    
