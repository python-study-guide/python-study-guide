

# You define a new function using the 'def' key word. 

def greetings(name):
    print('Hello', name)


greetings('Peter')


# Functions can access global variable (but this isn't good practice), e.g.

message="Hello Tom"

def greetings2():
    print(message)

greetings2()



def addition(a,b):
    return a+b

result=addition(4,6)
print(result)