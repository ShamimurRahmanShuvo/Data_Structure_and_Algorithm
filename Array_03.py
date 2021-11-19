# Array of odd integers within a range
min = int(input("Enter a Minimum number: "))
max = int(input("Enter a Maximum number: "))

odd_numbers = []

for i in range(min, max):
    if i%2 ==1:
        odd_numbers.append(i)
print("Odd Numbers", odd_numbers)