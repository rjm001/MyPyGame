# OOP Tenets and Overarching Notes

- lists and dictionaries are 'containers'
- any `.py` file in a project folder is called a "module".
    - e/g/. for BalloonGame, we have
        - a module of constants
        - a module of Balloon classes
        - a module of the BalloonMgr class

## OOP Tenets

1. (E) encapsulation: hiding the details and keeping everything in one place (chapter 8)
2. (P) polymorphism: how multiple classes can have methods with the same names
    - like in math defining multiplication of scalars, multiplication of scalar and vectors, multiplication of vectors, multiplication of scalar and matrices, etc. (chapter 9)
3. (I) inheritance: building on code that already exists (chapter 10)

PIE

## Note:

- Constants in Python, by convention are written in all capital letters
- e.g. `SPACE_SHIP_IMAGE`, `N_BALLOONS`, etc.

## Reference Counts

```python
import sys
sys.getrefcount(<object>)
```

### ref counts increments
1. additional variable is assigned to refer to the same object
2. when an object is passed into a function (so a local paprameter variable is set)
3. when an object is put into a 'container' like a list or dictionary

### ref count decrements

1. when a variable that refers to an object is reassigned
    - including to `None`
2. when a local variable that refers to an object goes out of scope (so deleted)
3. when removed from a container (e.g., `myList.pop()`)
4. when you use the del statement to explicitly delete a variable that refers to an object
5. if the reference count of the object's container goes to zero. (e.g., `del myList`)

## Magic Methods (aka Dunder Methods)


- `__init__()` is a 'dunder init'
- `__del__()` is dunder del
    - when you call this, it *doesn't overwrite* garbage collection, but rather *immediately precedes* garbage collection.

```python

class Student():
    def __init__(self, name):
        self.name = name
        print('Creating Student object', self.name)
    #
    def __del__self():
        print(f'In the __del__ method for student: {self.name}')

class Teacher():
    def __init__(self):
        print('Creating the Teacher object')
        self.oStudent1 = Student('Joe')
        self.oStudent2 = Student('Sue')
        self.oStudent3 = Student('Chris')
    #
    def __del__(self):
        print(f'In the __del__ method for Teacher')

oTeacher = Teacher()
del oTeacher #deletes the students too! but, actually, might not occur right away! if doing this interactively!
try:
    del oStudent2
except:
    print('Already deleted')

# actually, the above didn't call __del__ for me either! I wouldn't rely ono the __del__ method too much!

```


## Memory Slots

- 

## Abstract Methods

## Class Variables

Two reasons to use
1. for constants that may be slow to instantiate or take up a lot of memory and don't want to load for each instantiated object. e.g., a large data class or a picture
```python
class SpaceShip():
    SPACE_SHIP_IMAGE = pygame.image.load('images/ship.png')
    def __init__(self, window,...):
        self.image = pygwidgets.Image(window, (0,0),SpaceShip.SPACE_SHIP_IMAGE)
```
2. for counting class variables

```python
class Sample():
    nObjects = 0

```

