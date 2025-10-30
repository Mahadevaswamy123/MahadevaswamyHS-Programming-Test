# Problem-4: Count multiples of 1–9
# Author: Mahadevaswamy HS

nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = {}

for i in range(1, 10):         
    result[i] = sum(1 for n in nums if n % i == 0)

print(result)
