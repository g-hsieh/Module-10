def get_lastName():
    lastName = input("What is your last name? ")
    return lastName

def get_month():
    month = input("What is the month? ")
    return month

def get_sales():
    sales = float(input("What is the sales amount? "))
    return sales

def calculateNextMonthSales(sales, forecastPercent):
    nextMonthSales = sales * (1 + forecastPercent)
    return nextMonthSales

def display_result(lastName, month, sales, nextMonthSales):
    print("\nMonth and Sales Information")
    print(f"Last Name: {lastName}")
    print(f"Month: {month}")
    print(f"Sales: ${sales:,.2f}")
    print(f"Next Month Sales: ${nextMonthSales:,.2f}")

monthCount = 0
totalNextMonthSales = 0

runProgram = input(
    "Would you like to know the month & sales to find the month's forecast? (Y/N): "
)

while runProgram.lower() in ("y", "yes"):

    lastName = get_lastName()
    month = get_month()
    sales = get_sales()

    monthUpper = month.upper()

    if monthUpper in ("JAN", "FEB", "MAR"):
        forecastPercent = 0.10
    elif monthUpper in ("APR", "MAY", "JUN"):
        forecastPercent = 0.15
    elif monthUpper in ("JUL", "AUG", "SEP", "SEPT"):
        forecastPercent = 0.20
    elif monthUpper in ("OCT", "NOV", "DEC"):
        forecastPercent = 0.25
    else:
        print("Invalid Month")
        runProgram = input(
            "\nWould you like to enter another month & sales? (Y/N): "
        )
        continue

    nextMonthSales = calculateNextMonthSales(sales, forecastPercent)

    monthCount += 1
    totalNextMonthSales += nextMonthSales

    display_result(lastName, month, sales, nextMonthSales)

    runProgram = input(
        "\nWould you like to enter another month & sales? (Y/N): "
    )

print("\nProgram Ended")
print(f"Months Entered: {monthCount}")
print(f"Total Forecasted Sales: ${totalNextMonthSales:,.2f}")