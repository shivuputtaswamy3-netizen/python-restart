a=2
b=3
print("The sum is:",a+b)


#variale assignment
d=7
print("the inital assignment is:",d)
d="Rajesh"
print("the second assignment is:",d)

#strings indexing 

mystring = "Hello Good morning, \nhow are you today"
print(mystring)
print("the length of my string is:",len(mystring))
print("The first letter of my string is:",mystring[0])
print("The last letter of my string is:",mystring[-1])

#print slicing
print(mystring[0:6])
print(mystring[0:-2])
print(mystring[2:])

#stepsize
string2 = "ABCDEFGHIJK"
print(string2)
print("The sliced string upt0 2 i:",string2[:2])
print("The last two sliced:",string2[:-2])
print("The first two sliced:",string2[2:])
print("The first and last are two strings liced:",string2[2:-2])
print("The step size of 2:",string2[::2])
print("The step size of 2:",string2[::3])
print("The step size of 2:",string2[2:-2:2])

#reversing a strip

print("The reverse of the strip is:", string2[::-2])

#operations with string

F="shiva Kumar"
S="Kodihalli Puttaswamy"
print("The full name is:", F)
print("The caps of full name is:", F.upper())

#formatting with strings
print(f"The Full name  is {F+S}")


#lists its a list of objects that are in a sequence.some operations can be done on lists too.

list1 =[' 1', '2', '3','4']
list2 =['One ','Two ','Three','four']
print(f"The final list is {list1}+{list2}")
list1.append(list2)
print(f"The finl list is {list1}")
list1.append('six')
print(list1)
list1[4]= "All caps"
print(list1)


#excercises

list=[10,'Eleven',12]


















