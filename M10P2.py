def get_Length():
    length = float(input("What is the length? "))
    return length

def get_Width():
    width = float(input("What is the width? "))
    return width

def get_Height():
    height = float(input("What is the height? "))
    return height

def calculateWallSquareFootage(length, width, height):
    wallSquareFootage = (2 * length * height) + (2 * width * height)
    return wallSquareFootage

def calculateGallons(wallSquareFootage):
    gallons = wallSquareFootage / 50
    return gallons

def calculateArea(length, width):
    area = length * width
    return area

def displayResult(wallSquareFootage, gallons, area):
    print(
        f"The area of the ceiling or floor is {area:.2f} square units "
        f"with {gallons:.2f} gallons of ceiling paint or floor varnish."
    )
    print(f"The wall square footage is {wallSquareFootage:.2f} square feet.")

runProgram = input(
    "Would you like to know the wall square footage, the area, & number of gallons needed? (Y/N) "
)

while runProgram.lower() in ("y", "yes"):

    length = get_Length()
    width = get_Width()
    height = get_Height()

    wallSquareFootage = calculateWallSquareFootage(length, width, height)
    area = calculateArea(length, width)
    gallons = calculateGallons(wallSquareFootage)

    displayResult(wallSquareFootage, gallons, area)

    runProgram = input(
        "\nWould you like to enter another wall square footage, number of gallons, and area? (Y/N): "
    )

print("\nProgram ended.")
print(f"\nYou used {gallons:,.2f} gallons of ceiling paint for the ceiling and {gallons:,.2f} gallons of floor varnish for the floor.")