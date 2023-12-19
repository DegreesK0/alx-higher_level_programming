### Object-Oriented Programming (OOP):

Object-Oriented Programming (OOP) is a programming paradigm that organizes data and behavior into reusable and self-contained objects. These objects are instances of classes, which act as blueprints for creating objects. OOP promotes the concept of "objects," which can encapsulate data in the form of attributes (variables) and behavior in the form of methods (functions). The key principles of OOP include:
1. encapsulation
2. inheritance
3. polymorphism

### “First-Class Everything”:

In Python, the phrase "first-class everything" means that everything in Python, including functions, classes, and data types, is treated as an object. This means you can manipulate functions and classes in the same way you manipulate other objects, like integers or strings.

### What is a Class?

- A class is a blueprint or a template for creating objects in OOP.
- It defines the attributes (data) and methods (functions) that the objects of the class will have.
- Classes encapsulate data for the object and methods to operate on that data.
- Classes are defined using the `class` keyword in Python.

Example of defining a class:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")
```

### What is an Object and an Instance?

- **Object:**
  - An object is a concrete instance of a class created using the class constructor.
  - Objects represent real-world entities and have characteristics (attributes) and behaviors (methods).

  Example of creating an object (instance) of the `Car` class:

  ```python
  my_car = Car("Toyota", "Corolla")
  ```

- **Instance:**
  - An instance is a specific realization of any object.
  - It is a single, unique unit of a class created during the execution of a program.

  Example of using the `my_car` instance:

  ```python
  my_car.display_info()  # Output: Toyota Corolla
  ```

### Difference Between a Class and an Object (or Instance):

- **Class:**
  - A class is a blueprint or a template for creating objects.
  - It defines the attributes and methods that the objects of the class will have.
  - It is a logical entity and does not occupy memory space.

- **Object (or Instance):**
  - An object is a concrete instantiation of a class.
  - It represents a real-world entity and occupies memory space.
  - Objects can access class attributes and methods, and they can have unique values for their attributes.

### What is an Attribute?

- An attribute in the context of object-oriented programming refers to a property or characteristic of an object.
- Attributes are data members that hold data associated with a class and its objects.
- They represent the state or quality of the object.

Example of a class with attributes:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # brand is an attribute
        self.model = model  # model is an attribute
```

### Public, Protected, and Private Attributes:

- **Public Attributes:**
  - Attributes defined in a class are public by default in Python.
  - Public attributes can be accessed from outside the class.
  - Example: `self.brand`

- **Protected Attributes:**
  - Attributes can be protected by adding a single underscore prefix before their names.
  - Protected attributes should not be accessed from outside the class, but it is not enforced by the Python interpreter.
  - Example: `self._protected_attribute`

- **Private Attributes:**
  - Attributes can be made private by adding a double underscore prefix before their names.
  - Private attributes cannot be accessed directly from outside the class.
  - Example: `self.__private_attribute`

### What is `self`?

- `self` is a convention in Python that represents the instance of the class.
- It refers to the object being created or operated upon within a method.
- It is the first parameter of any instance method in a class and allows you to access the attributes and methods of the object.

Example:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")
```

In this example, `self.brand` and `self.model` refer to the attributes of the specific instance of the `Car` class.

### What is a Method?

- A method in Python is a function associated with a class.
- Methods define the behavior of the objects of the class.
- They can operate on class attributes and perform actions related to the class.

Example of a class with a method:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")
```

In this example, `display_info()` is a method of the `Car` class.

### The Special `__init__` Method:

- `__init__` is a special method in Python classes.
- It is called a constructor method and is automatically invoked when a new object of the class is created.
- It initializes the object's attributes.
- `self` is used within `__init__` to refer to the instance being created.

Example:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Initializes the brand attribute
        self.model = model  # Initializes the model attribute

    def display_info(self):
        print(f"{self.brand} {self.model}")

# Creating an instance of Car and calling the display_info method
my_car = Car("Toyota", "Corolla")
my_car.display_info()  # Output: Toyota Corolla
```

In this example, `__init__` initializes the `brand` and `model` attributes when a `Car` object is created.

### Data Abstraction, Data Encapsulation, and Information Hiding:

- **Data Abstraction:**
  - Data abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object.
  - It provides a clear separation between what an object does and how it achieves its functionality.
  - It focuses on the essentials and hides the complexities from the user.

- **Data Encapsulation:**
  - Data encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit known as a class.
  - Encapsulation helps in data abstraction by restricting access to certain attributes or methods, allowing the internal representation of an object to be hidden from the outside world.

- **Information Hiding:**
  - Information hiding is a principle that states that the inner workings of a class should be hidden from the outside world.
  - It allows the object to maintain its integrity by preventing external code from directly accessing its internal state.
  - Information hiding is achieved through encapsulation, where data members are kept private and accessed only through public methods (getters and setters).

### What is a Property?

- A property in Python is a special kind of attribute that allows for controlled access to an object's attributes.
- Properties are defined using the `@property` decorator in Python.
- They provide a way to implement getters, setters, and deleters for class attributes.

Example of a property:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

# Usage
circle = Circle(5)
print(circle.radius)  # Output: 5
circle.radius = 10
print(circle.radius)  # Output: 10
```

### Difference Between an Attribute and a Property in Python:

- **Attribute:**
  - An attribute is a variable that belongs to a class or object.
  - It holds data associated with the class or object.
  - Attributes can be accessed directly, and there is no restriction on their values.

- **Property:**
  - A property is a special kind of attribute that provides controlled access to class data.
  - It uses getter and setter methods to access and modify the attribute's value.
  - Properties allow for validation and encapsulation, ensuring that data is accessed and modified in a controlled manner.

### Pythonic Way to Write Getters and Setters in Python:

- In Python, the `@property` decorator is used to define getter methods, and `@<attribute>.setter` is used to define setter methods.
- Pythonic code emphasizes simplicity and readability.

Example of Pythonic getters and setters:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

# Usage
circle = Circle(5)
print(circle.radius)  # Output: 5
circle.radius = 10
print(circle.radius)  # Output: 10
```

In this example, the `radius` property provides controlled access to the `_radius` attribute, allowing validation of the input value. This follows the Pythonic way of defining getters and setters.

### Dynamically Creating New Attributes for Existing Instances:

In Python, you can dynamically create new attributes for existing instances of a class by simply assigning a value to a new attribute name. For example:

```python
class MyClass:
    pass

obj = MyClass()
obj.new_attribute = 42  # Dynamically creating a new attribute named "new_attribute"
print(obj.new_attribute)  # Output: 42
```

### Binding Attributes to Objects and Classes:

- **Object Attributes:**
  - Attributes bound to objects are specific to each instance of the class.
  - They are defined by assigning values inside methods or directly outside the class scope for a specific object.

- **Class Attributes:**
  - Attributes bound to classes are shared by all instances of the class.
  - They are defined directly inside the class but outside any methods.

Example:

```python
class MyClass:
    class_attribute = 10  # Class attribute

    def __init__(self, value):
        self.instance_attribute = value  # Instance attribute

obj1 = MyClass(5)
obj2 = MyClass(7)

print(obj1.instance_attribute)  # Output: 5
print(obj2.instance_attribute)  # Output: 7
print(obj1.class_attribute)     # Output: 10
print(obj2.class_attribute)     # Output: 10
```

### `__dict__` of a Class and Instance:

- `__dict__` is a dictionary containing the attributes of an object or class.
- For an instance, it stores instance attributes and their values.
- For a class, it stores class attributes and methods.

Example:

```python
class MyClass:
    class_attribute = 10

obj = MyClass()
print(obj.__dict__)  # Output: {'instance_attribute': 5}
print(MyClass.__dict__)  # Output: {'class_attribute': 10, ...}
```

### Finding Attributes of an Object or Class:

When you try to access an attribute of an object, Python searches for the attribute in the following order:

1. **Instance Attributes:** Attributes specific to the instance.
2. **Class Attributes:** Attributes shared by all instances of the class.
3. **Attributes from Parent Classes:** If the class inherits from other classes, Python searches the parent classes for the attribute.

### Using `getattr` Function:

The `getattr(object, attribute_name, default)` function is used to get the value of an attribute of an object. If the attribute doesn't exist, it returns the specified default value.

Example:

```python
class MyClass:
    class_attribute = 10

obj = MyClass()
print(getattr(obj, 'class_attribute', 'Attribute not found'))  # Output: 10
print(getattr(obj, 'non_existent_attribute', 'Attribute not found'))  # Output: Attribute not found
```

In the above example, `getattr` tries to get the value of `'class_attribute'` from `obj`. If it doesn't exist, the default value `'Attribute not found'` is returned.
