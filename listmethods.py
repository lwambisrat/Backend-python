# lists(collection of different data type) and tuples are ordered ,allow duplication in thier member
# sets and dictionaries are unorderd,donot allow duplication in thier member
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
print(fifth) # gives us the 10th element
number[0]=10  #replace 10 by first index(5)
newnum=len(number)-1 # contains the last index
fruit[newnum]=23 # replace the last index by 23
fruit.insert(2,45)# insert 45 in 3rd index
fruit.remove(4)# remove 4 from the list
fruit.pop(9)# pop remove the last item or if we give it index it remove that value found inthat index
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