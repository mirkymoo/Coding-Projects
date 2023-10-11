mph = int(input("How many mph is the vehicle travaling? "))
hoursTraveled = int(input("How many hours has it traveled? "))

print("Hour\t\tDistance Traveled")
print("---------------------------------")

for hour in range(1, hoursTraveled + 1):
    distance = mph * hour
    print(hour,"\t\t", distance)