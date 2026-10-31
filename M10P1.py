def get_lastName():
    lastName = input("What is your last name? ")
    return lastName

def get_month():
    month = input("What is the current month? ")
    return month

def get_sales():
    sales = float(input("What is the sales amount? $"))
    return sales

def get_next_month(month):
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    month = month.upper()

    if month in months:
        index = months.index(month)
        nextMonth = months[(index + 1) % 12]
        return nextMonth
    else:
        return "INVALID"

def get_forecast_percent(nextMonth):
    if nextMonth in ("JAN", "FEB", "MAR"):
        forecastPercent = 0.10
    elif nextMonth in ("APR", "MAY", "JUN"):
        forecastPercent = 0.15
    elif nextMonth in ("JUL", "AUG", "SEP"):
        forecastPercent = 0.20
    elif nextMonth in ("OCT", "NOV", "DEC"):
        forecastPercent = 0.25
    return forecastPercent

def calculateNextMonthSales(sales, forecastPercent):
    nextMonthSales = sales * (1 + forecastPercent)
    return nextMonthSales

def display_result(lastName, month, nextMonth, sales, nextMonthSales):
    print("\nMonth and Sales Information")
    print(f"Last Name: {lastName}")
    print(f"Current Month: {month}")
    print(f"Next Month: {nextMonth}")
    print(f"Sales: ${sales:,.2f}")
    print(f"Forecasted Sales: ${nextMonthSales:,.2f}")

monthCount = 0
totalNextMonthSales = 0

runProgram = input("Would you like to know next month's forecast based on this month's sales? (Y/N): ")

while runProgram.lower() in ("y", "yes"):

    lastName = get_lastName()
    month = get_month()
    sales = get_sales()

    nextMonth = get_next_month(month)

    if nextMonth == "INVALID":
        print("Invalid Month")
        runProgram = input("\nWould you like to enter another month & sales? (Y/N): ")
        continue

    forecastPercent = get_forecast_percent(nextMonth)
    nextMonthSales = calculateNextMonthSales(sales, forecastPercent)

    monthCount += 1
    totalNextMonthSales += nextMonthSales

    display_result(lastName, month, nextMonth, sales, nextMonthSales)
    runProgram = input("\nWould you like to enter another month & sales? (Y/N): ")

print("\nProgram Ended")
print(f"Months Entered: {monthCount}")
print(f"Total Forecasted Sales: ${totalNextMonthSales:,.2f}")