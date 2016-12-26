title: Pandas DataFrames
icon: fa-table
summary: Label and organize your N-Dimensional Data and increase your code readability with Pandas DataFrames

# Lesson Goals

  - Understand the purpose of the Pandas package and how to import it.
  - Know how to build a DataFrame and Series
  - Know how to index and select from DataFrames
  - Understand the Split-Apply-Combine workflow:
      - Know how to split data with the **DataFrame.groupby()** method
      - Know how to iterate over GroupBy groups.
      - Know how to apply aggregation functions to each group.
  - Be Familiar with the concent of "pivoting" tables with the **pivot()**, **melt()**, **stack()**, and **unstack()** functions.

# Sample Code

Import Pandas

    import pandas as pd

DataFrame creation:

    aa = {'X': [1, 2, 3], 'Y': [10, 20, 30]}
    df = pd.DataFrame(aa)

    bb = [[1, 10], [2, 20], [3, 30]]
    df2 = pd.DataFrame(bb, columns=['X', 'Y'])

Index a DataFrame:

    df['X']
    df.loc[1]
    df.iloc[2]
    df.ix[1:, 'Y']

GroupBy:

    groups = df.groupby(df.X < 2)
    groups.Y.mean()

    df['Condition'] = ['Mutant', 'Control', 'Mutant', 'Control']
    conditions = df.groupby('Condition')
    conditions.mean()

    for cond, data in conditions:
        print("Condition {} has Y mean = {}".format(cond, data.Y)

    Y_stats = conditions.Y.agg({'Mean': np.mean, 'STD': np.std})

