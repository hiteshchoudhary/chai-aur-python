n = int(input("Enter the number to add up to: "))  # takes the limit from user
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += i   # adds the current even number to the sum of the previous ones

print(f"Sum of the even numbers upto {n} is {sum_even}")