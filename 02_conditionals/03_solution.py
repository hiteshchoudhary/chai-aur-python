# score = 185

# if score >= 101:
#     print("Please verify your grade again")
#     exit()

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("Grade: ", grade)


#### Method 2: by taking input from user

score = int(input("Enter your score: "))

if score < 0:
    print("Invalid score! Score cannot be negative.")
    exit()
elif score > 100:
    print("Invalid score! Please verify your marks again.")
    exit()

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")