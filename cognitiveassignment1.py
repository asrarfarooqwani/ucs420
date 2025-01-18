#asgn1.1
print("asrar")
print("asrar")
print("asrar")
#asgn2.1
ist=1
sec=2
third=3
sum=ist+sec+third
print("sum is ",sum)
#asgn2.2
str1="asrar"
str2="farooq"
str3="wani"
strR=str1+str2+str3
print("concatinated string is ",strR)
#asgn4.1
print("table of 7 ")
for i in range(1,11):
    print(7*i)

print("table of 9")
for i in range(1,11):
    print(9*i)
#asgn4.2
n=int(input("enter a number for which u want the table to be displayed "))
for i in range(1,11):
    print(n*i)
#asgn4.3
n=int(input("enter a number upto which u want to calculate sum "))
sum=0
for i in range(1,n+1):
    sum=sum+i

print(sum)
#asgn5.1
def max(a,b,c):
    if a>b and b>c:
        return a
    elif b>a and a>c:
      return b
    else:
      return c

ans=max(4,5,6)
print("max number is ",ans)    
#asgn5.2
n2=int(input("enter the number upto which u want to calculate the sum of multiplier of 7 and 9 "))
sum2=0
for i in range(1,n2+1):
    if i%7==0 and i%9==0:
        sum2=sum2+i

print(sum2)
#asgn5.3
sum3=0
def checkprime(a):
    if a<2:
        return 0
    if a==2:
        return 1
    for j in range(2,a-1):
        if a%j==0:
            return 0
    return 1

n3=int(input("enter the number upto which u want to calculate the sum of prime numbers "))
for i in range(1,n3+1):
    flag=checkprime(i)
    if flag==1:
        sum3=sum3+i

print(sum3)
#asgn6.1
sum4=0
def checkodd(a):
    if a%2==0:
        return 0
    return 1


n4=int(input("enter the number upto which u want to add odd number "))
for i in range(1,n4+1):
    flag2=checkodd(i)
    if flag2==1:
        sum4=sum4+i
print(sum4)
#asgn6.2
sum5=0
def checkprime(a):
    if a<2:
        return 0
    if a==2:
        return 1
    for j in range(2,a-1):
        if a%j==0:
            return 0
    return 1

n3=int(input("enter the number upto which u want to calculate the sum of prime numbers "))
for i in range(1,n3+1):
    flag=checkprime(i)
    if flag==1:
        sum5=sum5+i
print(sum5)




