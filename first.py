print("Billie Eililsh")

name = 'BillieEilish'
age = 22
mark = 99
print(name,age,mark)
print(type(name))

a = 10
b = 20
sub = a-b
sum = a+b
div = b/a
mul = a*b
print(sub,sum,div,mul)
print(not(a>b))

#function
def Cal_sum(a,b):
    sum=a+b
    return sum
print(Cal_sum(5,10))

a=input('Enter a number')
print(a)
print(type(a))

p=int(input('Enter any number'))
j=int(input('Enter another number'))
sum = p+j
print(sum)

#Condition
age = 20
if(age>=18):
    print("You are legal")
else:
    print("Bachhei xass")

mark =int(input("Enter your Grade"))
if(mark>=90):
    print("Grade is A")
elif(90>mark>=80):
    print("Grade is A-")
elif(80>mark>=70):
    print("Grade is B")
elif(70>mark>=60):
    print("Grade is B-")
elif(60>mark>=50):
    print("Grade is C")
elif(50>mark>=40):
    print("Grade is C-")
else:
    print("YOU FAILED BROTHER")


i = 1
while i<=5:
    print(i)
    i+=1

i = 5
while i>=1:
    print(i)
    i-=1

i = 5
while i>=1:
    print(i)
    if(i==3):
        break
    i+=1
    print("End of Loop")

for i in range(5):
    print(i**2)

for i in range(1,10,2):
    print(i)

for i in range(0,10,2):
    print(i)

#list
list = [20,30,40,"Billie"]
print(list)
print(type(list))
list[0] = 50
print(list)
list.sort()
print(list)

print("HI BILLIE")

#DAY 2


list = [50,50,40]
list[0] = 80
print(list)

tup = (50,50,40)
print(tup.count(50))
print(len(tup))
print(tup.index(50))
print(tup)

dict = {
    "name" : "Billie",
    "age" : 23,
    "mark" : [20,30,40,50]
}
dict["name"] = "Billie Eilish"
print(dict)
print(dict["name"])

set1 = {1,2,2,3,"ram","gita"}
print(len(set1))
set1.add(6)
set1.add("Billie")
set1.remove(2)
print(set1)


set1 = {1,2,3,4,5}
set2 = {1,2,7,8,5}
print(set1)
print(set2)
print(set1.intersection(set2))
print(set1.union(set2))


set1 = {1,2,2,3,4}
set2 = {2,4,5,6,7}
forset1 = frozenset(set1)
forset2 = frozenset(set2)
print(forset1)
print(forset2)
print(forset1.intersection(forset2))
print(forset1.union(forset2))

from collections import deque
dq = deque([1,2,3,2,4,5])
list = [20,30]
dq.append(6)
dq.appendleft(0)
dq.remove(2)
dq.extend(list)
dq.insert(2,20)
print(dq)


from collections import defaultdict
name = "BillieEIlish"
dd = defaultdict(int)
for ch in name:
    dd[ch]+=1
print(dd)


squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(5)]
print(squares)

gen = (x**2 for x in range(5))
for val in gen:
    print(val)


marks = [60,70,80,90]
def s_grade(marks):
    if marks>=90:
        return "A"
    elif 90>marks>=80:
        return "B"
    elif 80>marks>=70:
        return "C"
    else:
        return "D"
grade = map(s_grade,marks)
print("Student marks",marks)
print("Student Grade",next(grade))   #list ko satta next 
print("Student Grade",next(grade))
print("Student Grade",list(grade))

#filter
marks =[60,50,45,35]
def fail(marks):
    return marks<50
result = filter (fail,marks)
print("student marks", marks)
print("failing marks",list(result))

from functools import reduce
num=[2,4,6,8]
def my_sum(x,y):
    return x+y
sum = reduce(my_sum,num)
print(sum)

num = 5
square = num ** 2
print("Square is : ",square)

f=lambda x: x**2   #2nd way
print(f(5))

#exception handle
try:
    num=int(input('Enter a number:'))
    result=10/num
    print('Result is:',result)
except ZeroDivisionError:
    print('Cnnot divide by zero')
except ValueError:
    print('Invalid input,please enter a number')


class NegativeValueError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeValueError("Negative values not allowed")
    print("You entered:", num)
except NegativeValueError as e:
    print(e)
except ValueError:
    print("Invalid input, please enter a valid number")























