1 To create sequences of numbers, NumPy provides a function _____ analogous to range that return arrarys instead of list.
- ans. Arrange

2 ndarray is also known as the ____ array.
- Alias

3. What will be the output of the following?
import numpy as np

print(np.minimum([2, 3, 4], [1, 5, 2]))

Ans. [1,3,2]


4. Which attribute is used to find the data type of numpy array?
Ans. dtyp

5 what will be output for the following code ?
import numpy as np

a = np.array([1, 2, 1, 5, 8])
b = np.array([0, 1, 5, 4, 2])
c = a + b
c = c * a
print(c)
Ans. 6


6 what will be output for the following code ?
import numpy as np

a = np.array([1.1, 2, 3])
print(a.dtype)

Ans. float64

7 what will be output for the following code ?
import numpy as np

a = np.array([11, 2, 3])
print(a.min())

Ans. 2


8. What are the attribute of numpy array?
Ans. Shape, dtype, ndim


9 what will be output for the following code?
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]])
print(a.shape)
Ans. (3,3)


10 what will be output for the following code?
import numpy as np

a = np.array([1, 2, 3])
print(a.ndim)

Ans. 1


11 what will be output for the following code ?
import numpy as np

z = [1, 2, 3]
y = np.array(z)

Ans. To convert z to array


12 what will be output for the following code ?
import numpy as np

a = np.array([[1, 2, 3], [0, 1, 4], [11, 22, 33]])

print(a.size)

Ans. 9


13 What is the purpose of zeros() function used in NumPy array ?
Ans. To make a matrix with all elements 0


14 what will be output for the following code ?
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[2, 2])
Ans. 11

14 what will be output for the following code ?
import numpy as np

a = np.array([1, 2, 3, 5, 8])
b = np.array([0, 1, 5, 4, 2])
c = a + b
c = c * a
print(c[2])

Ans. 24


15 what will be output for the following code ?
import numpy as np

a = np.array([[1, 2, 3]])
print(a.shape)

Ans. (1,3)


16 what will be output for the following code ?
import numpy as np

a = np.array([1, 5, 4, 7, 8])
a = a + 1
print(a[1])

Ans. 6

17 what will be output for the following code ?
import numpy as np

print(np.maximum([2, 3, 4], [1, 5, 2]))

Ans. [2 5 4]


18 what will be output for the following code ?
import numpy as np

a = np.array([2, 3, 4, 5])
b = np.arange(4)
print(a+b)

Ans. [2 4 6 8]


18 what will be output for the following code ?
import numpy as np

y = np.array([[11, 12, 13, 14], [32, 33, 34, 35]])
print(y.ndim)

Ans. 2


19 what will be output for the following code ?
import numpy as np

a = np.array([1, 2, 3])
print(a.ndim)
Ans. 1


20 what will be output for the following code ?
import numpy as np

a = np.array([2, 3, 4, 5])
print(a.dtype)
Ans. int32


21 what will be output for the following code ?
import numpy as np

a = np.array([1, 2, 3, 4])
x = a.tolist
Ans. list


22 what will be output for the following code ?
import numpy as np

a = np.array([[1, 2, 3], [5, 5, 6]])
print(a.shape)
Ans. (2, 3)

23 What is the use of the ones() function in NumPy array in Python ?
Ans. To make a matrix with all element 1


24 what will be output for the following code ?
import numpy as np

ary = np.array([4, 5, 6, 7, 8])
ary = ary + 1
print(ary[1])
Ans. 6


25 What is the default data type of NumPy arrays ?
Ans. float64


26 what will be output for the following code ?
import numpy as np

a = np.arange(10)
print(a[2:5])
Ans. [2,3,4]

27 which of the following is used to create an indentity matrix in NumPy?
Ans. eye()

28. Which of the following is used to reshape a NumPy array ?
Ans. reshape() and resize()


29 what will be output for the following code ?
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.stack((a, b))
print(c)
Ans. [[1,2,3] [4,5,6]]


30 Which of the following is used to find the maximum element in a NumPy array ?
Ans. max(), maximum(), and amax()


31 what will be output for the following code ?
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(c)
Ans. [ 1 2 3 4 5 6]


32 What is the purpose of NumPy in Python ?
(1) To provide a powerful N-dimensional array object
(2) To provide functions for performing mathematical operations on arrays
(3) To provide tools for integrating C/C++ and Fortran code with Python


33. How is the basic ndarray create in NumPy ?
Ans. By passing a Python list of the np.array() function


34 What is the Purpose of NumPy in Python ?
Ans. To do numerical calculations, and To do scientific computing

35. NumPy package is capable to do fast operations on arrays.
Ans. True

36. Amongst which of the following is true with reference to Pip in Python ?
(1) Pip is a standard package management system
(2) It is used to install and manage the software packages writeen in Python.
(3) Pip can be used to search a Python package

37. NumPy arrays can be ____.
Ans. indexed, Sliced, and Iterated

38. What is the Output of following code ?
import numpy as np

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
b = a
print(b is a)
Ans. True

39. Using ndim we can find
Ans. We can find the dimension of the array

40. NumPy developed by ?
Ans. Travis Oliphant

41. The most important object defined in NumPy is an N-dimensional array type called ?
Ans. ndarray

42. For performing the addition of two numbers, which of the following symbol in a flow chart is used ?
Ans. Processing

43. Which of the following is not a control structure ?
Ans. Process


44. What is the output of the following code ?
def s(n1):
    print(n1)
    n1 = n1 + 2


n2 = 4
s(n2)
print(n2)

Ans. 4 4


45. What is the output of the following code ?
x = 123
for i in x:
    print(i)

Ans. Error ('int' object is not iterable)


46. Choose the correct option with repect to Pyhton.
Ans. Tuples are immutable while lists are mutable

47. f.read(5) will read ____ from a file (file object is 'f).
Ans. 5 characters


48. Which one of the following is immutable data type ?
Ans. tuple


49. In Python language, which of the following operators is the correct option for raising k to the power 1 ?
Ans. k**1 (power)

50. Which of the following will read the entire content of file (file object 'f') ?
Ans. f.read()


51. What is the output of the following ?
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)

Ans. 4310


52. The Sequence logic will not be used while ____
Ans. Adding two numbers


53. What will be the output of the following code ?
tuple1 = (5, 1, 7, 6, 2)
tuple1.pop(2)
print(tuple1)
Ans. Error


54. Pictorial representation of an algorithm is called as ____
Ans. Flow Chart


55. What will be the output of the following code ?
def display(b, n):
    while n > 0:
        print(b, end="")
        n = n - 1


display("z", 3)

Ans. zzz

56. The Connector symbol for flow chart is ____
Ans. Circle

57. What is a variable defined outside a function reffered to as ?
Ans. A Global Variable

58. Recursive function is ____
Ans.  A function that calls itself

59. Which function is used to add an element (5) in the list ?
Ans.  list1.append(5)

60. What will be output for the following code ?
import numpy as np

ary = np.array([1, 2, 3, 5, 8])
ary = ary + 1
print(ary[1])
Ans.  3

61. In which format does a Binary file contain information ?
Ans. Same format in which the data is held in memory


62. Which of the following will delete the key-value pair for key=tiger in the dictionary ?
dic = {"Lion": "wild", "tiger": "wild", "cat": "domestic", "dog": "domestic"}
Ans.  del dic["tiger"]


63. What will be the output of the following Python code ?
d1 = {"abc": 5, "def": 6, "ghi": 7}
print(d1[0])
Ans. Error


64. What will be the output of the following Python code ?
def power(x, y=2):
    r = 1
    for i in range(y):
        r = r * x
    return r


print(power(3))
print(power(3, 3))
Ans.  9  27


65. The contents inside the 'for loop' are seperated by :
Ans. semicolon

66. In which of the following, data is stored permanently ?
Ans. B

67. A _____ stores information in the form of a stream of ACSII or Unicode characters, i.e., human readable.
Ans. Text file

68. Which of the following are valid string manipulation functions in Python ?
Ans. count(), strip(), and upper()


69. What is 'f' in the following statement ?

f=open("Data.text","r")
Ans. File Handle


70. ____ is part of user documentation.
Ans.  Installation Guide


71. Determine the output:
for i in range(20, 30, 10):
    j = i / 2
    print(j)
Ans. 10.0


72. What will be the output of the following ?
import numpy as np

print(np.minimum([2, 3, 4], [1, 5, 2]))
Ans. [1 3 2]

73. Python is a case sensitive language when dealing with indetifiers.
Ans. True


74. What is the output of the following code ?
print(bool(0), bool(3.14159), bool(-30), bool(1.0 + 1j))
Ans. False True True True


75. Actual instructions in flowcharting are represented in ____.
Ans.  Boxes


76. What is the output of the following ?
x = "abcd"
for i in range(len(x)):
    i.upper()
print(x)
Ans. Error


77. Any algorithm is a program written according to proper syntax.
Ans. False


78. What will be output of the following pseudo-code ?
Integer a
set a = 5
do
    print a - 2
    a = a - 1
while (a != 0)

end while
Ans.  None of these


79. Admin opened a file in python using open() function but forgot to specify the mode. In which mode the file will open ?
Ans.  read


80. Which of the following is true for variable names ?
Ans. unlimited lenght

81. Fill in the blank.
import pickle

f = open("data.dat", "rb")
d = ____.load(f)
f.close()
Ans.  pickle