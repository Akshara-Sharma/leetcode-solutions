nums = [2, 2, 1, 1, 4]

# traverse the array and print the number whose count == 1

for num in nums:
    if (nums.count(num) == 1):
        print(num)