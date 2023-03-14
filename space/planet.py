# hello
# radius = input('Tell me what your area is, fool: ')

# area = 3.142*int(radius)**2 
# print("Your area is: ", area)

# num1 = 5.3453346
# num2 = 10.78636678

# print('num1 is {0:.2f} and num2 is {1:.2f}'.format(num1, num2)) # string formatting

# using f strings
# print(f'num1 {num1} is and num2 is {num2}')

# class Planet:
#     def __init__(self):
#         self.name = 'Hoth'
#         self.radius = 200000
#         self.gravity = 5.5
#         self.system = 'Hoth System'


#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'

# hoth = Planet()                   #an instance of the class object that has access to all the properties of the object assigned with the self attribute/method
# print(f'the name is: {hoth.name}')
# print(f'the radius is: {hoth.radius}')
# print(f'the gravity is: {hoth.gravity}')
# print(hoth.orbit())  #attribites aren't the only things that can be inherited by the instance of an object, methods can also be inherited



class Planet: 
    
    
    shape = 'round'   # this now is a class attribute that everything (all the instances) has access to(globally scoped for that class). print(Planet.shape)   


                                              # basically the constructor or building template for the object
    def __init__(self, name, radius, gravity, system):  # the reason we do it this way is so we can create different instances of the object and not have hard coded attributes.
        self.name = name                                # we can pass in the attributes as arguements
        self.radius = radius
        self.gravity = gravity
        self.system = system


    def orbit(self):                                    # function/method as an attribute that all instances have access to
        return f'{self.name} is orbiting in the {self.system}'  # self works like (this) in javascript. any method of attibutes that have self injected in it is an instance method/attribute. What this means is the scope is limited to just the object instances and the values can be dynamically changes with arguements


    @classmethod                         # functions/methods that are on class level (scope)
    def commons(cls):                    # this cls gives us access to class level attributes
        return print(f'All planets are {cls.shape} because of gravity')



    @staticmethod
    def spin(speed = '2000 miles per hour'):      # static methods are accessible by everybody (instance and class)  but won't take anything expect the parameters explicitly passed into it... not that the variables/parameters will be declared elsewhere and referenced
        return f'Planets spins and spins at {speed}' # speed = ... is a default value that you can override





