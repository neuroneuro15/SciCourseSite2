title: High-Level Data Visualization
num: 8
icon: fa-area-chart
summary: Building a nice chart can be complicated! We'll learn how to create beautiful Matplotlib charts more quickly with Pandas and Seaborn.


# Lesson Goals

  - Understand the pros and cons of plotting with the Pandas and Seaborn
  - Know how to use **both** Pandas and Seaborn to plot categorical and continuous data
  - Know how to customize high-level plotting with Matplotlib
  - Know how to change the plot
  - Have a discussion on the good practices for data visualization


# Sample Code

Import Seaborn and set the style

    import matplotlib.pyplot as plt
    from matplotlib import style
    import seaborn as sns

    print(matplotlib.style.available)
    >> ['ggplot', 'classic', seaborn-muted']
    matplotlib.style.use('ggplot')

Get some sample data, the *Iris* dataset

    import pandas.rpy.common as rcom
    df = rcom.load_data('iris')

Bar Plot with Pandas

    df.plot.bar(x="Species", y="Petal.Length")

Bar Plot with Seaborn

    sns.barplot(x="Species", y="Petal.Length", data=df)

Subplots using a mix of pandas, seaborn, and matplotlib

    fig, (ax1, ax2) = plt.subplots(ncols=2)
    fig.suptitle('Petal widths and lengths for different species')

    df.plot.bar(x="Species", y="Petal.Length", ax=ax1)
    ax1.title('Petals are different lengths between species!')

    sns.violinplot(x="Species, y="Petal.Width", ax=ax2)
    ax2.title('Species have different widths!)


### Scatter plots:

Let's make a plot of the petal widths vs lengths, colored by species.  First, using matplotlib:

    fig, ax = plt.subplots()
    for species, data in df.groupby('Species')
        ax.scatter(data['Petal.Width'], data['Petal.Length'], label=species)
    ax.legend()

Using Pandas:

    fig, ax = plt.subplots()
    df.groupby('Species').plot.scatter(x='Petal.Width', y='Petal.Length', ax=ax)

Using Seaborn:

    sns.lmplot(x='Petal.Width', y='Petal.Length', hue='Species', data=df)

Using an even higher-level Seaborn plot, which adds 1D histograms;

    sns.jointplot(x='Petal.Width', y='Petal.Length', hue='Species', data=df)