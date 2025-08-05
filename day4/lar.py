def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

# Part 1: Second largest
nums = [12, 45, 2, 41, 31, 10, 12]
print("Original list:", nums)
print("Second largest number:", second_largest(nums))

# Part 2: Merge dictionaries using union (Python 3.9+)
dict1 = {"apple": 3, "banana": 5}
dict2 = {"banana": 10, "cherry": 7}

merged = dict1 | dict2
print("Merged dictionary:", merged)
