#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The bigger number is: ", num1)
elif num2 > num1:
    print("The bigger number is: ", num2)
else:
    print("The numbers are equal.")
#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 == num2:
    print('Equal')
else:
    print("Not Equal")
#Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
print("Sum: ", sum)
#Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

product = num1 * num2
print("Product", product)
#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 != 0:
    quotient = num1 / num2
    print("Quotient:", quotient)
else:
    print("Can't be divided by zero.")
#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 ** num2
print("Result:", result)
#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
sum = 0 

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    sum += num

print("Sum of all numbers:", sum)
#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_count = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 != 0:
        odd_count += 1

print("Number of odd numbers:", odd_count)
#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
for num in range(0 , 101, 2):
    print(num, end=" ")
#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
for num in range(101):
    if num % 10 != 0:
        print(num, end=" ")