Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> b = 10
>>> print(a,b)
12 10
>>> type(a)
<class 'int'>
>>> id(a)
1611122704
>>> id(12)
1611122704
>>> a = 12
>>> b = 12
>>> c = b
>>> id(b)
1611122704
>>> id(a)
1611122704
>>> id(c)
1611122704
>>> import sys
>>> sys.getsizeof(a)
28
>>> d = 12.5
>>> sys.getsizeof(d)
24
>>> id(d)
2464482726944
>>> 
