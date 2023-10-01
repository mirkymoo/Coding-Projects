speed_limit = int(input("Enter the speed limit: \n"))
if speed_limit <= 0:
        print("Invalid input for the speed limit. Please make sure you are entering a positive number greater than 0.")
elif speed_limit > 0:
        driving_speed = int(input("Enter how fast you are driving: \n"))
        if driving_speed < 0:
                print("Invalid input for the driving speed. Please make sure you are entering a positive number.")
        elif driving_speed >= 0:
                if driving_speed == 0:
                        print("You are not driving! Your car is parked.")
                elif driving_speed < speed_limit - 10:
                         print("You are driving too slow! You will get a $50 traffic ticket.")
                elif speed_limit + 6 <= driving_speed <= speed_limit +20:
                         print("You are driving too fast! You will get a $75 speeding ticket.")
                elif speed_limit + 21 <= driving_speed <= speed_limit + 40:
                        print("You are driving too fast! You will get a $150 speeding ticket.")
                elif driving_speed > speed_limit + 40:
                        print("You are driving too fast! You will get a $300 speeding ticket.")
                else:
                        print("You are driving at an appropriate speed. You will not be issued a traffic ticket.")