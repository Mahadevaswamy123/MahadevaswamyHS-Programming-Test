# Problem-2: Generate odd number series
# Author: Mahadevaswamy HS

a = int(input("Enter a number: "))
series = [2 * i + 1 for i in range(a)]
print(", ".join(map(str, series)))
