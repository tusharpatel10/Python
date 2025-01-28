# 1. write a python program which accepts the value of a circle from the user and compute the area of circle.

#  This Import Method is Pi value.
import math

print(math.pi)

# Method 1
from math import pi

r = int(input())
area = pi * r * r
print(f"The {r} area of circle is :", area)

# or

# Method 2
pi = 3.14
r = int(input())
area = pi * r * r
print("The area of circle is: ", end="")
print(area)


# 2. Wrtie a python program to find the factorial of a given positive number.

# Method 1
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print("The factorial of given number is :", fact)

# Or

# Method 2
n = int(input())
fact = 1
if n < 0:
    print("Factorial does not exist")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        fact *= i
    print("The factorial of", n, "given number is :", fact)


# 3. Write a python program to check the entered number is even or odd.
# Method 1
num = int(input())
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

# Method 2
num = int(input())
if (num % 2) == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# 4. Write a python program to print the calender of January month of the year 2023.

# Method 1
import calendar

year = int(input())
month = int(input())
print("The calender of: ", calendar.month(year, month))

# Method 2
import calendar

print("The calender of: ", calendar.month(2023, 12))


# 5.Write a program to test whether a passed letter is vowel or not?

# Method 1
char = input()
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
if char in vowels:
    print(f"The character '{char}' is a vowel!")
else:
    print(f"The character '{char}' is a consonant!")


# 6. Python program to find number of days between two given dates

from datetime import date as date_n


def number_of_days(date_1, date_2):
    return (date_2 - date_1).days


date_1 = date_n(2013, 4, 23)
date_2 = date_n(2019, 1, 7)
print(
    "\nNumber of days between the given Dates are: ",
    number_of_days(date_1, date_2),
    "days\n",
)


# 7. Write a program to input two numbers as input and compute the greatest common divisor(GCD).

a = int(input())
b = int(input())
while b != 0:
    temp = b
    b = a % b
    a = temp
print(a)


# 8. Calculate Area of triangle by user input base & height in python

b = float(input())
h = float(input())

area = (b * h) / 2
print("The area of the triangle is: ", area)


# 9. Check if a file exists or not in python
import os

file_path = "/usr/local/bina/file.text"
if os.path.exists(file_path):
    print(f"The file {file_path} exists")
else:
    print(f"The --> {file_path}<-- does not exists.")


# 10. write a pyathon program to find sum of three given integers.

num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = num1 + num2 + num3
print(f"The sum of three number is {num1}+{num2}+{num3} = ", sum)


# 11. write a python program to reverse a list of for example.

list = [10, 11, 12, 13, 14, 15, 16]
rev_list = list[::-1]
print(list)
print(rev_list)


# 12. Write a python program to reverse a list of
# for example

list = [10, 11, 12, 13, 14, 15]
print(list)

# Method - 1
list.reverse()
print(list)


# Method - 2
print(list[::4])


# 13. write a python program to solve.
# (x+y)*(x+y)

x = int(input())
y = int(input())
z = (x + y) * (x + y)
print(f"The result of ({x}+{y})*({x}+{y}) =", z)


# 14. Write a python program to multiply two numbers by repeated addition. Example : 6*3=6+6+6
n = 6
s = 3
r = 0
for i in range(s):
    r = r + n
print(f"The three value addition of {n} * {s} = {n} + {n} + {n} =", r)


# 15. Write a Python function that takes a string as parameter and returns a string with every succesive repetitive character replaced by & e.g. Parameter become Par&met&&.
# Method-1
st = "Parameter"
ch = ""
for i in st:
    if i not in ch:
        ch += i
    else:
        ch = ch + "&"

print(st)
print(ch)


# Method - 2
def str_code(st):

    ch = ""
    for i in st:
        if i not in ch:
            ch += i
        else:
            ch = ch + "&"
    print(ch)


st = input()
str_code(st)


# 16. Write a Python function to find the sum of all numbers between 100 and 500 which are divisible by 2.


def sum_div_by2():
    sum = 0
    for i in range(100, 501):
        if i % 2 == 0:
            sum += i
    print(sum)


sum_div_by2()


# 17. Write a Python function to get two matrics and multiply them. Make sure that number of columns of first matrix= number of rows of second.

import numpy as np

a = [[1, 2, 3], [2, 1, 3], [4, 6, 2]]
b = [[7, 1, 4], [5, 3, 1], [1, 2, 4]]

c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
c = np.dot(a, b)
for i in c:
    print(i)


# 18. write a python program to find sum of three given integers.

a = int(input())
b = int(input())
c = int(input())

sum = a + b + c
print(sum)


# 19. Write a python program to solve (X+y)*(x+y).
x = int(input())
y = int(input())

reg = (x + y) * (x + y)
print(f"The result of ({x} + {y}) * ({x} + {y}) =", reg)


# 20. Find The Largest number in the List
list = [200, 35, 456, 203, 806, 15, 666]

print(f"The list of => {list} \nThe Largest number is =", max(list))
print(f"The Smallest number is =", min(list))


# 21. Find the Factorial number.
def fact(n):
    if n == 1:
        f = 1
    else:
        f = n * fact(n - 1)
    return f


num = int(input())
result = fact(num)
print(result)


# 23. Student find the grade result.

english = float(input())
maths = float(input())
chemistry = float(input())
computer = float(input())

sum = english + maths + chemistry + computer

percentage = (sum / 400) * 100
print(f"The total is => {sum}.\nthe percentage is =>", percentage)

if percentage >= 90:
    print("A Grade")
elif percentage >= 80:
    print("B Grade")
elif percentage >= 70:
    print("C Grade")
elif percentage >= 60:
    print("D Grade")
elif percentage >= 40:
    print("E Grade")
else:
    print("Fail")


# 24. Integer is a prime number or not.
num = int(input())
isprime = 1
for i in range(2, num // 2):
    if num % i == 0:
        isprime = 0
        break
    if isprime == 1:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

# 25. Multiply of 3 within 10 and 50 loop.
for i in range(10, 50):
    if i % 3 == 0:
        print(i)


# 26. Given two number calculate to the arithmetic operation.

num1 = int(input())
num2 = int(input())
add = num1 + num2
print(f"The two value of Addition => {num1} + {num2} =", add)
sub = num1 - num2
print(f"The two value of Substract => {num1} - {num2} =", sub)
mul = num1 * num2
print(f"The two value of Multiply => {num1} * {num2} =", mul)
Div = num1 / num2
print(f"The two value of Division => {num1} / {num2} =", Div)


# 27. Write a python program to find the sum of digits of an integer number using while loop.

n = 654
sum = 0
while n > 0:
    p = n % 10
    sum = sum + p
    n = n // 10

print("The sum of digits if :", sum)


# * reverse number.
n = int(input())
sum = 0
while n > 0:
    p = n % 10
    sum = sum * 10 + p
    n = n // 10

print(f"The N number {n} is reverse if :", sum)


# * Palindrome number.
n = int(input())
temp = n
sum = 0
while n > 0:
    p = n % 10
    sum = sum * 10 + p
    n = n // 10

if temp == sum:
    print("The given Number is palindrome")
else:
    print("The given Number is not palindrome")


# 28. Write a python program
# input = "abc","xyz"
# output = "xyc","abz"

a = "abc"
b = "xyz"
print("before swap:", a, b)
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]

print("after swap:", a1, b1)


# 29. Pattern

n = 6
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()


# 30. Write a python function to find the sum of all numbers between 100 and 500 which are divisable by 2.
def abc(a, b):
    sum = 0
    for n in range(a, b + 1):
        if n % 2 == 0:
            sum += n

    print("The sum of even numbers is :", sum)


a = 100
b = 500
abc(a, b)


# 31. Write a Python program to show the character and count of its repitition count of repeated characters in a string.

string = "thequckbrownfothsialistfoefmq"
dictionary = {}
for char in string:
    if char in dictionary.keys():
        dictionary[char] += 1
    else:
        dictionary[char] = 1
for char in dictionary:
    print(char, "=>", dictionary[char])


# * Pattern
for i in range(6, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()


# 32. Advanced print method
message = input("enter a message: ")
print("Hello", message)
