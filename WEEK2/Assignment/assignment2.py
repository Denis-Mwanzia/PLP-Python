# Creating empty list: my_list
my_list = []
print(f"my_list = {my_list}")

# Appending elements [10,20,30,40] to the my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending elements, my_list = {my_list}")

# inserting elements 15 to the my_list at second position
my_list.insert(1,15)
print(f"After inserting 15, my_list = {my_list}")

# extending my_list elements with another list [50,60,70]
my_list.extend([50,60,70])
print(f"After extending my_list with [50,60,70], my_list = {my_list}")

# removing the last element from my_list
my_list.pop()
print(f"After removing the last element, my_list = {my_list}")

#Sorting my_list in ascending order
my_list.sort()
print(f"After sorting my_list in ascending order, my_list = {my_list}")

# Finding and printing the index of 30 in my_list
indexOf30 = my_list.index(30)
print(f"The index of 30 in my_list is {indexOf30}")