#Coding Task Write a program to calculate the area of a circle:
#Declare variables radius (8.9) and pi (3.14).
#Calculate the area using the formula: pi × radius × radius.
#Output only the area.

radius, pi= 8.9 ,3.14  #simultaneous assignments
area_of_circle= (pi*radius*radius)
print(area_of_circle)
print(round(area_of_circle, 2)) #rounding of the digit to two digitd
print(round(area_of_circle, 3)) 	#rounding of the digit to three digits

#exercise2(The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20)
mystring ="hello"
myfloat =10.0
myint=20
print(mystring, myfloat,myint)


#list
mylist = []
mylist.append(2)
mylist.append(4)
mylist.append(6)
mylist.append(8)
print(mylist)
print(mylist[0])
print(mylist[2])
print(mylist[1])

#exercise3 In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add #the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
#You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that #the index is zero-based, so if you want to access the second item in the list, its index will be 1.

numlist=[]
numlist.append(1)
numlist.append(2)
numlist.append(3)

stringlist=[]
stringlist.append("Hello")
stringlist.append("World")

names = ["John", "Eric", "Jessica"]

print("the secod name in list is", names[1] )
print(stringlist)
print(numlist)

#Python also supports multiplying strings to form a string with a repeating sequence:

lotsofhellos= "Hello"*10
print(lotsofhellos)

#Lists can be joined with the addition operators:
odd=[1,3,5,7]
even=[2,4,6,8]
all_number= odd+ even
print(all_number)

#The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x_list=[1,2,3,4,5,6,7,8,9,10]
y_list=[11,12,13,14,15,16,17,18,19,20]
print("x_list contains %d objects" %len(x_list))
print("y_list contains %d objects" %len(y_list))
big_list=x_list+y_list
print(big_list)
print("big_list contains %d objects" %len(big_list))

#newstyle
print(f"x_list contains{len(x_list)} objects")
print(f"y_list contains{len(y_list)} objects")
print(f"big_list contains{len(big_list)} objects")

#stringformatting

name="John"
age="23"
print(f"Hello,{name} you are,{age} years old")

#lengthof the string

s = "Strings are awesome"
print(f"The leghth of the string is {len(s)}")
print(f"The first occurance a is at {s.index("a")}")
print(f"the number of As should be {s.count("a")}")
print(f"The slice of the string is {s[:5]}")
print(f"The last slice of the string is {s[:]}")