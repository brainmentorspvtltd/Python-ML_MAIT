Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a, b = 12, 13
>>> a,b = b,a
>>> a
13
>>> b
12
>>> a = "Hello"
>>> a * 10
'HelloHelloHelloHelloHelloHelloHelloHelloHelloHello'
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/01-PythonBasic.py ========
34
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/01-PythonBasic.py ========
Enter first number : 12
Enter second number : 13
1213
>>> 
======== RESTART: C:/Users/asus/Desktop/PythonMAIT/01-PythonBasic.py ========
Enter first number : 12
Enter second number : 13
25
>>> for i in range(0,10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(0,6):
	print('*'*i)

	

*
**
***
****
*****
>>> for i in range(0,10):
	print(' ' * (10-i) + '*' * (2*i + 1))

	
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
>>> a = "Hello world"
>>> a[0]
'H'
>>> a[4]
'o'
>>> a[-1]
'd'
>>> a[-2]
'l'
>>> a[0:4]
'Hell'
>>> a[0:]
'Hello world'
>>> a[:5]
'Hello'
>>> a[:]
'Hello world'
>>> a[0:10:2]
'Hlowr'
>>> a[::-1]
'dlrow olleH'
>>> 
