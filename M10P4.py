def get_lastName():
    lastName = input("What is your last name? ")
    return lastName

def get_milesfromChicago():
    milesfromChicago = int(input("How many miles did you go from downtown Chicago? "))
    return milesfromChicago

def calculateTrainTicketPrice(milesfromChicago):
    if milesfromChicago >= 30:
        return 12.00
    elif 20 <= milesfromChicago <= 29:
        return 10.00
    elif 10 <= milesfromChicago <= 19:
        return 8.00
    else:
        return 5.00

def calculateTotalTicketPrice(currentTotal, TrainTicketPrice):
    TotalTicketPrice = currentTotal + TrainTicketPrice
    return TotalTicketPrice

def displayResult(lastName, milesfromChicago, TrainTicketPrice, TotalTicketPrice):
    print(f"Last Name: {lastName}")
    print(f"Miles from Downtown Chicago: {milesfromChicago}")
    print(f"Train Ticket Price: ${TrainTicketPrice:.2f}")
    print(f"Total Ticket Price: ${TotalTicketPrice:.2f}")

TotalTicketPrice = 0

runProgram = input("Would you like to know the price of each train ticket? (Y/N) ")

while runProgram.lower() in ("y", "yes"):

    lastName = get_lastName()
    milesfromChicago = get_milesfromChicago()

    TrainTicketPrice = calculateTrainTicketPrice(
        milesfromChicago
    )

    TotalTicketPrice = calculateTotalTicketPrice(
        TotalTicketPrice,
        TrainTicketPrice
    )

    displayResult(
        lastName,
        milesfromChicago,
        TrainTicketPrice,
        TotalTicketPrice
    )

    runProgram = input(
        "\nWould you like to enter another ticket? (Y/N) "
    )

print()
print(f"The sum of the total tickets is ${TotalTicketPrice:.2f}")