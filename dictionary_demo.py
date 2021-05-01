# Allows to store information as key value pair

numbers_dict = {
    "one": "1",
    "two": "2",
    "three": "3"
}

# print(numbers_dict['one'])
print(numbers_dict.get("four", "not a valid key"))
