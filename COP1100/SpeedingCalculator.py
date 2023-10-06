print("Please enter the speed limit: ")
speedLimit = int(input())
while 20 > speedLimit or speedLimit > 70:
    print("Please try again. The speed limit should be at least 20 but no more that 70. Enter the speed limit: ")
    speedLimit = int(input())
print("Enter the speed you were driving: ")
drivingSpeed = int(input())
while drivingSpeed < speedLimit:
    print("Please try again. Your driving speed should be at least that of the speed limit, or else you were not speeding.")
    drivingSpeed = int(input())
speeding = drivingSpeed - speedLimit
print("You were driving " + str(speeding) + " miles over the speed limit.", end='', flush=True)