print("Please enter three numbers to find out which is the smallest and largest value:")
num1 = int(input())
num2 = int(input())
num3 = int(input())

print("The smallest number is:", min(num1, num2, num3))
print("The largest number is:", max(num1, num2, num3))


# using only if/esle statments
"""
if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")
"""