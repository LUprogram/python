firstname = 'Melo'
lastname = 'Mario'
age = 30
country = 'Portugal'
marks = 98.05
total_items = list()
total_items.append('2 sisters')
shopping = list()
shopping.append('Shopping list:')
shopping.append('-eggs')
shopping.append('-milk')
shopping.append('-bread')
tuple_1 = tuple()
tuple_1 = (3,4,5,6,7,8,8)
information = dict()
information = { 'python':'a snake','ruby':'a gemstone','perl':'something from the sea'}
information.update({'julia':'beautiful name'})
wow = {2,4,6,8,0}


print('my name is:',firstname, 'and im',age,' old and i stay in:',country,', I got', marks, '. I have ',
total_items)

print('my name is: {} and im {} old and i stay in: {}, I got {}'.format(firstname, age, country, marks))

print('my name is: {1} and im {0} old and i stay in: {3}, I got {2}'.format(age,firstname, marks, country))

print(f'my name is: {firstname} and im {age} old and i stay in: {country}, I got {marks}'.format(firstname, age, country, marks))

print(f'my name is: {"Lala"} and im {34} old and i live in: {"Siria"}, I got {99.99}')

for i in shopping:
    print(i)

print(shopping, type(shopping))

print(tuple_1, type(tuple_1))

print(information, type(information))

print(wow, type(wow))