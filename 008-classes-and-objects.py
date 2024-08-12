class Person:

    # All classes must have a function called "__init__". This is a special function that is run
    # when generating/initialising a new object. 
    # the first parameter must be the special key word, "self", followed by all the property names your object will have. 
    def __init__(self, nameOfPerson, ageOfPerson):
        self.name = nameOfPerson
        self.age = ageOfPerson


    # this is how you define a method.
    # Again, you need add the special key word "self" as the very first parameter  
    def greetings(self, title):
        print('Hello', title, self.name + ', you are', self.age, 'years old.')

    def goodbye(self):
        print('farewell')
    

Alex = Person('Alexander', '32')

print(Alex.name)
print(Alex.age)

Alex.greetings('Mr')


# Here's an example of inheritance. Here we are creating a child class for the "Person" class above, called "Employee"

class Employee(Person):

    # For child classes, the init function is optional, but if you do omit it, then the parent class's init function
    # get run instead. 
    def __init__(self, nameOfPerson, ageOfPerson, payrollId, annualPay):
        self.id = payrollId
        self.salary = annualPay
        Person.__init__(self, nameOfPerson, ageOfPerson)


    def getDetails(self, title):
        print('Hello', title, self.name + ', you are', self.age, 'years old. Your id is,', self.id, 'and your salary is,', self.salary, 'dollars.')  

    # This method is overriding the parent class's methpd of the same name. 
    def goodbye(self):
        # you can use the "super()" method to call a parent class's method. 
        super().goodbye()
        print('See you tomorrow')


Pete = Employee('Peter', '18', '223432', '30000')  

print(Pete.name)
print(Pete.age)
print(Pete.id)
print(Pete.salary)

Pete.greetings('Mr')
Pete.getDetails('Mr')
Pete.goodbye()

