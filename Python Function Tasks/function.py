
#1. creat a simple function that take 2 numbers and print their values


def f (x,y):
    x = 5
    y = 10
    z = x+y
    print (z)
    return

#2. Create a simple function that takes 2 numbers and return their values

def f (a,b):
    a = 5
    b = 10
    return (a+b)
#3. In the above return function, use keyword arguments when calling the function

'''
f ()
'''

#4. In the above return function, give x and y default values of 0 and call the function with no arguments

def f(x=0, y=0):
    result = x+y
    return (result)
l= f ()
print (l)


#5. Create a function that can take any number of arguments and print the sum of them

def f (x,y):
    result = x+y
    return(result)
l= f(4,4)
print(l)

#6.Create the same sum function using the lambda


#7. Call the lambda function at the same definition line


#8. Write the difference between the local variable and global variable
'''
A global variable is a variable that is accessible globally.
A local variable is one that is only accessible to the current scope, such as temporary variables used in a single function definition.
'''

#example :
q = "I love coffee" # global variable
def f(p):
    p = 'Me Mohammad, You Jane.' # local variable
    print (p)
print (q)

