title: NumPy (Numerical Python) Arrays
day: 1
num: 4
icon: fa-list-ol
summary: NumPy is the workhorse of the scientific Python stack.  We'll use arrays to speed up analysis.


# Lesson Goals

  - Understand what the NumPy package is used for and how to **import** it.
  - Understand what an **array** is.
  - Know how to build arrays from core collections objects.
  - Know the main math functions in numpy
  - Understand the idea of **vectorization**
  - Know how to index data using a boolean **mask**

# Sample Code

Import NumPy:

    import numpy as np

*Note*: If you see "ImportError", then it means NumPy has not been installed.

## Working with Arrays

    a = [1, 2, 3, 4]
    a_array = np.array(a)

### Quick-building arrays

    one_thru_ten = np.arange(1, 11)
    one_thru_ten_five_vals = np.linspace(1, 10, 5)
    ten_ones = np.ones(10
    ten_zeros = np.zeros(10)

## Using NumPy functions and operators

    x = np.arange(5)
    x_squared = x ** 2
    sin_x = np.sin(x)
    sqrt_x = np.sqrt(x)

## Indexing Arrays

    x = np.arange(10)
    x0 = x[0]

    mask = x > 4
    big_x = x[mask]

