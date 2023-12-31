# Write your count_first_letter function here:
def count_first_letter(dict):
    new_dict={}
    for name in dict:
        first_letter = name[0]
        if first_letter not in new_dict:
            new_dict[first_letter] = 0
        new_dict[first_letter] += len(dict[name])
    return new_dict
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}