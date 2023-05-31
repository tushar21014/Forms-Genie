import re

data_params = '''%.@.[1275419724,"Can you attend?",null,2,[[877086558,[["Yes,  I'll be there",null,null,null,false],["Sorry, can't make it",null,null,null,false]],true,[],[],null,null,null,null,null,[null,[]]]],null,null,null,[],null,null,[null,"Can you attend?"]],"i5","i6","i7",false]
[[['What is your name?']], [["Yes,  I'll be there"], ["Sorry, can't make it"], ['Can you attend?']]]'''
pattern = r'"([^"]*)"'
main_words = re.findall(pattern, data_params)
unique_list = list(set(main_words))
filtered_list = [elem for elem in unique_list if not any(f'i{x}' in elem for x in range(1, 101))]
print("I am main words" , filtered_list)
split_list = [[item] for item in filtered_list]
print("i am split list", split_list)
