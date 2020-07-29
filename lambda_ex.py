""" lambda is a anonymous function """
names=['rudhra','surya','akarsh']
new_list = map(lambda x:x+' dev',names) # map returns an iterable object
print(new_list)
for i in new_list:
    print (i)

