title: Data Collection Objects and Iteration
icon: fa-refresh
summary: Iteration is the key to saving you time and improving your reliability. Here we'll cover strings, lists, tuples, and for-loops

# Lesson Goals

  - Understand the difference between ordered and unordered collections
  - Know the effects of addition and multiplication on ordered collections.
  - Know how to use the square brackets [] to **index** and **slice** values in a collection.
  - Know how to assign new values to an existing collection
    - Understand the difference between mutable and immutable collections
  - Know how to make a **for** loop.
    - Understand what iteration is, and the difference between c-style loops and iteration.
    - Know how to use the zip() and enumerate() functions to build more complex for loops.
    - Recognize list comprehensions.

# Sample Code

## Build strings, tuples, lists, sets, and dicts

### str

    s1 = 'Hello'
    s2 = "Hello"
    s3 = """Hello"""
    s4 = "Hello, " + "World!"
    hello = s4[:5]

### tuple

    tup1 = (10, 20, 30)
    tup2 = tuple((10, 20, 30))
    tup3 = (10, 20) + (30,)

### list

    list1 = [10, 20, 30]
    list2 = list((10, 20, 30))
    twenty = list2[2]
    list[0] = 100

### dict

    dict1 = {'a': 10, 'b': 20, 'c': 30}
    dict2 = dict(a=10, b=20, c=30)
    dict3 = dict([('a', 10), ('b', 20), ('c', 30)])
    ten = dict3['a']
    dict3['a'] = 100

## For loop

    data = [2, 4, 6, 8]
    for el in data:
        print(el)


### Build a new list

    data = [2, 4, 6, 8]
    data_squared = []
    for el in data:
        el_squared = el ** 2
        data_squared.append(el_squared)
    print(data_squared)

### Enumerate

    data = [2, 4, 6, 8]
    for idx, el in enumerate(data):
        print("Value {} is {}".format(idx, el))


## List comprehension

    data = [2, 4, 6, 8]
    x_squared = [x ** 2 for x in data]

# Quote

