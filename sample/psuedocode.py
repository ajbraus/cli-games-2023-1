

# sample = dict(one=1, two=2, three=3)
# print(sample)


person = {
    'name': "Henry",
    'age': 43,
    'home': { 'address': '924 Regent St', 'city': 'Marin' },
    'pets': [
        {
            'name': "SuzieQ",
            'species': 'Dog',
            'age': 7
        },
        {
            'name': "Edgelord",
            'species': 'Parrot',
            'age': 25
        }
    ]
}

# print(person['pets'][1]['name'])
# person['name'] = "Benjamin"
# print('name' in person)
# del person['name']
# print('name' in person)
# print(person)
for val in person.values():
  print(val)
# arr[3]
# print(person.name)









# arrive at park
# if it is sunny, put down blanket and begin bbq
  # if propane < 3, go buy more fuel
# else find shelter from rain

# if ice < 5, go buy ice
# if beer < 5, go on beer run 

# bbq includes
  # 
  # 


# Write a function that takes in an array of first, middle, and last names and returns a string of their name. 

# def full_name(arr):
#     return ' '.join(arr)

# print(full_name(["Michael", "B", "Jordan"]))

# # Write a function that takes in someone’s name and returns an array of their first and last name. 
# def first_and_last_arr(name):
#     return name.split(' ')

# print(first_and_last_arr("Steph Curry"))

# # Write a function that takes in an array and removes the last n-th elements
# def remove_nth_elements(arr, n):
#     arr.pop(n)
#     return arr

# print(remove_nth_elements([23,35,235,234,324,432,234], 3))

# Given an array of first and last name dictionaries, and return a list first and last names

# names = [{ 'first': "Fu", 'last': 'Bar'}, { 'first': "Baz", 'last': 'Blamo' }]

# full_names = []
# # LOOP!
# for n in names:
#     name = n['first'] + " " + n['last']
#     full_names.append(name)

# print(full_names)