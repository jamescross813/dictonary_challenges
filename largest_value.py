# Write your max_key function here:
def max_key(dict):
    starting_key = 0
    starting_value = 0
    for key, value in dict.items():
        if value > starting_value:
            starting_value=value
            starting_key=key
    return starting_key
# Uncomment these function calls to test your  function:
# print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
# print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"