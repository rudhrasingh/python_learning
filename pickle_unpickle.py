""" pickle is a serializer for iterable objects likes lists , tuples dictionaries 
Pickling -  is the process whereby a Python object hierarchy is converted into a byte stream
Unpickling -is the inverse operation, whereby a byte stream is converted back into an object hierarchy."""

import pickle
print('')
name_list=['rudhra','surya','akarsh']

print('pickling started ...')
picklefile = open("./pickle", 'wb') # it has to be wb to writen in binary  io stream
pickle.dump(name_list, picklefile)
picklefile.close()
print('pickling done ...')
print('pickle object created: '+str(picklefile)+' \n')


print('unpickling started ...')
picklefile = open('./pickle', 'rb')
result=pickle.load(picklefile)
picklefile.close()
print('unpickling done ...')
print('result obtained: ' + str(result))