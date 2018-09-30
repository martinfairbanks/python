#Python language study
#To study this you could paste the code snippets into the python shell
#or in the interactive shell in Visual Studio.
#You could also step through it using the Visual Studio debugger.

#math
#--------------------------------------------------

x=0
x += 1
print(x)

#integer division/floored
floored = 21 // 8
print(floored)

#division
division = 21 / 8
print(division)

#exponent
print(2**2)

#modulo/remainder
print(4%2)

#swap two values
x = 1
y = 2
x, y = y, x
print(x, y)


foo = 5

if foo < 5:
	print("The number is lower than 5!")

if foo == 5:
	print("the number is 5!")

#conversions
number = 6
secondNumber = "6"
print(str(number) + " + " + secondNumber + " = " + str(int(secondNumber) + number))

number = int(5.6)
print("Truncate: " + str(number))
number = int(5.6) + 1
print("Round up: " + str(number)) 


#None -> like null in C, represents the absence of a value
#--------------------------------------------------
#print returns None. python adds return None to all functions with no return statement
retVal = print("Hello")
print(retVal)


#strings, both '' and "" is valid for strings
#--------------------------------------------------
name = "Foo"

print(10, "Hello, " + name + "!")

#prints a blank line
print()

if name is "sdf":
	print("")
elif name is "Foo":
	print("Your name is Foo!")
else:
	print("")

#when * is used on strings it becomes the string replication operator
print("foo" * 5)

languages = ['Lisp', 'Smalltalk', 'C', 'Python', 'Swift']

#replace the newline character with empty string
print("Foo", end='')
print("Bar")

#replace the separation
print("banana", "orange", "apple", sep=', ')


#boolean expressions and control flow
#--------------------------------------------------
print('What is your name?')   
#name = input()
name = "Martin"

if name: #check true or false
	print("Thank you for entering your name.")
else:
	print("You didn't enter your name.")

if (2 < 4) and (5 == 5):
	print("True!")

if ((2 < 4) or (5 > 10)) and not (1 + 1 == 2):
	print("True!")
elif (1 > 4):
	print("True!")
else:
	print("False!")


#loops and control flow
#--------------------------------------------------
for l in languages:
	print(l)
	print(len(l))

for l in languages[1:3]:
	print(l)

foo = 0
while foo < 10:
	foo += 1
	if foo == 2:
		continue    #jump to beginning of while loop

	print(foo)
	
	if foo == 5:
		break

#while True:
#    print("asd")


#range loops
#--------------------------------------------------
for x in range(5):
	print(x)

#prints 5 to 9
for x in range(5,10):
	print(x)
	
#prints 5 to 19 in steps of 2
for x in range(5,20,2):
	print(x)

for i in range(5, 0, -1):
	print("Hi five times " + str(i))

total = 0
for num in range(101):
	total = total + num
print("Total numbers:", total)

magicNumber = 26
numbersTaken = [2, 5, 9, 14, 16]

for n in range(101):
	if n is magicNumber:
		print(n, "is the magic number!")
		break
	else:
		print(n)

print("Numbers still available:")

for n in range(1, 20):
	if n in numbersTaken:
		continue #go back to start of the for loop
	print(n)

for x in range(1,20): 
	if x%4 is 0:
		print(x,"is a multiple of 4.") 
	else:
		print(x)


#functions
#--------------------------------------------------
def foo(num):
	print("Inside foo function")
	amount = num * 10
	return amount	

print(foo(0.5))

#flexible amount of arguments
def addNumbers(*args):
	total = 0
	for a in args:
		total += a
	print(total)

addNumbers(3)
addNumbers(43,43,11,56,3452,3525)


#scope
#--------------------------------------------------
def foobar():
	num = 10                    #local variable
	print("Scope:", variable)   #global variable

variable = 9999                 #global variable
foobar()

def number():
	#refer to the global variable
	global variable
	variable = 10

number()
print(variable)

def square(x):
    return x**2

print(square(8))

#exception handling
#--------------------------------------------------
def div(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print("Error!")

print(div(0))
