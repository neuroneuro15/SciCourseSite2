title: Matrices and Image Analysis
day: 1
num: 6
icon: fa-th
summary: Arrays can be two-dimensional, too!  We'll cover 2D matrix manipulation and 3D Image Analysis with scikit-image!
exercises:
  - testfile.csv

# Lesson Goals

  - Know how to Build, Index, and Slice 2-D and 3D arrays
  - Understand the concept of data dimensionality
    - Know how to check how many dimensions an array has
  - Know how to visualize a matrix as an image
  - Know how to use the **scikit-image** package to load an image as an array
  - Understand how images are encoded as values, and the limitation of different encodings
  - Understand the pros and cons of different **colormaps** for visualizing data.


# Sample Code

build a 2 x 4 array:

    aa = [[1, 2, 3, 4], [5, 6, 7, 8]]
    aa_array = np.array(aa)
    aa_array.shape
    >> (2, 4)

get the value in the first row, third column:

    aa[0, 2]
