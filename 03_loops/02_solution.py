# n = 10
# sum_even = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         sum_even += 1

# print("Sum of even number is: , ", sum_even)

# This shows that it is 5 but in reality it's 30 so is this correct sir i don't know but i see my code and your code is simmiler but then also its output is diffrent 

size = 10
sum = 0

for i in range(1,size+1) :
    if i % 2 == 0 :
        sum+= i
    
print(sum)
