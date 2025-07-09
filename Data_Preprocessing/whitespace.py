text = " Hello World "
    
cleaned = text.strip()
lcleaned = text.lstrip()
rcleaned = text.rstrip()
no_spaces = text.replace(" ", "")
    
print("1. " + cleaned)
print("2. " + lcleaned)
print("3. " + rcleaned)
print("4. " + no_spaces)