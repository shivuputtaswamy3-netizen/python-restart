#execise1 
x=10
x=20
x=x+5
print(x)

print("-------")
a = 5
b = 10
a = b
b = 20
print(a, b)

print("Exercise 4: Chain Assignment")
x = y = z = 100
y = 50
print(x, y, z)


print("-------")

print("Exercise 5: Step-by-Step Tracking")
count = 0
count = count + 1
count = count + 1
count = count * 2
print(count)

print("-------")
print("Shortcut Operators")

x = 10
x += 5
x *= 2
print(x)

print("-------")
print("Exercise 7: Swap Without Python Magic")
a=30
b=600
temp=30
a=b
b=temp
print(a,b)

print("-------")
print("Exercise 9: Input Trap")
x = int(input("Enter a number: "))
y = x + 5
print(x,y)


print("-------")
print("Exercise 10: Type Awareness")
x = 10
y = int("10")
z = x + y
print(z)


print("-------")
print("Exercise 11: Lists vs Variables")
a=[1,2,3]
b=a
b.append(4)
print(a,b)


print("-------")
print("Exercise 12: Running Total")
total = 0
for i in range(5):
	#num=int(input(f"Enter the number {i+1}: "))
	#total=num+total
	#print(f"the running total is {total}")
print(f"The final total is {total}")

print("-------")
print("Digit Extraction")
n = 3497
last_digit = n % 10
n = n // 10
print(last_digit,n )











