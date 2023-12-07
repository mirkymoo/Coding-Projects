class HospitalMenu:
    def __init__(self):
        self.inpatient_price = 0
        self.outpatient_price = 0
        self.daily_rate = 1662
        self.inpatient_items = {
            1: ("VAGINAL DELIVERY SIMPLE", 2924),
            2: ("VAGINAL DELIVERY COMPLEX", 4200),
            3: ("VAGINAL DELIVERY INTERMEDIATE", 3200),
            4: ("C SECTION COMPLEX", 6200),
            5: ("C SECTION INTERMEDIATE", 5200),
            6: ("C SECTION SIMPLE", 4341),
            7: ("POST PARTUM TUBAL", 2336),
            8: ("FETAL VERSION", 3828)
        }
        self.outpatient_items = {
            1: ("OB AMNIOCENTESIS DIAGNOSTIC", 2356),
            2: ("OB CONTRACTION STRESS TEST", 666),
            3: ("OB FETAL NST", 596),
            4: ("PAP SMEAR BETHESDA", 96),
            5: ("US OB COMPLETE EXAM", 900),
            6: ("US OB COMPL EX ADDTL GESTATN", 450),
        }
        self.medication_prices = {
            1: ("OB EPIDURAL 1ST HOUR", 669),
            2: ("OB EPIDURAL EA ADDL HOUR", 472),
            3: ("OB OR ANESTHESIA 1ST 30 MIN", 551),
            4: ("OB OR ANESTHESIA EA ADDL 15 MIN", 94)
        }

    def display_main_menu(self):
        print("1. Inpatient")
        print("2. Outpatient")
        print("3. Exit")

    def handle_main_menu(self):
        while True:
            self.display_main_menu()
            choice = input("Select an option (1-3): ")
            if choice == '1':
                self.inpatient_menu()
            elif choice == '2':
                self.outpatient_menu()
            elif choice == '3':
                self.print_total_charges()
                print("Exiting program. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

    def inpatient_menu(self):
        print("Inpatient Items:")
        for key, (item, price) in self.inpatient_items.items():
            print(f"{key}. {item} - ${price}")
        inpatient_choice = int(input("Select an inpatient item (1-8): "))
        inpatient_total_price = self.inpatient_items[inpatient_choice][1]
        self.inpatient_price += inpatient_total_price
        print(f"\nInpatient Charges: {self.inpatient_items[inpatient_choice][0]} - ${inpatient_total_price}\n")
        self.medication_menu()

    def outpatient_menu(self):
        print("Outpatient Items:")
        for key, (item, price) in self.outpatient_items.items():
            print(f"{key}. {item} - ${price}")
        outpatient_choice = int(input("Select an outpatient item (1-6): "))
        outpatient_total_price = self.outpatient_items[outpatient_choice][1]
        self.outpatient_price += outpatient_total_price
        print(f"\nOutpatient Charges: {self.outpatient_items[outpatient_choice][0]} - ${outpatient_total_price}\n")
        self.medication_menu()

    def medication_menu(self):
        medication_total_price = 0
        while True:
            print("Medication Menu:")
            for key, (medication, price) in self.medication_prices.items():
                print(f"{key}. {medication} - ${price}")
            print("5. Exit Medication")
            choice = int(input("Select a medication (1-5): "))
            if choice == 5:
                break
            elif choice in self.medication_prices:
                medication_total_price += self.medication_prices[choice][1]
            else:
                print("Invalid choice. Please try again.")
        print(f"\nMedication Charges: ${medication_total_price}\n")
        self.inpatient_price += medication_total_price

    def print_total_charges(self):
        total_charges = self.inpatient_price + self.outpatient_price
        print("\nTotal Charges:")
        print(f"Inpatient Charges: ${self.inpatient_price}")
        print(f"Outpatient Charges: ${self.outpatient_price}")
        print(f"Medication Charges: ${total_charges - self.inpatient_price - self.outpatient_price}")
        print(f"Total Charges: ${total_charges}")

if __name__ == "__main__":
    hospital_menu = HospitalMenu()
    hospital_menu.handle_main_menu()