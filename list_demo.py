# Array
"""
# Negative index => index from backward
# [1:] => from index 1 to end
# [1:3] => from index 1 to 2 (3 excluded)

number_list = [1, 10, 2, 20, 3, 30, 2]

name_list = ["John", "Smith", "Anne", "Ethan"]

name_list.extend(number_list)
name_list.append("Luther")
name_list.insert(0, "007")
name_list.remove("Anne")  # Remove spefic item
name_list.pop()  # Remove last item
# name_list.clear()
# number_list.sort()
# number_list.reverse()
number_list2 = number_list.copy()
print(number_list2)
"""

# Tuple => immutable (cannot modify)
