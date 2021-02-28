import collections
import heapq
from .grid.py import Grid

class PriotityQueue():
    def __init__(self):
        self.elements: List[Tuple[float, Tuple[int, int] = [] 
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: Tuple (x, y), priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heapop(self.elements)[1]


class AStar():

    @static
    def best_guess():
        pass


    @static
    def navigate(grid: Grid, start, goal):
        candidate_points = PriorityQueue()
        candidate_points.put(start, 0)
        came_from: Dict[Location, Optional[Location]] = {}
        cost_so_far: Dict[Location, float] = {}
        came_from[start] = None
        cost_so_far[start] = 0
        while not candidate_points.empty():
            current_location = frontier.get()

            if current_location == goal:
                break

            for next in graph.neighbors(current):
                new_cost = cost_so_far[current_location] + graph.cost(current_location, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + AStar.best_guess(next, goal)
                candidate_points.put(next, priority)
                came_from[next] = current

            return came_from, cost_so_far
    
