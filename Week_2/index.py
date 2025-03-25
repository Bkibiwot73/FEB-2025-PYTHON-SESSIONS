my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

my_list.insert(1, 15)
print(my_list)

my_list.extend([50, 60, 70])
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()

index_30 = my_list.index(30)

print(f"Sorted list: {my_list}")
print(f"Index of 30: {index_30}")
