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

# Method 1
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

# Method 2
from datetime import date

date1 = date(2024, 12, 10)
date2 = date(2025, 8, 10)
print("The Number of days between the given Data are", (date2 - date1))

# 7. Write a program to input two numbers as input and compute the greatest common divisor(GCD).
# Method 1
a = int(input())
b = int(input())
while b != 0:
    temp = b
    b = a % b
    a = temp
print(a)

# or

# Method 2
import math

n1 = int(input())
n2 = int(input())
print(f"The GCD of {n1} and {n2} is:", end=" ")
print(math.gcd(n1, n2))


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

# Method - 1 this reverse function only worked on list
list.reverse()
print(list)


# Method - 2
print(list[::4])


# Reverse Method in function with string
def my_fun(x):
    return x[::-1]


mytext = my_fun("I wonder how this text looks like backwards")
print(mytext)


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

# Method 1
n = 654
sum = 0
while n > 0:
    p = n % 10
    sum = sum + p
    n = n // 10

print("The sum of digits if :", sum)

# or


# Method 2
def sumdigit(n):

    sum = 0
    while n > 0:
        p = n % 10
        sum = sum + p
        n = n // 10
    return sum


n = int(input("Enter a number: "))
print("The sum of digits if :", sumdigit(n))


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

# 32. Write a python program to fine the odd numbers in an array.abs
# Method 1
import numpy as np

array = np.array([10, 25, 30, 65, 75, 50, 121])

print("**The List of Odd Numbers in this oddArray Array")
for i in range(len(array)):
    if array[i] % 2 != 0:
        print(array[i], end=" ")

# or

# Method 2
list = [10, 25, 30, 65, 75, 50, 121]

print("**The List of Odd Numbers in this oddArray Array")
for i in range(len(list)):
    if list[i] % 2 != 0:
        print(list[i], end=" ")


""" ****** Pattern ****** """
# 1.
for i in range(6, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()

# 2.
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# 33. Advanced print method
message = input("enter a message: ")
print("Hello", message)

# 34. String have a special character or not
string = input("Enter a string: ")
if any(not char.isalnum() for char in string):
    print("String is not accepted")
else:
    print("String is accepted")


# 35. Write a python program 2020 calender (1,1,2020)-(1,12,2020) print january 1,2020 is Wednesday. Note That 2020 is leap year.
import calendar

year = 2020
print("January 1, 2020 is Wednesday.\n")
for month in range(1, 13):
    print(calendar.month(year, month))


# 36. Write a python to print Fibonacci seris by resucrsion.
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


nterms = int(input("How many terms ? : "))
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i), end=" ")


# Method 2
num = 10
n1, n2 = 0, 1
print(n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")


# 37. Write a python program to given string in a new string no duplicate consecutive latters.
# input: Pythhonn  Output: Python
def remove_dup(input_string):
    result = input_string[0]
    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i - 1]:
            result += input_string[i]
    return result


input_string = input("Enter the STRING : ")
print(remove_dup(input_string))


# 38. Write a python program to calculate the sum of all even number (first 100 even number in a list)
list = [x for x in range(2, 202, 2)]
print(list)
sum_of_even_number = sum(list)
print(sum_of_even_number)

# 39. Write a python program to calculate the sum of all odd number (first 100 even number in a list)
list = [x for x in range(1, 201, 2)]
print(list)
sum_of_even_number = sum(list)
print(sum_of_even_number)

# 40. Write a python program to print all the odd number (First 100 odd number in a ascending order)
list = [x for x in range(1, 201, 2)]
list.sort()
print(list)


# 41. Write a python program name of 10 students and input students marks. Find the maximum and minimum marks display their student names.
student = {}
for _ in range(4):
    name = input("Enter Student name : ")
    marks = int(input("Enter marks : "))
    student[name] = marks
max_student = max(student, key=student.get)
max_marks = student[max_student]
min_student = min(student, key=student.get)
min_marks = student[min_student]
print(f"Student with maximum marks is {max_student} with {max_marks} marks")
print(f"Student with minimum marks is {min_student} with {min_marks} marks")

# 42. Write a python programming to find the area of circle and rectangle Take the input from the user.
radius = float(input())
area_circle = 3.14 * radius**2
print("Area of the circle : ", area_circle)
length = float(input())
width = float(input())
area_rectangle = length * width
print("Area of the rectangle : ", area_rectangle)


# 43. Write a python program in a given list of find positive and negative number.
# input = [-4,3,-81,13,5,-23,-52]
# output : positive = 3, negative = 4
list = [-4, 3, -81, 13, 5, -23, -52]
positive_count = sum(1 for num in list if num > 0)
negative_count = sum(1 for num in list if num < 0)
print("Positive number is : ", positive_count)
print("Negative number is : ", negative_count)


# 44. Write a python program concatenate two 3 dimensional numpy array on axis 1.
import numpy as np

array1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array2 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])
result = np.concatenate((array1, array2), axis=1)
print("Array 1 : ", array1)
print("\nArray 2 : ", array2)
print("Concatenate Array : ", result)


# 45. Write a python program to count even odd number in a list using lambda function.
numbers = [1, 7, 9, 4, 2, 6, 5, 8, 3, 10]
count_even = len(list(filter(lambda x: x % 2 == 0, numbers)))
count_odd = len(list(filter(lambda x: x % 2 != 0, numbers)))
print("Even number count is : ", count_even)
print("Even number count is : ", count_odd)


# 46. Write a python program to find key with maximum unique value in a dictionary
# tet_dict={"A":[4,5,6,3],"B":[7,5,9,0],"C":[1,5,9,2]}

test_dict = {"A": [4, 5, 6, 3], "B": [7, 5, 9, 0], "C": [1, 5, 9, 2]}
max_unique_count = 0
key_with_max_unique = None
for key, value in test_dict.items():
    unique_count = len(set(value))
    if unique_count > max_unique_count:
        max_unique_count = unique_count
        key_with_max_unique = key

print(f"key with maximum unique value: ", {key_with_max_unique})


# 47. Write a program to replace 'a' with 'b', 'b' with 'c',...,'z' with 'a' similarly for 'A' with 'B', 'B' with 'C',...,'Z' with 'A' in a file. The other characters should remain unchanged.
def replace_chars(input_string):
    output_string = ""
    for char in input_string:
        if char.isalpha():
            if char == "z":
                output_string += "a"
            else:
                output_string += chr(ord(char) + 1)
        else:
            output_string += char
    return output_string


str = "A B C D E F"
print(str)
print(replace_chars(str))


# 48. Write a function that reads the contents of the file f3.txt and counts the numbers of alphabets, black spaces, lowercase, numbers of words startng with a vowel and number of occurences of a word "hello"
def read_and_count():
    lower_case = 0
    uper_case = 0
    alphabets = 0
    space = 0
    digit = 0
    string_count = 0
    with open("./demo.txt") as demo:
        c = demo.readlines()
    for j in c:
        for i in range(len(j)):
            if j[i].isalpha():
                alphabets += 1
            if j[i].isdigit:
                digit += 1
            if j[i].islower():
                lower_case += 1
            if j[i].isupper():
                uper_case += 1
            if j[i] == " ":
                space += 1
        string_count += j.lower().count("hello")
    print("Alphabets : ", alphabets)
    print("Space : ", space)
    print("Digits : ", digit)
    print("Lower Case : ", lower_case)
    print("Upper Case : ", uper_case)
    print("Count of 'hello' : ", string_count)


read_and_count()


# 49. Write a python function that takes two list and returns True if they have at least one common item.abs
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result


print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))


# 50. Write a NumPy Program to find the most frequent value in an array
import numpy as np

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
print("Original Array :", x)
print("Most Frequent value in the above array :")
print(np.bincount(x).argmax())

# 51. Write a python program for Row-wise element Addition in Tuple Matrix.
tuple_matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
row_sums = []
for row in tuple_matrix:
    row_sums.append(sum(row))
for row in tuple_matrix:
    print(row)
print("Row-wise :", row_sums)

# 52. Write a program to count the number of charactor (charactor frequency) in a string "google.com".
string = "google.com"
freq_count = {}
for char in string:
    if char in freq_count:
        freq_count[char] += 1
    else:
        freq_count[char] = 1
print(freq_count)

# FILE HANDLING
# 1. Open the File on the Server
f = open("Books-Exercise\\demo.txt", "r")
print(f.read())

# 2. Read Only Parts of the File
f = open("Books-Exercise\\demo.txt", "r")
print(f.read(7))

# 3. Read Lines
f = open("Books-Exercise\\demo.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())

# 4. Read All the Lines
f = open("Books-Exercise\\demo.txt", "r")
print(f.readlines())

# 5. Close The file
f = open("Books-Exercise\\demo.txt", "r")
print(f.readlines())
f.close()

# 6. Write to an Existing File
f = open("Books-Exercise\\demo.txt", "a")
f.write("\nNow the file has more content!")
f.close()


f = open("Books-Exercise\\demo.txt", "r")
print(f.read())

# 7. overwrite the content
f = open("Books-Exercise\\demo.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()


f = open("Books-Exercise\\demo.txt", "r")
print(f.read())


# 8. Delete a File
import os

os.remove("demofile.txt")

# 9. Check if File exist
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The File does not exist")


# 2. Write a program to compute the wages of a daily laborer as per the following rules:
# Hours worked Rate Applicable Upto first 8 hrs Rs. 100/-
# a. for next 4hrs Rs. 30/- per hr extra
# b. for next 4hrs Rs. 40/- per hr extra
# c. for next 4hrs Rs. 50/- per hr extra
# d. for rest Rs. 60/- per hr extra

h = int(input("Enter Total worked Hours : "))
wage = 0
if h <= 8:
    wage = 100
elif h <= 12:
    wage = 100 + (h - 8) * 30
elif h <= 16:
    wage = 220 + (h - 12) * 40
elif h <= 20:
    wage = 380 + (h - 16) * 50
else:
    wage = 580 + (h - 20) * 60
print("Your Total wage is =", wage)

# 3. Write a python program to combine two dictionary adding values for common keys.
from collections import Counter

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 100, "b": 200, "d": 400}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)


""" 7 & 8 FEB Questions """
# 1. Print the current data and time in a formatted.
# (Year-Month-Day Hour : Minute)
import datetime

now = datetime.datetime.now()
print("Current Date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# 2. Create a dictionary with the roll number and percentage of 10 students write a program to print only those Roll number from the dictionary whose percentage is greater than 50.
students = {}
for i in range(3):
    roll_no = int(input())
    percentage = float(input())
    students[roll_no] = percentage
print("\nRoll numbers with percentage greate than 50 :")
for roll_no, percentage in students.items():
    if percentage > 50:
        print(roll_no)


# 3. Write a program that print only the element in the lower triagnle part of a square matrix a given below.Do not include the diogonal in lower triangle...abs
""" 1 0 0 0
2 3 0 0
4 5 6 0
7 8 9 10 """

matrix = [[1, 0, 0, 0], [2, 3, 0, 0], [4, 5, 6, 0], [7, 8, 9, 10]]
n = len(matrix)
print("Elements in the lower triagnle (Excluding diogram):")
for i in range(n):
    for j in range(i):
        print(matrix[i][j], end=" ")
    print()


# July 2025
# 1. Write a Python to combine two dictionary adding values for common keys.
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
d3 = {}
for key in set(d1) | set(d2):
    d3[key] = d1.get(key, 0) + d2.get(key, 0)

print(d3)


# 2. Write a program to replace 'a' with 'b','b' with 'c',...,'z' with 'a' and similarly for 'A' with 'B','B' with 'C',...'Z' with 'A' in a file. The other characters should remain unchanged.

# With File
text = open("input.text").read()
result = ""
for c in text:
    if c >= "a" and c <= "z":
        result += "a" if c == "z" else chr(ord(c) + 1)
    elif c >= "A" and c <= "Z":
        result += "A" if c == "Z" else chr(ord(c) + 1)
    else:
        result += c
open("output.txt", "w").write(result)


# Without File Solution
text = "a b c d A B C D"
result = ""
for c in text:
    if c >= "a" and c <= "z":
        result += "a" if c == "z" else chr(ord(c) + 1)
    elif c >= "A" and c <= "Z":
        result += "A" if c == "Z" else chr(ord(c) + 1)
    else:
        result += c
print(result)


# 3. Write a program to compute the wages of a daily laborer as per the following rules :- Hours Worked Rate Applicable Upto first 8 hrs Rs.100/-
#       a For next 4 hrs Rs. 30/- per hrs extra
#       b For next 4 hrs Rs. 40/- per hrs extra
#       c For next 4 hrs Rs. 50/- per hrs extra
#       d For rest Rs. 60/- per hrs extra

h = int(input())
w = 0
if h > 20:
    w += (h - 20) * 60
    h = 20
if h > 16:
    w += (h - 16) * 50
    h = 16
if h > 12:
    w += (h - 12) * 40
    h = 12
if h > 8:
    w += (h - 8) * 30
    h = 8
w += h * 100
print("Wages : Rs.", w)
