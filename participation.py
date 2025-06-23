#!/usr/bin/env python3

# Setting the correct password which is Secure123
Allowed_password = "Secure123" 

attempt = 0
#After this attemps, tell the user to retry
max_attempts = 3 

while True:
    password = input("Please enter your password: ")
    attempt += 1
    
    # using for loop inside while loop to count digits
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
    
    # Checking if password is correct and granting access after
    if password == Allowed_password:
        print("Access granted!")
        break
    else:
        # Checking for digits
        if digit_count == 0:
            print("Error: Need a digit.")
        else:
            
            print("Access denied.")
        
       
        if attempt >= 2:
            print(f"Alert: you have entered {attempt} times wrong password.")
        
        
