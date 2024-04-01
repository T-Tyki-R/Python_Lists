# Advanced List Methods and Identity Operators

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Possible Solution via Nested Loops
for sub_name in submitted:
    for att_name in attended:
       if sub_name is att_name:
           print(sub_name + " had submitted their work")
           break
    
print(True if submitted is attended else False)

# Help
for att_names in attended:
    for sub_names in submitted:
        if att_names not in  sub_names:
            removed = attended.remove(att_names)
            print(removed)
        