def get_Length():
    length = float(input("What is the length in feet? "))
    return length

def get_Width():
    width = float(input("What is the width in feet? "))
    return width

def get_Height():
    height = float(input("What is the height in feet? "))
    return height

def calculateWallSquareFootage(length, width, height):
    wallSquareFootage = (2 * length * height) + (2 * width * height)
    return wallSquareFootage

def calculatewGallons(wallSquareFootage):
    wGallons = wallSquareFootage / 50
    return wGallons

def calculatefcGallons(length, width):
    fcGallons = (length * width) / 50
    return fcGallons

def displayResult(wGallons, fcGallons):
    print()
    print(f"You will need {wGallons:.2f} gallons of wall paint.")
    print()
    print(f"You will need {fcGallons:.2f} gallons of ceiling paint or floor varnish.")

runProgram = input(
    "Would you like to know how many gallons of paint are needed to paint your room? (Y/N) "
)

while runProgram.lower() in ("y", "yes"):

    length = get_Length()
    width = get_Width()
    height = get_Height()

    wallSquareFootage = calculateWallSquareFootage(length, width, height)
    fcGallons = calculatefcGallons(length, width)
    wGallons = calculatewGallons(wallSquareFootage)

    displayResult(wGallons, fcGallons)

    runProgram = input("\nWould you like to enter another wall square footage, number of gallons, and area? (Y/N): ")

print("\nProgram ended.")