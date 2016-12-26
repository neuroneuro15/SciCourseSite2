title: Building Your Library
num: 10
icon: fa-briefcase
summary: Increase your productivity and effectiveness by writing reusable code as functions and modules.


# Lesson Goals

  - Understand the DRY 9"Don't Repeat Yourself") principle and why it is important.
  - Know how to write your own functions
  - Understand the parts of a function, including the **arguments**, **keyword arguments**, **output**, and the **docstring**.
  - Understand the concepts of **scope** and **namespaces**, and how it affects your code
  - Know how to write your own Python modules and use them your scripts.
  - Understand the purpose of the Python path and how to change it.


# Sample Code

A function that adds two numbers, "x" and "y", and outputs ("returns") the result:

    def add(x, y):
        return x + y

A for loop inside a function that sums up each element in a list:

    def add(my_list):
        total = 0
        for el in my_list:
            total += el
        return total

Adding some help text to my add function in a **docstring**:

    def add(x, y):
        """Returns the sum of x and y."""
        return x + y

Importing my add function from my self-made file, which I will call for this example *mytools.py*:

    import mytools

    mytools.add(3, 5)
    >> 8
