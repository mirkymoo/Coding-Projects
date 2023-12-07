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
    selection = validate_input("Enter choice: ")
    return selection

def getRoomCharge():
    days = validate_input("\nEnter how many days did the patient stay at the hospital: ")
    return days * 1662

def getPatientType():
    print("\nMain Menu")
    print("\nIs this an in-patient or out-patient?")
    print("1. In-Patient")
    print("2. Out-Patient")
    print("3. Quit")
    patientType = validate_input("Enter choice: ")
    return patientType

def getServiceCharge(selection, patientType):
    if patientType == 1:
        prices = {1: 2924, 2: 4200, 3: 3200, 4: 6200, 5: 5200, 6: 4341, 7: 2336, 8: 3828}
    elif patientType == 2:
        prices = {1: 96, 2: 106, 3: 900, 4: 90, 5: 256}
    else:
        print("Error in getServiceCharge")
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
    print("9. Go to medication menu.")
    while True:
        selection = getChoiceSelection()
        if 1 <= selection <= 8:
            return getServiceCharge(selection, patientType)
        elif selection == 9:
            break

def outPatientServicesMenu(patientType):
    print("\nOut-Patient Services Menu:")
    print("1. PAP SMEAR BETHESDA - $96")
    print("2. PAP SMEAR SCREEN BY CYTOTEC MC - $106")
    print("3. US OB COMPLETE EXAM - $900")
    print("4. URINE PREGNANCY TEST - $90")
    print("5. CULTURE URINE - $256")
    print("6. Go to medication menu.")
    
    outPatientADDL = 0
    
    while True:

        selection = getChoiceSelection()

        if 1 <= selection <= 5:
            outPatientADDL += getServiceCharge(selection, patientType)
            print(f"\nOption {selection} selected. Please select another option or press 6 to medication menu.")
        elif selection == 6:
            break
        else:
            print("Invalid choice. Enter 1-6")    

def inPatientMedicationMenu(patientType):
    print("\nMedication Menu:")
    print("1. OB EPIDURAL 1ST HOUR - $669")
    print("2. OB EPIDURAL EA ADDL HOUR - $472")
    print("3. OB OR ANESTHESIA 1ST 30 MIN - $900")
    print("4. OB OR ANESTHESIA EA ADDL 15 MIN - $450")
    print("5. OB OR ANESTHESIA - $551")
    print("6. Exit current menu.")

    medication_charge = 0

    while True:
        selection = getChoiceSelection()
        if 1 <= selection <= 5:
            medication_charge += getMedicationCharge(selection, patientType)
            print(f"\nOption {selection} selected. Please select another option or press 6 to finish.")
        elif selection == 6:
            break 

    return medication_charge

def outPatientMedicationMenu():
    print("\nMedication Menu:")
    print("1. Prenatal Multivitamins With Folic Acid, 30 tablets - $74.4")
    print("2. Clindamycin 2% Vag Crm - $28.08")
    print("3. Clotrimazole 1% Vag Crm W/Appl - $68.96")
    print("4. Sulfamethoxazole-Trimethoprim 200 Mg-40 Mg/5 Ml Oral Susp - $19.63")
    print("5. Levonorgestrel 1.5 Mg Tab - $316.03")
    print("6. Exit current menu.")

    medication_charge = 0

    while True:
        selection = getChoiceSelection()
        if 1 <= selection <= 5:
            medication_charge += getMedicationCharge(selection)
            print(f"\nOption {selection} selected. Please select another option or press 6 to finish.")
        elif selection == 6:
            break     
    return medication_charge

def getMedicationCharge(selection, patientType):
    if patientType == 1:
        prices = {1: 669, 2: 472, 3: 900, 4: 450, 5: 506}
    elif patientType == 2:
        prices = {1: 74.4, 2: 28.08, 3: 68.96, 4: 19.63, 5: 316.03}
    else:
        print("Error in getMedicationCharge")
        return 0
    return prices.get(selection, 0)

def main():
    while True:
        patientType = getPatientType()
        roomCharge = 0
        serviceCharge = 0
        medicationCharge = 0
        totalCharge = 0

        try:
            if patientType == 1:
                roomCharge = getRoomCharge()
                serviceCharge = inPatientServicesMenu(patientType)
                medicationCharge = inPatientMedicationMenu(patientType)
            elif patientType == 2:
                serviceCharge = outPatientServicesMenu(patientType)
                medicationCharge = outPatientMedicationMenu(patientType)
            elif patientType == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Enter 1-3")
                continue

            if roomCharge is not None and serviceCharge is not None:
                totalCharge = roomCharge + serviceCharge + medicationCharge
                print(" ********************************")
                print("\n      Hospital Bill Summary\n") 
                print(" ********************************\n")
                print(f" Room charges \t\t${roomCharge:0.2f}")
                print(f" Lab & Services\t\t${serviceCharge:0.2f}")
                print(f" Medication \t\t${medicationCharge:0.2f}")
                print(f" Total charges \t\t${totalCharge:0.2f}")
                print("\n ********************************")
            else:
                print("Invalid charges. Please try again.")

            break

        except ValueError:
            print("Invalid choice. Enter a numeric value.")


main()