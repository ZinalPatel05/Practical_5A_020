odd_numbers = []

for num in range(1, 101):
    if num % 2 != 0:
        odd_numbers.append(num)

print("List of odd numbers between 1 to 100:")
print(odd_numbers)

print("\nMinimum odd number:", min(odd_numbers))
print("Maximum odd number:", max(odd_numbers))
print("Total sum of odd numbers:", sum(odd_numbers))
