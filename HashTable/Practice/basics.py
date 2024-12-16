my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa', 'Stuart'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]


# def hash_function(name: str):
#     sum_of_chars = 0
#
#     for char in name:
#         sum_of_chars += ord(char)
#
#     return sum_of_chars % 10

def hash_function(name: str):
    return sum(ord(char) for char in name) % 10

def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]

    if value not in bucket:
        bucket.append(value)

def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]

    return value in bucket

add('Stuart')
add('Stuart')

print(my_hash_set)
print('Contains Stuart:',contains('Stuart'))
