# Exercise #1
# Filter out all of the empty strings from the list below

# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

list(filter(lambda item: item.strip(), places))


# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda x: (x.split()[-1]).lower())
print(author)


# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

# F = (9/5)*C + 32
# How do you convert from Celsius to Fahrenheit?
# To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
cities_farhenheit = list(map(lambda c:  (c[0], (9/5) * c[1]+ 32), places))


print(cities_farhenheit)


# Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.

# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8

def fibonacci(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else: 
        return (fibonacci(f-1) + fibonacci(f-2))

print(fibonacci(5))