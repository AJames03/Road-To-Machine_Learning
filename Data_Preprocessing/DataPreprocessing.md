# DATA PREPROCESSING
---

##### `Author:` Aron James L. Betinol

##### `Published Date:` July 09, 2025

##### `Description:` This is for my personal study to improve my skills and knowledge in Data Preprocessing

## INTRODUCTION
---

**`What is Data Preprocessing?`**

- A Data Preprocessing is a crucial step in the data science and machine learning pipeline. It refers to the process of cleaning, transforming, and organizing raw data into a format suitable for analysis or model training.

- From the previous study we learn about `Data Binning`, `Missing Data`, `Normalization`, `Data Cleaning` and `Replace Data` which is important before the data is uploading to the database/s.

**`How to implement the Data Preparation?`**

#### 1. **White Space**

Using Python, you can use `.strip()`, `.lstrip()`, `.rstrip()`, or `.replace()`
- **.strip()** - is a string method in Python that removes leading and trailing white space (spaces, tabs, newlines) from a string.
- **.lstrip()** - also known as left strip to remove the left white space.
- **.rstrip()** - also known as right strip to remove the right white space.
- **.replace()** - it is use to replace either from with white space to none white space area.

*Example:*
    
```python
text = " Hello World "
    
cleaned = text.strip()
lcleaned = text.lstrip()
rcleaned = text.rstrip()
no_spaces = text.replace(" ", "")
    
print("1. " + cleaned)
print("2. " + lcleaned)
print("3. " + rcleaned)
print("4. " +no_spaces)
```

*Expected Output:*

```python
1. Hello World
2. Hello World 
3.  Hello World
4. HelloWorld
```

#### 2. Uppercase and Lowercase

In Python, you can convert strings to uppercase or lowercase using built-in string methods:

```python
text = "Hello World"
lower_text = text.lower()
print(lower_text)

# Output: hello world
```

<table style="width:100%; text-align:center;">
  <tr>
      <th>Method</th>
      <th>Description</th>
      <th>Example</th>
  </tr>
    <tr>
        <td>lower()</td>
        <td>Converts all characters to lowercase</td>
        <td>"Python".lower() -> "python"</td>
    </tr>
    <tr>
        <td>upper()</td>
        <td>Converts all characters to uppercase</td>
        <td>"Python".upper() -> "PYTHON"</td>
    </tr>
    <tr>
        <td>capitalize()</td>
        <td>Capitalizes the first character</td>
        <td>"python is fun".capitalize() -> "Python is fun"</td>
    </tr>
    <tr>
        <td>title()</td>
        <td>Capitalizes the first letter of each word</td>
        <td>"python is fun".title() -> "Python Is Fun"</td>
    </tr>
    <tr>
        <td>swapcase()</td>
        <td>Swaps uppercase to lowercase and vice versa</td>
        <td>"PyThOn".title() -> "pYtHoN"</td>
    </tr>
</table>

#### 3. Data Types

It is simple but it is useful in data cleaning to insure that data is accurate to the data types which is the `string`, `boolean`, `integers`, `float`, `double`, etc...

---

# Conclusion:

- It has a different approach for data preprocessing and data cleaning. But there's a primary needed for data cleaning.
