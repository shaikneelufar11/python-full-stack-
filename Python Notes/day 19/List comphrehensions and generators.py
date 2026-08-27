# List Comprehension

squares = [x * x for x in range(6)]
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)

names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)

prices = [1000, 800, 450, 300]
discounted = [price * 0.9 for price in prices]
print(discounted)

product_info = [("Laptop", 1000), ("Phone", 800), ("Tablet", 450)]
expensive = [name for name, price in product_info if price > 700]
print(expensive)

# Nested List Comprehension
products_colors = [
    {"name": "Laptop", "colors": ["Silver", "Black"]},
    {"name": "Phone", "colors": ["Gold", "Blue"]}
]

all_colors = [
    color
    for product in products_colors
    for color in product["colors"]
]

print(all_colors)


# Generators

def simple_generator():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("End")


gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))



# Generator with while loop

def count_up_to(n):
    count = 1

    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)

print(next(counter))
print(next(counter))
print(next(counter))


# Generator for square numbers

def square_numbers(n):
    for i in range(n):
        yield i * i
squares = square_numbers(5)
print(next(squares))
print(next(squares))

'''List Comprehension → Creates a list in a concise way

Generator → Produces values one at a time

yield → Produces a value and pauses the function

next() → Moves the generator to the next yield

Generator → Saves memory because values are generated when needed'''