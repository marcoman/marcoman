# Array split
# Prompt:
# Write a function that processes the array and outputs a list of sublists. Each sublist should contain consecutive elements from the original array, with the sublists being separated by None values. For example, given the input array 

# [12, 9, 3, None, 11, 2, 10, None, 5, 13, None, 1]

# Your function should return:

# [[12, 9, 3], [11, 2, 10], [5, 13], [1]]

mylist = [12, 9, 3, None, 11, 2, 10, None, 5, 13, None, 1]

list_of_lists = []

# Iterate through the list to get the output
newlist = []
for item in mylist:
    if item is None:
        list_of_lists.append(newlist)
        newlist = []
        
    else:
        newlist.append(item)
        print (newlist)

if (len(newlist) > 0):
    list_of_lists.append(newlist)

print (f'list_of_lists is {list_of_lists}')