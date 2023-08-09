my_info = {"name": "Marin", "age": 35, "address": "Sofia"}

print(my_info)
print(my_info.values())
print(f'These are the dict values: {my_info.values()}')
print(my_info.pop("age"))
print(my_info)
my_info.update({"age": 35})
print(my_info)
my_info.update({"age": 36})
print(my_info.keys())
print(my_info.popitem())