Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> squares=[]
>>> for value in range(1,21):
	square=value**2
	squares.append(square)
	print(squares)

	
[1]
[1, 4]
[1, 4, 9]
[1, 4, 9, 16]
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25, 36]
[1, 4, 9, 16, 25, 36, 49]
[1, 4, 9, 16, 25, 36, 49, 64]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
>>> squares=[]
>>> for valus in range(1,11):
	square=value**2
	squares.append(square)
	print(squares)

	
[400]
[400, 400]
[400, 400, 400]
[400, 400, 400, 400]
[400, 400, 400, 400, 400]
[400, 400, 400, 400, 400, 400]
[400, 400, 400, 400, 400, 400, 400]
[400, 400, 400, 400, 400, 400, 400, 400]
[400, 400, 400, 400, 400, 400, 400, 400, 400]
[400, 400, 400, 400, 400, 400, 400, 400, 400, 400]
>>> squares=()
>>> for value in range(1,11):
	square=value*2
	squares.append(square)
	print(squares)

	
Traceback (most recent call last):
  File "<pyshell#17>", line 3, in <module>
    squares.append(square)
AttributeError: 'tuple' object has no attribute 'append'
>>> squares=[]
>>> for value in range(1,11):
	squares.append(value**2)

	
>>> print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> digit={1,2,3,4,8,9,6}
>>> max(digit)
9
>>> min(digit)
1
>>> type(digit)
<class 'set'>
>>> type(2)
<class 'int'>
>>> type(%)
SyntaxError: invalid syntax
>>> squares=[value**2 for value in range(1,11):
	 
SyntaxError: invalid syntax
>>> squares=[value**2 for value in range(1,11)]:
	
SyntaxError: invalid syntax
>>> squares=[value**2 for value in range(1,11)]
>>> print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> squares=[value**2 for value in range(1,21)]
>>> print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
>>> squares=[]
>>> for value in range(1,11):
	square=value**2
	squares.append(square)
	print(squares)

	
[1]
[1, 4]
[1, 4, 9]
[1, 4, 9, 16]
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25, 36]
[1, 4, 9, 16, 25, 36, 49]
[1, 4, 9, 16, 25, 36, 49, 64]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> squares=[]
>>> for valus in range(1,11):
	squares.append(valus**2)
	print(squares)

	
[1]
[1, 4]
[1, 4, 9]
[1, 4, 9, 16]
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25, 36]
[1, 4, 9, 16, 25, 36, 49]
[1, 4, 9, 16, 25, 36, 49, 64]
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> square=[]
>>> pa
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    pa
NameError: name 'pa' is not defined
>>> squares=[value**2 for value in range(2,22)]
>>> squares.append(value)
>>> print(squares)
[4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 10]
>>> 