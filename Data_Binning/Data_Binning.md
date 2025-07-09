# DATA BINNING
---
**Author:** Aron James L. Betinol

**Date Write:** July 08, 2025

---
### What is Data Binning?
- Binning is the process of **grouping continuous data into discrete categories or intervals**, known as bins. It is commonly used in data analysis, machine learning, and image processing to simplify or summarize data.

#### Sample Code:
```python
import pandas as pd

ages = [21, 22, 25, 29, 34, 38, 41, 42, 47, 55]

df = pd.DataFrame({'age':ages})

bins = [20, 30, 40, 50, 60]
labels = ['Young', 'Middle-Age', 'Older', 'Senior']

df["Age groups"] = pd.cut(df["age"] , bins, labels=labels)

print(df)
```

#### Explanation:
---
#
```python
import pandas as pd
```
- According to www.w3schools.com, **Pandas** is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
- The name **"Pandas"** has a reference to both **"Panel Data"**, and **"Python Data Analysis"** and was created by Wes McKinney in 2008.
- It was needed to create a Panel Data using python.
---
#

```python
ages = [21, 22, 25, 29, 34, 38, 41, 42, 47, 55]
```
- It is a datasets which is needed or in specific a set of age.

```python
df = pd.DataFrame({'age':ages})
```
- It is used to display all the datasets according to the pandas data frame.

**Output:**

|   | Age |  
|-------|-----|
| 0 | 21  | 
| 1   | 22  |
| 2 | 25  | 
| 3   | 29  |
| 4 | 34  | 
| 5   | 38  |
| 6 | 41  | 
| 7   | 42  |
| 8 | 47  | 
| 9   | 55  |
---
#

```python
bins = [20, 30, 40, 50, 60]
labels = ['Young', 'Middle-Age', 'Older', 'Senior']
```
- It is a used for the range
    - [20] = Range 20-29
    - [30] = Range 30-39
    - [40] = Range 40-49
    - [50] = Range 50-60
    - [60] = Range 60
- Now the labels:
    - [20] = Range 20-29 - [Young]
    - [30] = Range 30-39 - [Middle-Age]
    - [40] = Range 40-49 - [Older]
    - [50] = Range 50-60 - [Senior]
    - [60] = Range 60 - [Senior]
---
#
```python
df["Age groups"] = pd.cut(df["age"] , bins, labels=labels)
```
**To understand this line list identify each purpose:**
```python
df["Age groups"]
```
- It is holding a title of the column which is "Age groups"
```python
pd.cut(df["age"] , ... )
```
- **pd.cut:**
    - is used to categorize each age into a group or range (like 20–30, 30–40, etc.).
- **df["age"]:**  
    - refers to the "age" column from a DataFrame named df
```python
bins, labels=labels
```
- **bins -**  is a list that defines the intervals or cut-off points for splitting your numerical data.
- **labels -** is a list of names or tags you assign to each bin.
---
#
```python
print(df)
```
- It is used to display the contents of the DataFrame df on the screen.
