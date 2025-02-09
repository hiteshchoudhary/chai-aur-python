# n = 10
# sum_even = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         sum_even += 1

# print("Sum of even number is: , ", sum_even)

# The Correct Solution would be :

num = int(input("Please Enter a number : "))
sum = 0

for nums in range(num+1):
    if nums % 2 == 0:
        sum += nums

print(sum)
