sum = 0
print("Enter the numbers you would like to add together. To exit the program and see your total, enter -1, Please enter the first number: ")
num = int(input())
while num >= 0:
    sum = sum + num
    print("Enter the next number: ")
    num = int(input())
print("The total of all your numbers is:" + str(sum))