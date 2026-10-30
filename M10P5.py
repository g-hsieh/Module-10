def get_County():
    County = input("What's your county name? ")
    return County


def get_MarketValue():
    MarketValue = float(input("What is the market value? $"))
    return MarketValue

def calculateAssessedValue(MarketValue, AssessedPercent):
    AssessedValue = MarketValue * AssessedPercent
    return AssessedValue

countyCount = 0
totalMarketValue = 0
totalAssessedValue = 0

runProgram = input("Would you like to know your county and the market value of your house? (Y/N): ")

while runProgram.lower() in ("y", "yes"):

    County = get_County()
    MarketValue = get_MarketValue()

    County = County.upper()

    if County == "COOK":
        AssessedPercent = 0.90
    elif County == "DUPAGE":
        AssessedPercent = 0.80
    elif County == "MCHENRY":
        AssessedPercent = 0.75
    elif County == "KANE":
        AssessedPercent = 0.60
    else:
        AssessedPercent = 0.70

    AssessedValue = calculateAssessedValue(MarketValue, AssessedPercent)

    print(f"\nCounty: {County}")
    print(f"Market Value: ${MarketValue:,.2f}")
    print(f"Assessed Value: ${AssessedValue:,.2f}")

    countyCount += 1
    totalMarketValue += MarketValue
    totalAssessedValue += AssessedValue

    runProgram = input("\nWould you like to enter another county and market value? (Y/N): ")

print("\nProgram Ended")
print(f"You entered {countyCount} counties.")
print(f"The total market value is ${totalMarketValue:,.2f}")
print(f"The total assessed value is ${totalAssessedValue:,.2f}")