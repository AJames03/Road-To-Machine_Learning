import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "First_Name": ["Aron James"],
    "Middle_Name": [None],
    "Last_Name": ["Betinol"]
}

df = pd.DataFrame(data)

# For First Name
df["First_Name"] = df["First_Name"].fillna("Unknown")
df["First_Name"] = df["First_Name"].str.upper()

# For Middle Name
df["Middle_Name"] = df["Middle_Name"].fillna("Unknown")
df["Middle_Name"] = df["Middle_Name"].str.upper()

# For Last Name
df["Last_Name"] = df["Last_Name"].fillna("Unknown")
df["Last_Name"] = df["Last_Name"].str.upper()

print(df)

text = " Hello World "
    
    cleaned = text.strip()
    lcleaned = text.lstrip()
    rcleaned = text.rstrip()
    no_spaces = text.replace(" ", "")
    
    print("1. " + cleaned)
    print("2. " + lcleaned)
    print("3. " + rcleaned)
    print("4. " + no_spaces)