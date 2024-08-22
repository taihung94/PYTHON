def RectangleArea(strArr):
    # Extract the coordinates from the input strings
    points = [tuple(map(int, point.strip('()').split())) for point in strArr]
    
    # Extract unique x and y coordinates
    x_coords = {point[0] for point in points}
    y_coords = {point[1] for point in points}
    
    # There should be exactly two unique x and y coordinates for a valid rectangle
    if len(x_coords) != 2 or len(y_coords) != 2:
        return 0  # Invalid rectangle

    # Calculate width and height
    width = abs(max(x_coords) - min(x_coords))
    height = abs(max(y_coords) - min(y_coords))
    
    # Calculate the area of the rectangle
    area = width * height
    
    return area

# Example usage:
# print(RectangleArea(["(0 0)", "(3 0)", "(0 2)", "(3 2)"]))  # Output: 6
# print(RectangleArea(["(1 1)", "(1 4)", "(5 1)", "(5 4)"]))  # Output: 12
strArr=["(0 0)", "(3 0)", "(0 2)", "(3 2)"]
points = [tuple(map(int, point.strip('()').split())) for point in strArr]
print(points)
