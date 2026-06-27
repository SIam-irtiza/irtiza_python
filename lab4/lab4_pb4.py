def distinct(numbers):

    new_list = []

    for item in numbers:

        if item not in new_list:
            new_list.append(item)

    return new_list

mylist = [1,2,3,3,3,4,5]

print(distinct(mylist))