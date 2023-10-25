#Assigment promt: Search the web to discover the 
#ten most common user-selected passwords and store them in an array. 
#Design a program that prompts a user for a password and continue to prompt the user 
#until the user has not chosen one of the common passwords.


common_passwords = ["123456", "password", "qwerty", "111111", "abc123", "password1", "iloveyou", "1q2w3e4r", "000000", "zaq12wsx"]
user_password = input("Please enter your new password: ")

while user_password in common_passwords:
    user_password = input("This password is too common! Please use a different one. Enter your new password: ")


print("Your new password was sucessfully set!")