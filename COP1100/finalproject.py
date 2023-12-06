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
    return selection

def getRoomCharge():
    days = int(input("Enter how many days did the patient stay at the hospital: "))
    return days * 1662

def getPatientType():
    print("\nMain Menu")
    print("\nIs this an in-patient or out-patient?")
    print("1. In-Patient")
    print("2. Out-Patient")
    print("3. Quit")
    patientType = int(input("Enter choice: "))
    return patientType

def getServiceCharge(selection, patientType):
    if patientType == 1:
        prices = {1: 2924, 2: 4200, 3: 3200, 4: 6200, 5: 5200, 6: 4341, 7: 2336, 8: 3828}
    elif patientType == 2:
        prices = {1: 96, 2: 106, 3: 900, 4: 450, 5: 506}
    else:
        print("Error in Service Charge")
        return 0
    return prices.get(selection, 0)

def inPatientServicesMenu(patientType):
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
            if 1 <= selection <= 8:
                return getServiceCharge(selection, patientType)
            elif selection == 9:
                break
            else:
                print("Invalid choice. Enter 1-9")
        except ValueError:
            print("Invalid choice. Enter 1-9")

def outPatientServicesMenu(patientType):
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
            if 1 <= selection <= 5:
                return getServiceCharge(selection, patientType)
            elif selection == 6:
                break
            else:
                print("Invalid choice. Enter 1-6")
        except ValueError:
            print("Invalid choice. Enter 1-6")

def medicationMenu():
    print("\nMedication Menu:")
    print("1. OB EPIDURAL 1ST HOUR - $669")
    print("2. OB EPIDURAL EA ADDL HOUR - $472")
    print("3. OB OR ANESTHESIA 1ST 30 MIN - $900")
    print("4. OB OR ANESTHESIA EA ADDL 15 MIN - $450")
    print("5. OB OR ANESTHESIA - $551")
    print("6. Return to main menu.")
    while True:
        try:
            selection = getChoiceSelection()
            if 1 <= selection <= 5:
                return getMedicationCharge(selection)
            elif selection == 6:
                break
            else:
                print("Invalid choice. Enter 1-6")
        except ValueError:
            print("Invalid choice. Enter 1-6")

def getMedicationCharge(selection):
    prices = {1: 669, 2: 472, 3: 900, 4: 450, 5: 506, 6: 0}
    return prices.get(selection, 0)

def main():
    while True:
        patientType = getPatientType()
        roomCharge = 0
        serviceCharge = 0
        medicationCharge = 0

        try:
            if patientType == 1:
                roomCharge = getRoomCharge()
                serviceCharge = inPatientServicesMenu(patientType)
            elif patientType == 2:
                serviceCharge = outPatientServicesMenu(patientType)
            elif patientType == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Enter 1-3")
                continue

            if patientType == 1 or patientType == 2:
                medicationCharge = medicationMenu()

            totalCharge = roomCharge + serviceCharge + medicationCharge
            print(f"Room charges \t\t${roomCharge:0.2f}")
            print(f"Lab & Services \t\t${serviceCharge:0.2f}")
            print(f"Medication \t\t${medicationCharge:0.2f}")
            print(f"Total charges \t\t${totalCharge:0.2f}")

        except ValueError:
            print("Invalid choice. Enter a numeric value.")
        break

main()