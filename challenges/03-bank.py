print("Welcome to Chase bank.")
print("Have a nice day!")

print("Welcome to Chase bank.\n")
# print("Have a nice day!")

print("Would you like to: \n")
print("1. check account balance")
print("2. withdraw cash")
print("3. make a deposit ")

operation = input()

if operation == "1":
    print("your account balance is -20,000.\n")

elif operation == "2":
    print("insuffecient funds\n")

elif operation == "3":
    print("Gimme that money\n")

print("all set ? yes : no  ")  

response = input()

if response == "yes":
    print("thank you, goodbye")
elif response == "no":
    print("get a job")
print()