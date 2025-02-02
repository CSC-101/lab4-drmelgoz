import data

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


# Part 5


# Part 6


