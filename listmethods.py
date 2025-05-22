# lists(collection of different data type) and tuples are ordered ,allow duplication in thier member
# sets and dictionaries are unorderd,donot allow duplication in thier member

#list method
fruit=list(2,3,4,5,6,7,8)
# the above list is the same with the bottom one
fruit=[2,3,4,5,6,7,8]
# last_index=len(fruit)-1 to acces the last element
first,second,*rest=fruit
print(first) #gives us only the first element(2)
print(second)#gives us only the second element(3)
print(rest)#gives us new list contains the rest element(4,5,6,7)
number=[5,6,7,8,9,0]
first,*rest,fifth=number
print(first) # gives us the first element(5)
print(rest)#gives us new list contains the rest relement until 9th
print(fifth) # gives us the 5th element
number[0]=10  #replace 10 by first index(5)
newnum=len(number)-1 # contains the last index
fruit[newnum]=23 # replace the last index by 23
fruit.insert(2,45)# insert 45 in 3rd index
fruit.remove(4)# remove 4 from the list
fruit.pop(9)# pop remove the last item or if we give it index it remove that value found in that index
del fruit # delete the fruit list itself
del fruit[3]#delete the 3rd index 
fruits.clear()# clears the list, gives us empty list []
print(fruit+number)# join fruit and number respectively=[2,3,4........5,..0]
print(number+fruit)# join number and fruit respectively=[5,6......2,3...8]
print(fruit.count(9))# counts number 9 in fruit
print(fruit.index(8)) #print index of 8
print(fruit.reverse())#reverse the item of fruit
print(fruit.sort())#by modifies the first list sort the element ascending
print(fruit.sort(reverse=True))#sort the element descendingly 
print(sorted(fruit))# gives the sorted list without modifinig the original list



#tuple
company=('wiki','google')
#the above method is equal to the below one
company=tuple('wiki','google')
company[1]#gives us the result in index 1
#tuple is immutable so if we want to modify we can change to list
industry=list(company)#it changes to list
k=tuple(industry)#if we want to change to tuple
print('l' in company)#checks if l is existed in company
subject=('math','english','physics')
teacher=('veronica','linda','eric')
course=subject+teacher # result will be tuple of concatnation of both
#it isn't possible to delete individual element from tuple but we can delete the tuple it self
del course # delete the tuple it self 


#sets

sibiling={'lwam','hewan','mena'}
parent={'ella','richo'}
len(parent)# to get length of the set
print('gem' in parent)# to check if gem is in parent
parent.add('arsema') # to add single value
parent.update(['mom','dad','bro'])#to add multiple value to set but it has to be in list argument
family=('lul','mebre','moke')
parent.update(family)# update the value of parent by ading family tuple
#in set we can't insert value to set simply but if we want
my_set = {1, 2, 3}
value_to_replace = 2
new_value = 4

if value_to_replace in my_set:
    my_set.remove(value_to_replace)
    my_set.add(new_value)

print(my_set)
# Expected output: {1, 3, 4}
#we can also use clear method to empty the set
parent.clear()
#we can delete the set itself
del parent
#we can change list to set and give us the unique values and also we can change set to list
animal=['dog','cat']
homeanimal=set(animal)#to change list to set
#we can join two sets using union method(create new set) or using update method
parent.union(sibiling)
#we can also get intersection value from 2 sets
parent.intersection(sibiling)
lists={3,4,5,6}
menu={1,2,3,5}
menu.issubset(lists)# gives us boolean value
menu.issuperset(lists)#gives us boolean value 
lists.difference(menu) # gives us new set contains the content of lists that didnt contain in menu
# if two sets doesn't have common value and call them disjoint and we can also check if they have common value
menu.isdisjoint(lists) # gives us boolean value if they dont have same gives us true
listss=[2,3,3,4,5,6]
change=set(listss)#changes to sets which means gives us only the unique values

#  dictionary:
# dictionary  is orderded and changeable and donot allow duplicates for key  but for value it can duplicate and it store data in key:value pairs.
# Keys must be immutable: This means keys can be strings, numbers, or tuples but not lists.
# Keys must be unique: Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
dictionary={'brand':'ford','model':'fiat'}
print(len(dictionary))
# we can also use dict() to declare dictionaries
#ell=dict(age=23,name='lwam')
dictionary.items()# gives us the whole item of the dictionary in to list of tuples
#result will be =dictionary items([('brand','ford'),('model','fiat')])
dictionary.keys() # gives us the keys only as a list = dictionary_keys(['brand','model'])
dictionary.values() # gives us the values only as a list =dictionary_values(['ford','fiat'])
name=["lwam","hewan","merry"]
age=[23,34,45]
data=dict([(name,age) for name,age in zip(name,age)])  # using this method(list comperehension method) we can change lists to dictionary. the list comprehesion gives us list of tuple but the dict
# changes it to dictionary.
print(data) # out put wiil be {'lwam': 23, 'hewan': 34, 'merry': 45}
change=list(data) # gives us the list of keys only =['lwam', 'hewan', 'merry'] but if we want to change all of these values to list we use the below method
dataa=list(data.items()) # changes it to a list of tuple=[('lwam', 23), ('hewan', 34), ('merry', 45)]
list_from_dict = list(zip(data.keys(), data.values())) # we can also use zip method to change it to list
# functions operation
def students():
    print('lwam')
