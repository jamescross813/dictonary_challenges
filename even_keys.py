# Write your sum_even_keys function here:
def sum_even_keys(dict):
    sum = 0
    for key, value in dict.items():
        if key%2==0:
            sum+=value 
    return sum
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6