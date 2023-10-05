print("Enter the weight of your package in lbs:")
packageWeight = float(input())
if packageWeight <= 2:
    freight = packageWeight * 1.1
elif 2 < packageWeight <= 6:
    freight = packageWeight * 2.2
elif 6 < packageWeight <= 10:
    freight = packageWeight * 3.7
elif packageWeight > 10:
    freight = packageWeight * 3.8
else
    print("Error.")
print("The shipping charge for the package is $", freight)