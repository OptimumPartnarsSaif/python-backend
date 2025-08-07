# -----------------------------
# 1. Use sets to remove duplicates from a list
# -----------------------------

print("🔹 Removing duplicates using sets:")
names = ["Alice", "Bob", "Alice", "Eve", "Bob", "Charlie", "Eve"]
print("Original list:", names)

unique_names = list(set(names))
print("Unique names:", unique_names)

print("\n" + "-"*40 + "\n")

# -----------------------------
# 2. Use dictionaries to count word frequency
# -----------------------------

print("🔹 Counting word frequency using dictionaries:")

text = """
apple banana apple orange banana apple cherry banana orange cherry
"""

words = text.strip().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

print("\n" + "-"*40 + "\n")

# -----------------------------
# 3. Same word frequency example using the walrus operator
# -----------------------------

print("🔹 Word frequency using walrus operator:")

word_count_walrus = {}
for word in words:
    word_count_walrus[word] = (count := word_count_walrus.get(word, 0)) + 1

print("Word frequencies (walrus):")
for word, count in word_count_walrus.items():
    print(f"{word}: {count}")
