# 9 - Classes
This chapter deals with object-oriented programming, one of the most powerful approaches to writing software. Object-oriented programming defines the natures of general classes of objects, and then creates individual objects, called instances, that belong to these classes, and thus come equipped with the behaviour characteristic to them. OOP teaches one to see the world as a programmer does.

## 9.1 - Creating and using a class
Example of simple Python class:

```
class Dog():                                         # Name usually capitalized
	def __init__(self, name, age):                   # Constructor
		self.name = name                             # Attributes
		self.age = age
		
	def bark(self):                                  # Methods
		print(f"{self.name.title()}: Woof, Woof!")
	def sit(self):
		print(f"{self.name.title()} is sitting.")	
```

A function inside a class is called a **method**. The `__init__()` method is the class' constructor, which is run every time an instance of the class is created. Every method definition must include the `self` parameter, though it need not be passed as argument when the method is called. 

Any variable prefixed with `self`, such as `self.name` is available to every method in the class and is called an **attribute**. The attributes of class instances created outside the class are accessible.

We can create an instance and give its constructor arguments using the name of the class. Then we can access it's attributes and use it's methods with dot notation:

```
my_dog = Dog("cobi", 9)

print(f"My dog's name is {my_dog.name}.")
my_dog.bark()
```

## 9.2 - Working with classes and instances
The values of the attributes of a class instance can be modified directly or through a dedicated method. It’s usually much better to use dedicated methods, as that
1) hides the implementation details, which a user doesn’t need to see.
2) ensures that class attributes are never given wrong values.

Each attribute must have an initial value, so, those attributes that aren’t given as arguments in the creation of an instance must be given values in the body of the `__init__()` constructor.

```
Car mi_coche("honda", "civic")

mi_coche.set_odometer(-10)
>>> "ERROR, mileage can't be negative."
```

## 9.3 - Inheritance
If you write a class that is a specific kind of another class, you can use **inheritance** to avoid rewriting the same structures. When a class inherits from a parent class, it automatically receives all of its attributes and methods, along with new ones that might be defined for it.

```
class Car():  # No parent class
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
		
	def describe_car(...)
		
	...
	
class ElectricCar(Car):  # Superclass specified in parentheses
	def __init__(self, brand, model, battery):
		super().__init__(brand, model)
		self.battery_type = battery  # New attribute

		
my_car = ElectricCar("tesla", "cybertruck", "12V")
my_car.describe_car() # We can use the parents method
```

The `super()` function is used by the subclass to access the superclass, or parent class, in this case, to access its constructor and give values to brand and model. The parent class needs to be included in the file and be defined before the child class.

If a child class needs to use a method or attribute from its parent class in a different way (or disable it) it can **override** it by defining its own method or attribute with the same name, which Python will use and ignore the inherited one.

As your classes grow in complexity, you may find that, to reduce your long lists of attributes and have a more elegant representation of the world in your code, you can **use class instances as attributes**. Just as real-world objects are made up of other complex objects, a class can be made up of other classes. 

```
...
class Battery():
	def __init__(self, capacity = 70):
		self.capacity = capacity
	
	def describe_battery(self):
		print(f"- Capacity = {self.capacity} kWh")
	

class ElectricCar(Car):
	def __init__(self, brand, model):
		super().__init__(brand)
		self.battery = Battery()	
	

my_tesla = ElectricCar("tesla", "cybertruck")
my_tesla.battery.describe_battery() # Calling the method of a class atribute
```

By modelling more complicated items, we will face new questions like if a specific method belongs in the battery class or in the electric car class, or how many classes should make up the car class. These questions reflect a higher mode of thinking, called **object-oriented thinking**, not concerned with code syntax but with how to best model the real world using code. There are multiple valid approaches to modelling the same system, but not all of them are equally efficient; experience and personal taste will be helpful in these cases. 

## 9.4 - Importing classes
Classes can be imported from python modules the same way as functions. The module name should be the name of the python file without the `.py` extension. If the file's name doesn't begin with a letter, the Python interpreter might not let you import. You can store as many classes as you like in a single module, but it's best to keep the modules conceptually coherent (e.g. using the car module to store car-related classes).

```
from car import Car

my_car = Car("volkswagen", "golf")
my_car.describe_car()
```

You can also import an entire module, to use which elements you'll need to use dot notation, same as with functions.

```
import car

my_car = car.Car("renault", "clio")
my_battery = car.Battery(85)
```

There's a discouraged way of importing an entire module, which is using `from car import *`. This can create naming conflicts and confusion, but some programs do use it.

## 9.5 - The Python Standard Library
The **Python Standard Library** is a set of modules that comes with every Python installation. There are many modules with object types and functions that will be perfect for handling many common programming needs, so knowing to some extent the library is a good idea, if you want keep your code simple and efficient.

A data type example that the standard library provides is the `OrderedDict` class. It works just like a dictionary, storing key and value pairs, but with the added feature that, like a list, it retains the order in which its elements were added.

```
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title() + ".")
```

## 9.6 - Styling classes
Class names should be written in CamelCaps. Instances and modules should be written in snake_caps. Each module and class should have a docstring explaining with they can be used for.

You can use blank lines to organize code, but don’t use them excessively. Within a class you can use one blank line between methods, and within a module you can use two blank lines to separate classes.

If you need to import a module from the standard library and a module that you wrote, place the import statement for the standard library module first. Then add a blank line and the import statement for the module you wrote. In programs with multiple import statements, this convention makes it easier to see where the different modules used in the program come from.

