# Write your frequency_dictionary function here:
def frequency_dictionary(list_of_strings):
    new_dict={}
    for string in list_of_strings:
        if string not in new_dict:
            new_dict.update({string:0})
        new_dict[string]+=1
    
# Uncomment these function calls to test your  function:
#print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}