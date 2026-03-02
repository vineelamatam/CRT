'''
1) write a python code to count the digits of number?
Ex: 123 --> output :3
2)sum of the digits of a number?
Ex:123-->1+2+3=6
3)product of the digits of a number?
4)reverse the number?
5)even and odd numbers?
6)print largest digit of a number?

'''
n = int(input())
count = 0 
while n > 0:
    count += 1 
    n //= 10  
print("Number of digits:", count)

n = int(input("Enter a number: "))
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    n //= 10

print("Sum of digits:", sum_digits)

n = int(input("Enter a number: "))
product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n //= 10

print("Product of digits:", product)

n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed number:", reverse)

n = int(input("Enter a number: "))
even_count = 0
odd_count = 0

n = abs(n)

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n //= 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)

n = int(input("Enter a number: "))
largest = 0

n = abs(n)

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10

print("Largest digit:", largest)
