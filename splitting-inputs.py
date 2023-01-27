# Only 1 space
from_user = input('Enter two words: ')
print(from_user)  # 👉️ 'one two'

# 👇️ split with space separator
result = from_user.split(' ')
print(result)  # 👉️ ['one', 'two']

first, second = result
print(first)  # 👉️ one
print(second)  # 👉️ two


from_user = input('Enter two numbers: ')
print(from_user)  # 👉️ '5          10'   👈️ has multiple spaces between digits

# 👇️ split with space separator
result = [int(x) for x in from_user.split()]      # if want words, can just use results = [x for x in from_user.split()]
print(result)  # 👉️ [5, 10]

first, second = result
print(first)  # 👉️ 5
print(second)  # 👉️ 10

# https://bobbyhadz.com/blog/python-split-input
