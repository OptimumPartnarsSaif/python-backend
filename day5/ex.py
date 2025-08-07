# -----------------------------
# Merge two dictionaries using the walrus operator
# -----------------------------

print("🔹 Merge two dictionaries with key conflict resolution")

# Example input dictionaries
dict1 = {
    "apple": 2,
    "banana": 3,
    "cherry": 1
}

dict2 = {
    "banana": 4,
    "cherry": 2,
    "date": 5
}

# Merge dictionaries: add values when keys conflict
merged_dict = {}

# Go through all keys in the union of both dictionaries
for key in dict1.keys() | dict2.keys():
    merged_dict[key] = (
        (val1 := dict1.get(key, 0)) + (val2 := dict2.get(key, 0))
    )
    print(f"{key}: {val1} (from dict1) + {val2} (from dict2) = {merged_dict[key]}")

# Final merged result
print("\n✅ Merged Dictionary:")
print(merged_dict)
