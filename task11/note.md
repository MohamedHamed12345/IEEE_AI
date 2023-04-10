 **Introduction**: Pandas is a Python library for data manipulation and analysis. 
 It provides data structures for efficiently storing and manipulating large datasets.
    
-   **Importing Pandas**: To use Pandas, we first need to import it using the `import` statement.
    
    Example:
    
    ```
    pythonimport pandas as pd
    
    ```
    
-   **Creating a DataFrame**: A DataFrame is a two-dimensional table of data. We can create a DataFrame by passing a dictionary of lists or arrays to the `pd.DataFrame()` function.
    
    Example:
    
    ```
    pythondata = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
    df = pd.DataFrame(data)
    print(df)
    
    ```
    
    Output:
    
    ```
    markdown    name  age
    0   Alice   25
    1     Bob   30
    2 Charlie   35
    
    ```
    
-   **Reading Data from a CSV File**: We can read data from a CSV file into a DataFrame using the `pd.read_csv()` function.
    
    Example:
    
    ```
    pythondf = pd.read_csv('data.csv')
    print(df)
    
    ```
    
-   **Reading Data from an Excel File**: We can read data from an Excel file into a DataFrame using the `pd.read_excel()` function.
    
    Example:
    
    ```
    pythondf = pd.read_excel('data.xlsx')
    print(df)
    
    ```
    
-   **Viewing Data**: We can view the first few rows of a DataFrame using the `df.head()` method.
    
    Example:
    
-   **Filtering Data**: We can filter rows of a DataFrame using boolean indexing.
    
    Example:
    
    ```
    pythondf_filtered = df[df['age'] %3E 25]
    print(df_filtered)
    
    ```
    
-   **Grouping Data**: We can group rows of a DataFrame by one or more columns using the `df.groupby()` method.
    
    Example:
    
    ```
    pythondf_grouped = df.groupby('name').sum()
    print(df_grouped)
    
    ```
    
-   **Aggregating Data**: We can aggregate data in a DataFrame using functions like `sum()`, `mean()`, and `count()`.
    
    Example:
    
    ```
    pythondf_agg = df.groupby('name').agg({'age': 'mean', 'income': 'sum'})
    print(df_agg)
    
    ```
    
-   **Merging Data**: We can merge two DataFrames on a common column using the `pd.merge()` function.
    
    Example:
    
    ```
    pythondf1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
    df2 = pd.DataFrame({'name': ['Alice', 'Charlie'], 'income': [50000, 60000]})
    df_merged = pd.merge(df1, df2, on='name')
    print(df_merged)
    
    ```
    
-   **Joining Data**: We can join two DataFrames on their index using the `pd.join()` function.
    
    Example:
    
    ```
    pythondf1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]}, index=['A', 'B'])
    df2 = pd.DataFrame({'income': [50000, 60000]}, index=['A', 'C'])
    df_joined = df1.join(df2)
    print(df_joined)
    
    ```
    
-   **Pivoting Data**: We can pivot a DataFrame using the \`df.pivot>)](<-   **Introduction**: Pandas is a Python library for data manipulation and analysis. It provides data structures for efficiently storing and manipulating large datasets.
    
-   **Importing Pandas**: To use Pandas, we first need to import it using the `import` statement.
    
    Example:
    
    ```
    pythonimport pandas as pd
    
    ```
    
-   **Creating a DataFrame**: A DataFrame is a two-dimensional table of data. We can create a DataFrame by passing a dictionary of lists or arrays to the `pd.DataFrame()` function.
    
    Example:
    
    ```
    pythondata = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
    df = pd.DataFrame(data)
    print(df)
    
    ```
    
    Output:
    
    ```
    markdown    name  age
    0   Alice   25
    1     Bob   30
    2 Charlie   35
    
    ```
    
-   **Reading Data from a CSV File**: We can read data from a CSV file into a DataFrame using the `pd.read_csv()` function.
    
    Example:
    
    ```
    pythondf = pd.read_csv('data.csv')
    print(df)
    
    ```
    
-   **Reading Data from an Excel File**: We can read data from an Excel file into a DataFrame using the `pd.read_excel()` function.
    
    Example:
    
    ```
    pythondf = pd.read_excel('data.xlsx')
    print(df)
    
    ```
    
-   **Viewing Data**: We can view the first few rows of a DataFrame using the `df.head()` method.
    
    Example:
    
-   **Filtering Data**: We can filter rows of a DataFrame using boolean indexing.
    
    Example:
    
    ```
    pythondf_filtered = df[df['age'] %3E 25]
    print(df_filtered)
    
    ```
    
-   **Grouping Data**: We can group rows of a DataFrame by one or more columns using the `df.groupby()` method.
    
    Example:
    
    ```
    pythondf_grouped = df.groupby('name').sum()
    print(df_grouped)
    
    ```
    
-   **Aggregating Data**: We can aggregate data in a DataFrame using functions like `sum()`, `mean()`, and `count()`.
    
    Example:
    
    ```
    pythondf_agg = df.groupby('name').agg({'age': 'mean', 'income': 'sum'})
    print(df_agg)
    
    ```
    
-   **Merging Data**: We can merge two DataFrames on a common column using the `pd.merge()` function.
    
    Example:
    
    ```
    pythondf1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
    df2 = pd.DataFrame({'name': ['Alice', 'Charlie'], 'income': [50000, 60000]})
    df_merged = pd.merge(df1, df2, on='name')
    print(df_merged)
    
    ```
    
-   **Joining Data**: We can join two DataFrames on their index using the `pd.join()` function.
    
    Example:
    
    ```
    pythondf1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]}, index=['A', 'B'])
    df2 = pd.DataFrame({'income': [50000, 60000]}, index=['A', 'C'])
    df_joined = df1.join(df2)
    print(df_joined)
    
    ```
    
-   **Pivoting Data**: We can pivot a DataFrame using the \`df.pivot>)](<-   **Introduction**: Pandas is a Python library for data manipulation and analysis. It provides data structures for efficiently storing and manipulating large datasets.
    
-   **Importing Pandas**: To use Pandas, we first need to import it using the `import` statement.
    
    Example:
    
    ```
    pythonimport pandas as pd
    
    ```
    
-   **Creating a DataFrame**: A DataFrame is a two-dimensional table of data. We can create a DataFrame by passing a dictionary of lists or arrays to the `pd.DataFrame()` function.
    
    Example:
    
    ```
    pythondata = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
    df = pd.DataFrame(data)
    print(df)
    
    ```
    
    Output:
    
    ```
    markdown    name  age
    0   Alice   25
    1     Bob   30
    2 Charlie   35
    
    ```
    
-   **Reading Data from a CSV File**: We can read data from a CSV file into a DataFrame using the `pd.read_csv()` function.
    
    Example:
    
    ```
    pythondf = pd.read_csv('data.csv')
    print(df)
    
    ```
    
-   **Reading Data from an Excel File**: We can read data from an Excel file into a DataFrame using the `pd.read_excel()` function.
    
    Example:
    
    ```
    pythondf = pd.read_excel('data.xlsx')
    print(df)
    
    ```
    
-   **Viewing Data**: We can view the first few rows of a DataFrame using the `df.head()` method.
    
    Example:
    
-   **Filtering Data**: We can filter rows of a DataFrame using boolean indexing.
    
    Example:
    
    ```
    pythondf_filtered = df[df['age'] %3E 25]
    print(df_filtered)
    
    ```
    
-   **Grouping Data**: We can group rows of a DataFrame by one or more columns using the `df.groupby()` method.
    
    Example:
    
    ```
    pythondf_grouped = df.groupby('name').sum()
    print(df_grouped)
    
    ```
    
-   **Aggregating Data**: We can aggregate data in a DataFrame using functions like `sum()`, `mean()`, and `count()`.
    
    Example:
    
    ```
    pythondf_agg = df.groupby('name').agg({'age': 'mean', 'income': 'sum'})
    print(df_agg)
    
    ```
    
-   **Merging Data**: We can merge two DataFrames on a common column using the `pd.merge()` function.
    
    Example:
    
    ```
    pythondf1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
    df2 = pd.DataFrame({'name': ['Alice', 'Charlie'], 'income': [50000, 60000]})
    df_merged = pd.merge(df1, df2, on='name')
    print(df_merged)
    
    ```
    
-   **Joining Data**: We can join two DataFrames on their index using the `pd.join()` function.
    
    Example:
    
    ```
    pythondf1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]}, index=['A', 'B'])
    df2 = pd.DataFrame({'income': [50000, 60000]}, index=['A', 'C'])
    df_joined = df1.join(df2)
    print(df_joined)
    
    ```
    
