import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

#using BST
# bst = BSTNode(names_1[0])

# for name_1 in names_1[1:]:
#     bst.insert(BSTNode(name_1))

# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

#optimized
# names1_set = set(names_1)
# names2_set = set(names_2)
# duplicates = list(names1_set.intersection(names2_set))

#using one set
# names_set = set(names_1)

# for name in names_1:
#     names_set.add(name)

# for name in names_2:
#     if name in names_set:
#         duplicates.append(name)

# using only lists
# less optimized than set but better than BST
sorted_names1 = sorted(names_1)
sorted_names2 = sorted(names_2)

idx1 = 0
idx2 = 0

while idx1 < len(sorted_names1) or idx2 < len(sorted_names2):       
    if sorted_names1[idx1] == sorted_names2[idx2]:
        duplicates.append(sorted_names1[idx1])
        idx1 += 1
        idx2 += 1
    elif sorted_names1[idx1] < sorted_names2[idx2]:
        if idx1 == len(sorted_names1) - 1:
            break 
        idx1 += 1
    elif sorted_names2[idx2] < sorted_names1[idx1]:
        if idx2 == len(sorted_names2) - 1:
            break 
        idx2 += 1


    




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


