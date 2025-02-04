import data
import math

# Write your functions for each part in the space below.

# Part 1
def first_element(groups:list[list[int]]) -> list[int]:
    result = [group[0] for group in groups if (len(group) > 0)]
    return result



# Part 2
def x_coordinates(points:list[data.Point]) -> list[float]:
    result = [point.x for point in points]
    return result


# Part 3
def are_in_positive_quadrant(points:list[data.Point]) -> list[data.Point]:
    result = [point for point in points if (point.x > 0) and (point.y > 0)]
    return result


# Part 4
def distance(point_a:data.Point, point_b:data.Point) -> float:
    x1 = point_a.x
    x2 = point_b.x
    y1 = point_a.y
    y2 = point_b.y
    dx = x2 - x1
    dy = y2 - y1
    result = math.sqrt((dx ** 2) + (dy ** 2))
    return result

# Part 5
def manhattan_distance(point_a:data.Point, point_b:data.Point) -> float:
    x1 = point_a.x
    x2 = point_b.x
    y1 = point_a.y
    y2 = point_b.y
    dx = x1 - x2
    dy = y1 - y2
    result = abs(dx) + abs(dy)
    return result

# Part 6
def distance_all(points:list[data.Point]) -> list[float]:
    distances = [manhattan_distance(point, data.Point(0,0)) for point in points]
    return distances


