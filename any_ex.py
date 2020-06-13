""" any takes a list and results in True if any item is True or False if all items are false """
true_list=[True,False,True,False,True,True] # returns True
result1=str(any(true_list))
print(result1)

false_list=[False,False,False] # returns False
result2=str(any(false_list))
print(result2)

string_list=['rudhra','','surya'] # returns True
result3=str(any(string_list))
print(result3)

string_list2=['','','']  # empty strings are considered null/None in python # returns False
result4=str(any(string_list2))
print(result4)

