heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# Length of the list
print("Length of the list = ", len(heros))

# Add black panther
heros.append('black panther')
print("Updated heros = ", heros)

# Add black panther after hulk
heros.remove('black panther')
heros.insert(3, 'black panther')
print("After 2nd update: ", heros)

# Replace thor and hulk with doctor strange
heros[1:3] = ['doctor strange']
print("3rd Update: ", heros)

# Sort in alphabetical order
heros.sort()
print("Sorted Heros: ", heros)