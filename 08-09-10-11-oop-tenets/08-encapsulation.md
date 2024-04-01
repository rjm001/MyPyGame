# 08 Encapsulation

### Encapsulation with Functions

- You don't care how the function works. Just what it does. (As long as it correctly works! And works with the write speed)

### Encapsulation with Objects

*client*: any sofware that creates an object from a class and makes calls to the methods of that object.
    - within a class, you need to worry about how the different methods of a class share the instance variables.
    - consider the effieincy of your algorithms
    - think about what the interface should look like.
- as a *client programmer*, you need to know the **interface** of the class. 
    - what the class methods do
    - what arguments should be passed in
    - what data is passed back from each method
    - encapsulation from:
        - hiding method implementation dtails and instance variables
        - providing all the functionality a client needs from an object through tis interface

### Encapsulation with Python

- Python allows for direct access to instance variables using simple dot syntax!
- Client code can legally access an instance variable of an object by name using the syntax `<object>.<instanceVariableName>`. This isn't true with all languages!
    - a strict interpretation of encapsulation says *this isn't allowed!*
- Guido Van Rossum famously said:
    - "We're all adults here" meaning programmers should know what they are doing and the risks involved when they attempt to access instance variables directly
        - **Namely, the risk is, the instance variable names are a matter of *how* the methods work. So, a method may change the instance variable name and break the client code. But this is the client code writer's fault!**
            - there are many valid reasons for a developer of a class to want to change a name too!
                - the name doesn't describe the data it represents clearly enough (anymore)
                - the variable is a Boolean and they want to swap True False for representativbe names (e.g., open and closed or allowed and disallowed)
                - there was a spelling or capitalization mistake in the original name
                - the variable was originally a Boolean, but they later realized they need more than two values!
        - another risk updating policy:
            - it might be that how the interest rate is calculated changes, for example. If you just access the interest rate instance variable and not the correct method, you might not get the updated value!
        - another risk: (in)validating program data
            - client code can too easily set an instance variable to an invalid value!
                - it`s better to use a designated method with checks to set instance variable than just give the client code free access!
                - example where a club can only have 5 members, but the limitation is implemented through the setting method, rather than hard coded into the data structure. A client accessing the instance variable could override the cap of 5 people, carelessly doing unknown damage to the software!

#### Strict Interpretation with Getters and Setters

- This is the way client software is allowed to access instance variables with a strict interpretation of encapsulation.
- Alternative words that mean the same thing
    - `getter == accessor`
    - `setter == mutator`

### When is direct access safe?

1. it is absolutely clear what the instance variable means
2. little or no validation of the data is needed
3. no chance the name will change

e.g., pandas.shape and pandas.columns

## Making Instance Variables More Private

### 1. implicitly private

- add a leading underscore
- this is a convention; no enforcement


```python
self._name
self._socialSecurityNumber
self._dontTouchThis


def _internalMethod(self):
    pass

def _dontCallMeFromClientSoftware(self):
    pass

```
### 2. Explicitly Private

- putting a double underscore disallows client softrware from directly accessing your date

```python
#python3
class PrivatePerson():
    def __init__(self, name, privateData):
        self.name = name
        self.__privateData = privateData
    #
    def getName(self):
        return self.name

oPrivatePerson = PrivatePerson('Tom', 'SSN=***')
oPrivatePerson.getName()
oPrivatePerson.__privateData #get an error saying it DNE

oPrivatePerson._PrivatePerson__privateData #you can access it if you know how it's been mangled!!
```


This happens because python provides "name mangling" behind the scene.
It changes the name from `__<name>` to `_<className>__<name>` always!! So it's more just a deterrant.

## Decorators and `@property`

- Decorators are methods (or functions) that take other methods (or functions) as inputs and extend the way they work
- There is a set of built-in decorators that provide a compromise between direct access and using getters and setters

**property:** an attribute of a class that appears to client code to be an instance variable. But, instead causes a method to be called when it is accessed. So, could be a getter or a setter!


```python

class Example():
    def __init__(self, startingValue):
        self._x = startingValue
    #
    @property #note it's **not** followed by a colon
    def x(self): # the decorated getter method
        return self._x
    #
    @x.setter #this is an optional pairing with @property getter.
    def x(self, value): # this is hte decorated setter method
        self._x = value
    

oExample = Example(10)
print(oExample.x) #note, we are using the x method! the x variable is _x.
oExample.x = 20 #nice. Uses the setter? I can debug this and see where it goes!
oExample.x
```
### A very cool example!

```python
class Student():
    #
    def __init__(self, name, startingGrade=0):
        self.__name = name
        self.grade = startingGrade #note, this **isn't** setting an instance variable. This is setting the **property** grade. Internally, python translates this to a call to the setter method, which sets the private variable self.__grade! Very interesting. And confusing to the unitiated, since the property stuff is happening in an obtuse way that looks like variable assignment to the unitiatied. Obviously, python needs to know what the whole class does and can't just execute the constructor here without seeing the methods and properties first.
    #
    @property
    def grade(self):
        return self.__grade
    #
    @grade.setter
    def grade(self, newGrade):
        try:
            newGrade = int(newGrade)
        except (TypeError, ValueError) as e:
            raise type(e)(f'New Grade: {str(newGrade)} is an invalid type')
        if (newGrade < 0) or (newGrade > 100):
            raise ValueError(f'New grade: {str(newGrade)}, must be between 0 and 100') #equivalent to f'New grade: "{(newGrade)}", must be between 0 and 100' ?
        self.__grade = newGrade
        

oStudent1 = Student('Joe Schmoe')
oStudent2 = Student('Jane Smith')
print(oStudent1.grade)
print(oStudent2.grade)
print()

oStudent1.grade = 85 #setting the property grade, not the instance variable. Through the @property.
oStudent2.grade = 92

print(oStudent1.grade)
print(oStudent2.grade)

oStudent2.grade = 'blah' #can see the input validation/sanitization is working!
print(oStudent2.grade)
oStudent2.grade = 120 

```

