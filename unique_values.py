# Write your unique_values function here:
def unique_values(dict):
    my_list =[]
    for val in dict.items():
        if val[1] not in my_list:
            my_list.append(val[1])
    return len(my_list)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1