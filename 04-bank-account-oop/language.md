# Note on OOP Language

0. Style: classes start with capital letters and are camelcase after. Methods and variables are camel case starting with a lower case.
1. the variables that are self.variables are "instance variables". They have "object" scope.
2. the variables that are given to methods that aren't instance variables are "local" variables. They disappear as soon as the method call is done.
3. What's the primary difference between a method and a function in Python?
    a. A method is defined inside a class
    b. A method is applied to an object by the dot notation object.method(local_variables)
    c. Python translates this into method(object, local_variables)
    d. That's why the definition of the method, the first argument has to account for the fact that the object itself will be passed in as it
        - Note that *self* is **not** a **keyword**. Rather *self* is a **convention**. By convention, we call 'self' the first argument passed to (all) methods. But, whatever word you put there, it will be the name of the object that python receives!
4. variables defined outside of objects and in main are *global* variables
5. a common technique in python programming (and OOP in general) is to have an Object Manager Object as a global variable that manages all the other objects. Perhaps even have hierarchies of this!
    - question: how deep should these hierarchies run?
        - should you have objects that manage objects that manage objects?
            - does your system have subsystems that need to keep track of themselves?
                - if your system has subsystems, then you probably need subsystem OMOs. Otherwise, no. The bank is complete with accounts, etc.
                - A website... well, if you have a payment system on your website, you might need a whole subsystem for that payment method too.
    - note: having an object that manages/contains other objects is called 'composition.' It sounds straightforward when thinking about, for example, a car object having a steeringwheel object, but it is much more profound when you think about a system object managing the interactions of the system. A car is a system, but feels more integrated than a platform with (perhaps adversarial) interactions within the platform. Something to think about if I were designing amazon, how would I do it? What kind of objects does Amazon need? Advertisement objects. Users, goods, 3rd party sellers. 3rd party sellers should have 3rd party goods, which are perhaps a subclass of your own goods? Pretty interesting to think about!
6. Exception handling
    - Three things can happen with this 'try' statement
    a. it succeeds! then the program continues past the except statement
    b. it fails and the except is the correct error!
        - Then the except block is executed and the program continues
        - note that ValueError is a standard python library exception. Since int() is a standard python library function, it makes sense that its there. See [here for more](https://docs.python.org/3/library/exceptions.html).
    c. it fails and the except block does not correct the error
        - then python will step out of the current function or method, and continue up the hierarchy of functions and methods until 1 or 2 happens in an upstream function or method *or* 1 or 2 never happens, the program quits and python displays the error!
        - **it's a pretty useful feature of python that this keeps moving up the levels looking for the right handling, passing it to the right level of authority. Imagine if this could happen with real life.**

```python
age = input('Please enter your age')
try:
    age = int(age)
except ValueError:
    print('Sorry, that was not a valid number')
```


7. Raising Exceptions
    a. Raise a *standard* exception
        - `raise <StandardExceptionName>(<Any message you want to attach to it>)`
    b. Raise a *generic* exception (not best practices!!!)
        - `raise Exception('<The message displayed with your generic exception>')`
        - question: what catches this generic exception:? Just `except Exception:`
            - You can also abbreviate the Exception, SQL style:
                - `except Exception as e:`
    c. Define your own exception(s)
        - Best way! Example below and in the program
        - Your own exception should inherit from the exception class

```python
class <CustomExceptionName>(Exception):
    pass
```