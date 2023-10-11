mph = int(input("How many mph is the vehicle travaling? "))
hoursTraveled = int(input("How many hours has it traveled? "))

print("Hour\t\tDistance Traveled")
print("---------------------------------")

for hoursTraveled in range(1, hoursTraveled + 1):
    distance = mph * hoursTraveled
    print(hoursTraveled,"\t\t",distance)