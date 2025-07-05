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
