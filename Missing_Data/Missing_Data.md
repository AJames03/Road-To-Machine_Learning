# Missing Data
**Author:** Aron James L. Betinol
**Published:** July 08, 2025
**Description:** This study is for my personal benefits and to help also the community to understand much better in the topic of Missing Data. And it has also a references comes from W3Schools and GeeksforGeeks.
---
### What is Missing Data?
- Missing data refers to the absence of a value in a dataset where a value is expected. It occurs when no data value is stored for a variable in an observation. This can happen for many reasons, such as:
    - A participant skipped a question in a survey.
    - A sensor or device failed to record a reading.
    - Data was lost or corrupted during processing or storage.
---
### Sample Codes by Python
```python
import pandas as pd
import numpy as np

data = {
    "A": [1, 2, 3, np.nan],
    "B": [4, np.nan, 6, 7],
    "C": [8, 9, np.nan, 11]
}

df = pd.DataFrame(data)
df_clean = df.dropna()
print(df_clean)
```

#### Explanation
- Each line much better to understand how it works and what it's functions.

##### 1. Pandas and Numpy
#
```python
import pandas as pd
import numpy as np
```
##### `NumPy`
**Purpose:** To work with numbers quickly and efficiently, especially with arrays or matrices.
- It makes math faster and easier.
- You can do things like adding arrays, matrix multiplication, and more.
- Example: You use NumPy for fast calculations in scientific or statistical work.
##### `Pandas`
**Purpose:** To work easily with tables or spreadsheets.
- It helps organize data into rows and columns.
- You can **filter**, **sort**, **group**, and **analyze data**.
- ***Example:*** You use pandas to clean and arrange your survey results.
---
##### 2. Data or Array
#
```python
data = {
    "A": [1, 2, 3, np.nan],
    "B": [4, np.nan, 6, 7],
    "C": [8, 9, np.nan, 11]
}
```
- It is a array of data.

##### 3. Data Frame
#
```python
df = pd.DataFrame(data)
```
- `df` it is a variable name
- `pd.DataFrame` it is a function of pandas
- `data` it is a variable name of array which created on the previous line.
- **Purpose:** it is use to display a raw data or the array.
---
##### 4. Data Cleaning
#
```python
df_clean = df.dropna()
```
- `dropna` the purpose of it is to drop a rows which has a NaN, Unknown, or Missing data.
---
##### 5. Output
#
```python
print(df_clean)
```
- `print()` it is used to display an output.
- `df_clean` this is the variable name from the previous
##### Note:
- To understand the code, if the row has a NaN, Unknown, or Missing Data automatically they are not showing to the output.
    

