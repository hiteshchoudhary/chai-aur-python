# age = 26
# day = "Wednesday"

# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     # price = price - 2
#     price -= 2

# print("Ticket price for you is $",price)



# method 2: Using if-else statements
age = int(input("Enter your age: "))
day = input("Enter the day: ").strip().lower()
discount = 2
if age >= 18:
    if day == "wednesday":
        price = 12 - discount
        print(f"Ticket price for you is ${price}")
    else:
        price = 12
        print(f"Ticket price for you is ${price}")
else:
    if day == "wednesday":
        price = 8 - discount
        print(f"Ticket price for you is ${price}")
    else:
        print(f"Ticket price for you is ${8}")























