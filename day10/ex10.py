# -------------------------------
# Exercise 1: Custom Fibonacci Iterator
# -------------------------------
class Fibonacci:
    def __init__(self, n):
        self.n = n        # total terms
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b


# -------------------------------
# Exercise 2: Alternating Signs Generator
# -------------------------------
def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield num * sign
        sign *= -1


# -------------------------------
# Exercise 3: Dictionary Comprehension with ASCII
# -------------------------------
def word_ascii_dict(words):
    return {word: {ch: ord(ch) for ch in word} for word in words}


# -------------------------------
# Exercise 4: Set Comprehension for Vowels
# -------------------------------
def extract_vowels(s):
    vowels = "aeiou"
    return {ch.upper() for ch in s if ch.lower() in vowels}


# -------------------------------
# Exercise 5: Prime Generator
# -------------------------------
def primes():
    yield 2
    found = [2]
    n = 3
    while True:
        is_prime = True
        limit = int(n ** 0.5)
        for p in found:
            if p > limit:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            found.append(n)
            yield n
        n += 2


# -------------------------------
# DEMO SECTION
# -------------------------------
if __name__ == "__main__":
    # Exercise 1 Demo
    print("Exercise 1: Fibonacci (first 10 terms)")
    fib = Fibonacci(10)
    print(list(fib))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # Exercise 2 Demo
    print("\nExercise 2: Alternating Signs")
    nums = [1, 2, 3, 4, 5]
    print(list(alternating_signs(nums)))  # [1, -2, 3, -4, 5]

    # Exercise 3 Demo
    print("\nExercise 3: Word -> {char: ASCII}")
    words = ["hi", "cat"]
    print(word_ascii_dict(words))
    # {'hi': {'h': 104, 'i': 105}, 'cat': {'c': 99, 'a': 97, 't': 116}}

    # Exercise 4 Demo
    print("\nExercise 4: Extract vowels from string")
    s = "Hello World"
    print(extract_vowels(s))  # {'E', 'O'}

    # Exercise 5 Demo
    print("\nExercise 5: First 6 primes using next()")
    prime_gen = primes()
    for _ in range(6):
        print(next(prime_gen), end=" ")  # 2 3 5 7 11 13
    print()
