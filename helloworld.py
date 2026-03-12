print("Hello world", end="")
print("welcome python")
print("laptop", "mouse", "keyboard",sep="\t")

#Variables

name= "Ravi"
age=22
city= "Chennai"
print(name, age, city, sep="-")

#Multiple assignment

name = "Meena"
age = 22
student=True
print(name, age, student)

#Indexing

word = "python"
print(word[0])
print(word[2])
print(word[-1])

#Arithematic operators

print(25 + 10)
print(50 - 20)
print(8 * 5)
print(100 / 10)
print(10 % 3)
print(2 ** 4)
print(20 // 3)

#BODMAS Expression

print(3 + 2 * 5 ** 2)

#Assignment operator

num = 50
num +=25
print(num)

num = 100
num /=10
print(num)

#comparison operators

print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)

#String Comparison

a = "apple"
b = "Apple"
print(a == b)

#Logical operators

print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))

#Membership operator

numbers = [10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

#Swap variables

a = 10
b = 20
a, b = b, a
print(a)
print(b)

#Bitwise XOR
a=6
b=3
print(a^b)