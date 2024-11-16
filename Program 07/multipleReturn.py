def calculate(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
rect_area, rect_perimeter = calculate(a, b)
print("Area of the rectangle: ", rect_area)
print("Perimeter of the rectangle: ", rect_perimeter)