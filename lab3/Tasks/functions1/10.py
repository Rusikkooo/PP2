# Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def uniq(my_list):
    new_list = []
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
    return new_list
my_list = list(map(int,input("Please enter your list: ").split()))
print(uniq(my_list))

