# In this project I will be making a calulator entirely in python
#This is to figure out which funtion the user wants to use
a=input("""
Which function do you wish to use, type the number in the brackets:
1. Addition (1)
2. Substraction (2)
3. Division (3)
4. Multiplication (4)
Enter the number : """)
#Now I need to make an if statement to figure out whaat commant the user wishes to use
if a == "1": # Now I need to execute the command in this case this is addition
    a= int(input("Enter the first number you want to add: " ))# Now that i have the first number i know to add i can just ask for the second number and print them at once and add them together
    b= int(input("Enter the second number you want to add: "))# I just need a way to add the both of them together which is the print statemnt
    print(f"{a} + {b} = {a+b}")# I addded them both together and tested amd it works 
elif a == "2":# Now this is for the second function which is substraction    
    a = int(input("Enter the number which you want to subtract from: ")) # This is for the number to subtract from
    b = int(input("Enter thw number which you want to subract from the original number: "))# This is for the number which number you subtract from the origanal number
    print(f"{a} - {b} = {a-b}") # This combines the 2 numbers and gives an output
elif a == "3" :# This is for the second funtion to figure out if it is a division or not
    a = int(input ("Enter the number which you want to Divide from: "))# This is the first number you have to divide from
    b = int(input( "Enterthe number which you want to divide the original number from: "))# This is the number which you divide with
    print(f"{a} ÷ {b} = {a/b}")# this prints and outputs the answer

elif a == "4": # This is to fiqure out that the user wants multiplication
    a = int(input("Enter the number you want to multiply"))# so the number which is getting multiplied first
    b = int(input("Enter the second number you want to multiply"))# The number which is getting multiplied second
    print(f"{a} x {b} = {a * b}")
else: 
    print("Error reading message try again by re starting the program")# Just incase the first input was typre wrongly