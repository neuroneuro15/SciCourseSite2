title: Plotting with Matplotlib
icon: fa-bar-chart
summary: Matplotlib is a key Python package for performing data visualization.  We'll learn to build and customize graphs to make publication-quality figures.

# Lesson Goals

  - Understand the purpose of the Matplotlib and how to import it
  - Know how to build line plots, scatter plots, and histograms
  - Understand Matplotlib's hierarchical object model
  - Know how to label your plots
  - Know how to build subplots
  - Know how to explore objects and learn what **methods** are available for customizing it.

# Sample Code

Import Matplotlib:

    import matplotlib.pyplot as plt

Line plot:

    x = np.linspace(0, np.pi * 4, 300)
    sinx = np.sin(x)
    plt.plot(x, sinx)

Labeled Scatter plot:

    plt.scatter(x, sinx)
    plt.xlabel('x')
    plt.ylabel('Sin(x)')
    plt.title('The Sine of X')

Histogram:

    rand_nums = np.random.randn(1000)
    plt.hist(rand_nums)

Subplots:

    fig, axes = plt.subplots(ncols=2)
    ax1 = axes[0]
    ax1.plot(x, sinx)
    ax1.plot(x, np.cos(x))
    ax1.title('The Sine of X')

    axes[1].hist(rand_nums)

To save the figure:

    fig.savefig('my_figure1.png')


