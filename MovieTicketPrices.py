#MovieTicketPrices

time = input("Enter the time of day as either \"day\" or \"night\":\n")
age = int(input("Enter your age:\n"))

if time == 'day':
    if 0 < age < 4:
        print("Your movie ticket is free!")
    elif age >= 4:
        print("Your movie ticket would cost $8")
    else:
        print("That is not a valid age. Try again.")
elif time == 'night':
    if 0 < age < 4:
        print("Your movie ticket is free!")
    elif 4 <= age <= 16:
        print("Your movie ticket would cost $12")
    elif 17 <= age <= 54:
        print("Your movie ticket would cost $15")
    elif age > 54:
        print("Your movie ticket would cost $13")
    else:
        print("That is not a valid age. Try again.")
else:
    print("Error. Invalid input.")