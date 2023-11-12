

def getSales():
    monthlySales = float(input("Enter the salesperson's monthly sales."))
    return(monthlySales)

def getAdvancedPay():
    advancedPay = float(input("Enter the amount of advanced pay, or\nenter 0 if no advance pay was given."))
    return(advancedPay)

def determineCommisionRate(monthlySales):
    if monthlySales < 10000.00:
        commissionRate = 0.10
    elif 10000.00 <= monthlySales <= 14999.99:
        commissionRate = 0.12
    elif 15000.00 <= monthlySales <= 17999.99:
        commissionRate = 0.14
    elif 18000.00 <= monthlySales <= 21999.99:
        commissionRate = 0.16
    else:
        commissionRate = 0.18
    return(commissionRate)

def main():
    monthlySales = getSales()
    advancedPay = getAdvancedPay()
    commissionRate = determineCommisionRate(monthlySales)
    pay = monthlySales * commissionRate - advancedPay

    print(f"The pay is ${pay:0.2f}")
    if pay < 0:
        print("The sales person must reimburse\nthe company")

main()
