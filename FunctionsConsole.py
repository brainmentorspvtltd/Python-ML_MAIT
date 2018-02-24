Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def show():
	print("Hello")

	
>>> show()
Hello
>>> def temp_conv(c):
	return 9/5 * c + 32

>>> temp = [28.9,33.4,38.9,31.7,37.2]
>>> temp_conv(temp)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    temp_conv(temp)
  File "<pyshell#6>", line 2, in temp_conv
    return 9/5 * c + 32
TypeError: can't multiply sequence by non-int of type 'float'
>>> for t in temp:
	temp_conv(t)

	
84.02
92.12
102.02
89.06
98.96000000000001
>>> list(map(lambda c : 9/5 * c + 32, temp))
[84.02, 92.12, 102.02, 89.06, 98.96000000000001]
>>> lambda : "hello"
<function <lambda> at 0x0000024ECDB65A60>
>>> m = lambda : "hello"
>>> type(m)
<class 'function'>
>>> m()
'hello'
>>> map(temp_conv, temp)
<map object at 0x0000024ECDB73B38>
>>> list(map(temp_conv, temp))
[84.02, 92.12, 102.02, 89.06, 98.96000000000001]
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/PythonFunctions.py ========
[94.1, 98.06, 102.02, 85.64, 73.22]
>>> 
=========== RESTART: C:/Users/asus/Desktop/PythonMAIT/Example_1.py ===========
Sorted data [{'id': 101, 'name': 'Redmi', 'price': 12000}, {'id': 105, 'name': 'Redmi', 'price': 15000}, {'id': 106, 'name': 'Nokia', 'price': 18000}, {'id': 107, 'name': 'Vivo', 'price': 20000}, {'id': 103, 'name': 'Samsung', 'price': 52000}, {'id': 104, 'name': 'Apple', 'price': 65000}, {'id': 102, 'name': 'Apple', 'price': 82000}, {'id': 108, 'name': 'Apple', 'price': 100000}]
>>> 
=========== RESTART: C:/Users/asus/Desktop/PythonMAIT/Example_1.py ===========
{'id': 101, 'name': 'Redmi', 'price': 12000}
{'id': 105, 'name': 'Redmi', 'price': 15000}
{'id': 106, 'name': 'Nokia', 'price': 18000}
{'id': 107, 'name': 'Vivo', 'price': 20000}
{'id': 103, 'name': 'Samsung', 'price': 52000}
{'id': 104, 'name': 'Apple', 'price': 65000}
{'id': 102, 'name': 'Apple', 'price': 82000}
{'id': 108, 'name': 'Apple', 'price': 100000}
>>> def even(num):
	return num % 2 == 0

>>> even(12)
True
>>> numbers = [i for i in range(2,51)]
>>> for n in numbers:
	even(n)

	
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
>>> list(filter(even, numbers))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> 
=========== RESTART: C:/Users/asus/Desktop/PythonMAIT/Example_1.py ===========
{'id': 101, 'name': 'Redmi', 'price': 12000}
{'id': 105, 'name': 'Redmi', 'price': 15000}
{'id': 106, 'name': 'Nokia', 'price': 18000}
{'id': 107, 'name': 'Vivo', 'price': 20000}
{'id': 103, 'name': 'Samsung', 'price': 52000}
{'id': 104, 'name': 'Apple', 'price': 65000}
{'id': 102, 'name': 'Apple', 'price': 82000}
{'id': 108, 'name': 'Apple', 'price': 100000}
{'id': 102, 'name': 'Apple', 'price': 82000}
{'id': 103, 'name': 'Samsung', 'price': 52000}
{'id': 104, 'name': 'Apple', 'price': 65000}
{'id': 108, 'name': 'Apple', 'price': 100000}
>>> 
=========== RESTART: C:/Users/asus/Desktop/PythonMAIT/Example_1.py ===========
{'id': 101, 'name': 'Redmi', 'price': 12000}
{'id': 105, 'name': 'Redmi', 'price': 15000}
{'id': 106, 'name': 'Nokia', 'price': 18000}
{'id': 107, 'name': 'Vivo', 'price': 20000}
{'id': 103, 'name': 'Samsung', 'price': 52000}
{'id': 104, 'name': 'Apple', 'price': 65000}
{'id': 102, 'name': 'Apple', 'price': 82000}
{'id': 108, 'name': 'Apple', 'price': 100000}
------------------------------------------
{'id': 102, 'name': 'Apple', 'price': 82000}
{'id': 103, 'name': 'Samsung', 'price': 52000}
{'id': 104, 'name': 'Apple', 'price': 65000}
{'id': 108, 'name': 'Apple', 'price': 100000}
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py ========
hello
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py ========
<function outer.<locals>.inner at 0x000001BDC8E13E18>
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py ========
Traceback (most recent call last):
  File "C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py", line 17, in <module>
    print(func_())
NameError: name 'func_' is not defined
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py ========
hello
>>> def calc(x,y):
	return x+y, x-y, x/y, x*y

>>> calc(12,5)
(17, 7, 2.4, 60)
>>> a,b,c,d = calc(12,5)
>>> a
17
>>> b
7
>>> c
2.4
>>> d
60
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py ========
(<function outer.<locals>.inner at 0x000001114DDB3E18>, <function outer.<locals>.inner_2 at 0x00000111503A4730>)
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py ========
hello
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py ========
hello world
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/NestedFunction.py ========
hello
>>> calc(12,5)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    calc(12,5)
NameError: name 'calc' is not defined
>>> def calc(x,y):
	return x+y, x-y, x/y, x*y

>>> a,b = calc(12,5)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a,b = calc(12,5)
ValueError: too many values to unpack (expected 2)
>>> a,*b = calc(12,5)
>>> a
17
>>> b
[7, 2.4, 60]
>>> for i in range(0,20,1.5):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for i in range(0,20,1.5):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
