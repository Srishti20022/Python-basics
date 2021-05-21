Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # python numpy practice
>>> import numpy as np
x = np.array([1, 2, 3, 4, 5, 6,7])
>>> y = np.array([-1, -2, -3, -4, -5, -6, -7)]
SyntaxError: invalid syntax
>>> y = np.array([-1, -2, -3, -4, -5, -6, -7])
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(x+y)
NameError: name 'x' is not defined
>>> x = np.array([1, 2, 3, 4, 5, 6,7])
>>> print(x+y)
[0 0 0 0 0 0 0]
>>> print(np.array([1, 2,3 ]), np.array([4, 5, 6)])
SyntaxError: invalid syntax
>>> print(np.array([1, 2,3 ])+ np.array([4, 5, 6)])
SyntaxError: invalid syntax
>>> print(np.array([1, 2,3 ])+ np.array([4, 5, 6]))
[5 7 9]
>>> list([1, 2,3]) + list([4, 5, 6])
[1, 2, 3, 4, 5, 6]
>>> # here list gets concatenated not added like in case of array
>>> np.arrange(x)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    np.arrange(x)
AttributeError: module 'numpy' has no attribute 'arrange'
>>> np.arrange([1, 6, 3,4 8, 0])
SyntaxError: invalid syntax
>>> np.arrange(3, 1, 5, 1, 5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    np.arrange(3, 1, 5, 1, 5)
AttributeError: module 'numpy' has no attribute 'arrange'
>>> np.arange(x)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    np.arange(x)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> np.arange(1, 0, 3, 9, 2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    np.arange(1, 0, 3, 9, 2)
TypeError: arange() takes at most 4 arguments (5 given)
>>> np.arange(1, 10)
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> # arrange returns array
>>> np.arange(1, 10, 2)
array([1, 3, 5, 7, 9])
>>> np.linespace(1, 20, True, 15)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    np.linespace(1, 20, True, 15)
AttributeError: module 'numpy' has no attribute 'linespace'
>>> np.linespace(1, 20, retstep=True, num=15)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    np.linespace(1, 20, retstep=True, num=15)
AttributeError: module 'numpy' has no attribute 'linespace'
>>> np.linspace(1, 20, retstep = True, num = 15)
(array([ 1.        ,  2.35714286,  3.71428571,  5.07142857,  6.42857143,
        7.78571429,  9.14285714, 10.5       , 11.85714286, 13.21428571,
       14.57142857, 15.92857143, 17.28571429, 18.64285714, 20.        ]), 1.3571428571428572)
>>> np.linspace(1, 20, retstep = False, num = 15)
array([ 1.        ,  2.35714286,  3.71428571,  5.07142857,  6.42857143,
        7.78571429,  9.14285714, 10.5       , 11.85714286, 13.21428571,
       14.57142857, 15.92857143, 17.28571429, 18.64285714, 20.        ])
>>> np.zeroes(10)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    np.zeroes(10)
AttributeError: module 'numpy' has no attribute 'zeroes'
>>> np.zeros()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    np.zeros()
TypeError: Required argument 'shape' (pos 1) not found
>>> np.zero(4)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    np.zero(4)
AttributeError: module 'numpy' has no attribute 'zero'
>>> np.zeros(2)
array([0., 0.])
>>> np.zeros(10)
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
>>> np.ones(10)
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
>>> np.hundreds(10)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    np.hundreds(10)
AttributeError: module 'numpy' has no attribute 'hundreds'
>>> w = np.array('1', 1, 1.0)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    w = np.array('1', 1, 1.0)
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
>>> w = np.array(['1', 1, 1.0])
>>> print(w)
['1' '1' '1.0']
>>> #all the elements get changed to higher order datatype
>>> np.zeros_like(w)
array(['', '', ''], dtype='<U3')
>>> np.random.random()
0.7247340450667215
>>> # returns a random value
>>> np.random.random(size = (1 ,2))
array([[0.24140912, 0.44379397]])
>>> np.random.randint(5)
4
>>> # gives an integer between 0 to 5 excluding 5
>>> np.random.randint(5, 20)
6
>>> # gives integer value between 5 to 20 excluding 20
>>> np.random.randint(5, 20, 5)
array([11, 16,  6, 13, 15])
>>> # gives an array consists integer between 5 to 20 excluding of 5
>>> np.random.randint(5, 20, (5, 5))
array([[15, 16, 10, 16, 12],
       [ 7,  6,  8,  6,  5],
       [ 5,  6,  5, 11,  9],
       [18, 16, 17, 12, 17],
       [ 7, 18,  6, 10, 10]])
>>> np.random.random(3, 3)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    np.random.random(3, 3)
  File "mtrand.pyx", line 425, in numpy.random.mtrand.RandomState.random
TypeError: random() takes at most 1 positional argument (2 given)
>>> np.random.randn(3, 3)
array([[ 1.18135887,  1.03085195,  0.07487426],
       [-1.48565264,  0.27321286,  0.25143656],
       [-0.41821191, -0.6248101 , -1.24234367]])
>>> # gives both positive and negative and positive number
>>> print("abx")


