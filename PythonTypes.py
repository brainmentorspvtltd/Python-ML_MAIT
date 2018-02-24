Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> emp = ['Ram',25,'Delhi',25000.00]
>>> emp[0]
'Ram'
>>> emp[-1]
25000.0
>>> emp[::-1]
[25000.0, 'Delhi', 25, 'Ram']
>>> x = []
>>> x.append(12)
>>> x.append(24)
>>> x
[12, 24]
>>> x = [23,45,7,6,9,12,11,49,87]
>>> sorted(x)
[6, 7, 9, 11, 12, 23, 45, 49, 87]
>>> x.sort()
>>> x
[6, 7, 9, 11, 12, 23, 45, 49, 87]
>>> a = []
>>> for i in range(0,51):
	a.append(i)

	
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> a = []
>>> a = [for i in range]
SyntaxError: invalid syntax
>>> a = [i for i in range(0,51)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
>>> a = [j for i in range(0,51)]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a = [j for i in range(0,51)]
  File "<pyshell#21>", line 1, in <listcomp>
    a = [j for i in range(0,51)]
NameError: name 'j' is not defined
>>> x = (12,34,5,78,'hi',10.5)
>>> x[0]
12
>>> x[-1]
10.5
>>> x[0] = 'bye'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x[0] = 'bye'
TypeError: 'tuple' object does not support item assignment
>>> emp = 'Ram',28,'HCL'
>>> emp
('Ram', 28, 'HCL')
>>> emp = name, age, salary = 'Shyam', 29, 12000
>>> emp
('Shyam', 29, 12000)
>>> name
'Shyam'
>>> emp = {'name' : 'ram', 'age':28, 'company':'hcl'}
>>> emp[1]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    emp[1]
KeyError: 1
>>> emp['name']
'ram'
>>> emp.get('name')
'ram'
>>> emp = {'name' : ['ram','shyam'], 'age':[24,25]}
>>> emp['name']
['ram', 'shyam']
>>> emp['name'][0]
'ram'
>>> emp['name'].append('mohan')
>>> emp
{'name': ['ram', 'shyam', 'mohan'], 'age': [24, 25]}
>>> for i in emp:
	print(i)

	
name
age
>>> emp.keys()
dict_keys(['name', 'age'])
>>> emp.values()
dict_values([['ram', 'shyam', 'mohan'], [24, 25]])
>>> emp.items()
dict_items([('name', ['ram', 'shyam', 'mohan']), ('age', [24, 25])])
>>> for i in emp.items():
	print(i)

	
('name', ['ram', 'shyam', 'mohan'])
('age', [24, 25])
>>> s1 = {23,4,56,78,99}
>>> type(s1)
<class 'set'>
>>> 
