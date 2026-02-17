# odd_numbers.py

# Generate list of odd numbers between 1 and 100
odd_numbers = [num for num in range(1, 101) if num % 2 != 0]

# Display results
print("List of odd numbers between 1 and 100:")
print(odd_numbers)

print("\nMinimum odd number:", min(odd_numbers))
print("Maximum odd number:", max(odd_numbers))
print("Total sum of odd numbers:", sum(odd_numbers))
