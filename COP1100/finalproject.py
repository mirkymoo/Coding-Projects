#

#Validate that no negative inputs are entered
def validate_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

services_total = 0

def mainMenu():
    print("\nPlease select an option:")
    print("1. In-Patient")
    print("2. Out-Patient")
    print("3. Quit")
    while True:
        try:
            selection = int(input("Enter choice: "))
            if selection == 1:
                inPatientServicesMenu()
                break
            elif selection == 2:
                outPatientServicesMenu()
                break
            elif selection == 3:
                break
            else:
                print("Invalid choice. Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1-3")
    exit

def inPatientServicesMenu():
    print("\nIn-Patient Services Menu:")
    print("Please select services provided")
    print("1. VAGINAL DELIVERY SIMPLE - $2924")
    print("2. VAGINAL DELIVERY COMPLEX - $4200")
    print("3. VAGINAL DELIVERY INTERMEDIATE - $3200")
    print("4. C SECTION COMPLEX - $6200")
    print("5. C SECTION INTERMEDIATE - $5200")
    print("6. C SECTION SIMPLE - $4341")
    print("7. POST PARTUM TUBAL - $2336")
    print("8. FETAL VERSION - $3828")
    print("9. Return to main menu.")
    prices = [2924, 4200, 3200, 6200, 5200, 4341, 2336, 3828]
    while True:
        try:
            selection = int(input("Enter choice: "))
            if (selection > 0 and selection < 9):
                services_total += selection
            elif selection == 9:
                mainMenu()
            else:
                print("Invalid choice. Enter 1-9")
                inPatientServicesMenu()
        except ValueError:
            print("Invalid choice. Enter 1-9")

def outPatientServicesMenu():
    print("\nOut-Patient Services Menu:")
    print("1. PAP SMEAR BETHESDA - $96")
    print("2. PAP SMEAR SCREEN BY CYTOTEC MC - $106")
    print("3. US OB COMPLETE EXAM - $900")
    print("4. US OB COMPL EX ADDTL GESTATN- $450")
    print("5. US OB LIMITED 1+FETUSES - $506")
    print("6. Return to main menu.")
    prices = [96, 106, 900, 450, 506]
    while True:
        try:
            selection = int(input("Enter choice: "))
            if (selection > 0 and selection < 6):
                services_total += prices[selection - 1]
            elif selection == 6:
                mainMenu()
            else:
                print("Invalid choice. Enter 1-6")
                outPatientServicesMenu()
        except ValueError:
            print("Invalid choice. Enter 1-6")

def medicationMenu():
    print("\nOut-Patient Services Menu:")
    print("1. OB EPIDURAL 1ST HOUR - $669")
    print("2. OB EPIDURAL EA ADDL HOUR - $472")
    print("3. OB OR ANESTHESIA 1ST 30 MIN - $900")
    print("4. OB OR ANESTHESIA EA ADDL 15 MIN - $450")
    print("5. US OB LIMITED 1+FETUSES - $506")
    print("6. Return to main menu.")
    prices = [669, 472, 900, 450, 506]
    while True:
        try:
            selection = int(input("Enter choice: "))
            if (selection > 0 and selection < 6):
                services_total += prices[selection - 1]
            elif selection == 6:
                mainMenu()
            else:
                print("Invalid choice. Enter 1-6")
                medicationMenu()
        except ValueError:
            print("Invalid choice. Enter 1-6")

mainMenu()