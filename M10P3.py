def get_carMake():
    return input("What is the car make? ")

def get_carModel():
    return input("What is the model? ")

def get_evCode():
    return input("What is the electric vehicle code? ")

def get_MSRP():
    return float(input("What is the MSRP price? $"))

def calculateNewMSRP(msrp, percentOff):
    discountAmount = msrp * percentOff
    newMSRP = msrp - discountAmount
    return newMSRP

def calculateOTDPrice(newMSRP):
    salesTax = newMSRP * 0.07
    OTDPrice = newMSRP + salesTax
    return OTDPrice

def calculateTotalSalesPrice(newMSRP, salesTax):
    totalSalesPrice = newMSRP + salesTax
    return totalSalesPrice

def displayResult(carMake, carModel, evCode, msrp, percentOff,
                  discountAmount, newMSRP, OTDPrice, totalPrice):

    print("\nVehicle Information")
    print(f"Car Make: {carMake}")
    print(f"Model: {carModel}")
    print(f"EV Code: {evCode}")
    print(f"Original MSRP:      ${msrp:,.2f}")
    print(f"Discount Percent:    {percentOff:.0%}")
    print(f"Discount Amount:    ${discountAmount:,.2f}")
    print(f"Discounted MSRP:    ${newMSRP:,.2f}")
    print(f"OTD Price:          ${OTDPrice:,.2f}")
    print(f"Total Sales Price:  ${totalPrice:,.2f}")

# Initialize accumulators
totalMSRP = 0
totalSalesPrice = 0

runProgram = input("Would you like to enter a vehicle? (Y/N): ")

while runProgram.lower() in ("y", "yes"):

    carMake = get_carMake()
    carModel = get_carModel()
    evCode = get_evCode()
    msrp = get_MSRP()

    if evCode.lower() == "ev":
        percentOffMSRP = 0.30
    elif carMake.lower() == "honda":
        percentOffMSRP = 0.10
    elif carMake.lower() == "toyota":
        percentOffMSRP = 0.15
    else:
        percentOffMSRP = 0.05

    discountAmount = msrp * percentOffMSRP

    newMSRP = calculateNewMSRP(msrp, percentOffMSRP)

    salesTax = newMSRP * 0.07

    OTDPrice = calculateOTDPrice(newMSRP)

    totalPrice = calculateTotalSalesPrice(newMSRP, salesTax)

    totalMSRP += msrp
    totalSalesPrice += totalPrice

    displayResult(
        carMake,
        carModel,
        evCode,
        msrp,
        percentOffMSRP,
        discountAmount,
        newMSRP,
        OTDPrice,
        totalPrice
    )

    runProgram = input("\nWould you like to add another vehicle? (Y/N): ")

print("\nProgram Ended")
print(f"Total MSRP of all vehicles:     ${totalMSRP:,.2f}")
print(f"Total Sales Price of vehicles:  ${totalSalesPrice:,.2f}")