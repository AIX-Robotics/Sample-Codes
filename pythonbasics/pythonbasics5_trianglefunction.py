# Define a function to compute the area of a triangle
def triangleArea(base: int, height: int) -> float:
    area = 0.5 * base * height
    return area


# Compute and print out the area of two different triangles
area1 = triangleArea(10, 2)
# find area of triangle with base 10 & height 2
area2 = triangleArea(3, 7)  # find area of triangle with base 3 & height 7

# Display the results of the computations
print("The area of a triangle of base 10 and height 2 is", area1)
print("The area of a triangle of base 3 and height 7 is", area2)
