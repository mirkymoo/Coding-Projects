#A needy tamagotchi which changes its moods rapidly
import random

check_tamagotchi = input("Would you like to check on your tamagotchi? Please type \"Y\" for yes or \"N\" for no:")

if check_tamagotchi == "Y":
    tamagotchi_mood = random.seed(0,5)
    if tamagotchi_mood == 0 or 1:
         print("Your tamagotchi is happy.")
    elif tamagotchi_mood == 2:
         print("Your tamagotchi is sad.")
    elif tamagotchi_mood == 3:
        print("Your tamagotchi is sleeping.")
    elif tamagotchi_mood == 4 or 5:
        print("You tamagotchi is hungry.")

#for some reason the tamagotchi is always happy....?