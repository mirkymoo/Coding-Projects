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

def getChoiceSelection():
    selection = int(input("Enter choice: "))
    return(selection)

def getRoomCharge():
    days = int(input("Enter how many days did the patient stay at the hospital:"))
    return(days * 1662)

def getPatientType():
    print("\nMain Menu")
    print("\nIs this an in-patient or out-patient?")
    print("1. In-Patient")
    print("2. Out-Patient")
    print("3. Quit")
    patientType = int(input("Enter choice: "))
    return(patientType)

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
    while True:
        try:
            selection = getChoiceSelection()
            if (selection > 0 and selection < 9):
                getServiceCharge(selection)
            elif selection == 9:
                getPatientType()
            else:
                print("Invalid choice. Enter 1-6")
                inPatientServicesMenu()
        except ValueError:
            print("Invalid choice. Enter 1-6")

def getServiceCharge(selection):
    patientType = getPatientType()
    if patientType == 1:
        prices = {1: 2924, 2: 4200, 3: 3200, 4: 6200, 5: 5200, 6: 4341, 7: 2336, 8: 3828}
        serviceCharge = prices[selection]
    elif patientType == 2:
        prices = {1: 96, 2: 106, 3: 900, 4: 450, 5: 506}
        serviceCharge = prices[selection]
    else:
        print("Error in getServiceCharge")
    return(serviceCharge)

def outPatientServicesMenu():
    print("\nOut-Patient Services Menu:")
    print("1. PAP SMEAR BETHESDA - $96")
    print("2. PAP SMEAR SCREEN BY CYTOTEC MC - $106")
    print("3. US OB COMPLETE EXAM - $900")
    print("4. US OB COMPL EX ADDTL GESTATN- $450")
    print("5. US OB LIMITED 1+FETUSES - $506")
    print("6. Return to main menu.")
    while True:
        try:
            selection = getChoiceSelection()
            if (selection > 0 and selection < 6):
                getServiceCharge(selection)
            elif selection == 6:
                getPatientType()
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
    while True:
        try:
            selection = getChoiceSelection()
            if (selection > 0 and selection < 6):
                getMedicationCharge(selection)
            elif selection == 6:
                getPatientType()
            else:
                print("Invalid choice. Enter 1-6")
                medicationMenu()
        except ValueError:
            print("Invalid choice. Enter 1-6")

def getMedicationCharge(selection):
    prices = {1: 669, 2: 472, 3: 900, 4: 450, 5: 506}
    medicationCharge = prices[selection]
    return(medicationCharge)

def main():
    patientType = getPatientType()
    while True:
        try:
            if patientType == 1:
                roomCharge = getRoomCharge()
                inPatientServicesMenu()
                break
            elif patientType == 2:
                outPatientServicesMenu()
                break
            elif patientType == 3:
                break
            else:
                print("Invalid choice. Enter 1-3")
                getPatientType()
        except ValueError:
            print("Invalid choice. Enter 1-3")
    
    medicationCharge = getMedicationCharge()
    serviceCharge = getServiceCharge()

    totalCharge = roomCharge + serviceCharge + medicationCharge
    print(f"Room charges \t\t${roomCharge:0.2f}")
    print(f"Lab & Services \t\t${serviceCharge:0.2f}")
    print(f"Medication \t\t${medicationCharge:0.2f}")
    print(f"Total charges \t\t${totalCharge:0.2f}")

main()

