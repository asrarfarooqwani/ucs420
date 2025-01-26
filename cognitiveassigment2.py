#question1
l = [10, 20, 30, 40, 50, 60]
print(l)
l.append(100)
l.append(200)
print(l)
del l[0]
del l[2]
print(l)
l.sort()
print(l)
l.reverse()
print(l)
#question2
score = [45, 89.5, 76, 45, 4.89, 92, 58, 45]
print(score)
m = max(score)
print(m)
i = score.index(m)
print(i)
mm = min(score)
print(mm)
count = score.count(mm)
print(count)
x = float(input("search a score "))
if x in score:
     print(score.index(x))
else:
    print("not present")
#question3
def checkprime(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    for i in range(2, n - 1):
        if n % i == 0:
            return 0
    return 1
import random as r
random_list = []
for i in range(0,100):
    random_list.append(r.randint(100, 900))
print(random_list)

sumeven = 0
sumodd = 0
sumprime=0
for i in range(0,100):
    if random_list[i] % 2 == 0:
        sumeven += random_list[i]
    else:
        sumodd += random_list[i]
for i in range(0,100):
    flag=checkprime(random_list[i])
    if flag==1:
        sumprime=sumprime+random_list[i]     
print(sumodd)
print(sumeven)
print(sumprime)
#question4
print (sum)

a = {34, 56, 78, 90}
b = {78, 45, 90, 23}

c = a.union(b)
print("union", c)

d = a.intersection(b)
print("intersection", d)

e1 = a.difference(b)
print("a - b =", e1)

e2 = b.difference(a)
print("b - a =", e2)

if a.issubset(b):
    print("a is a subset of b")
else:
    print("a is not a subset of b")

if b.issuperset(a):
    print("b is a superset of a")
else:
    print("b is not a superset of a")

x = int(input("enter the score: "))
if x in a:
    print("yes, it was present and it is popped and updated set")
    a.remove(x)
    print(a)
else:
    print("it isn't present")
#question5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
sample_dict["location"] = sample_dict.pop("city")

print(sample_dict)

