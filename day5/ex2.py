numbers = [3, 5, 7, 5, 9, 3]

unique_ordered = []
seen = set()

for num in numbers:
    if num not in seen:
        unique_ordered.append(num)
        seen.add(num)

print(unique_ordered)
# ==============================================
# the second
# ==============================================
# Define the sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (A ∪ B)
union = A | B
print("Union (A ∪ B):", union)

# Intersection (A ∩ B)
intersection = A & B
print("Intersection (A ∩ B):", intersection)

# Difference (A - B)
difference = A - B
print("Difference (A - B):", difference)

# Symmetric Difference (A Δ B)
symmetric_difference = A ^ B
print("Symmetric Difference (A Δ B):", symmetric_difference)
# ==============================================
# the second third
# ==============================================
text = "apple banana apple cherry banana"

# Split the string into words
words = text.split()

# Use a set to find unique words
unique_words = set(words)

# Print results
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
# Dictionary creation
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Science", "English"]
}
print("Student Dictionary:")
print(student)

# Word frequency
text = "hello world hello"
words = text.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord Frequency Dictionary:")
print(word_freq)

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("\nDictionary of Squares:")
print(squares)

# Walrus operator input validation
while (num := int(input("\nEnter a number greater than 10: "))) <= 10:
    print("Number is not greater than 10, try again.")

print(f"✅ You entered: {num}")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = {}

for key in dict1.keys() | dict2.keys():
    if key in dict1 and key in dict2:
        # Use walrus operator to assign and compute
        merged[f"{key}_resolved"] = (v1 := dict1[key]) + (v2 := dict2[key])
        print(f"Conflict on '{key}': {v1} + {v2} = {merged[f'{key}_resolved']}")
    elif key in dict1:
        merged[key] = dict1[key]
    else:
        merged[key] = dict2[key]

print("\n✅ Merged Dictionary with Conflict Resolution:")
print(merged)
