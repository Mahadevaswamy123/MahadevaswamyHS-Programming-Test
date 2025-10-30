# Problem-3: Conditional odd series
# Author: Mahadevaswamy HS

a = int(input("Enter a number: "))
if a % 2 == 0:
    a -= 1
series = [2 * i + 1 for i in range(a)]
print(", ".join(map(str, series)))
