# Advanced List Methods and Identity Operators

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Possible Solution via Nested Loops
for sub_name in submitted:
    if sub_name in attended:
        print(sub_name + " had submitted their work")
           
    
print(True if submitted is attended else False)

for att_names in attended:
     if att_names not in  submitted:
        attended.remove(att_names)
        print(attended)
        