# write a python program to remove duplicate from a list.

## There are various ways to remove duplicate from a list. Let's see.

def remove_duplicate(lst):
    li = []
    for item in lst:
        if item not in li:
            li.append(item)
    return li

lst1 = ['a','b','c','a','c','d','c','e','c']

print("After remove duplicates from lst1",remove_duplicate(lst1))
