'''km=1

cm=km*100000
print("1 km is equal to  100000cm: ",cm)

l=int(input("enter the length of rectangle:"))
b=int(input("enter the breath oof rectangle:"))

a=l*b

p=2*(l*b)

print("area of rectangle :",a)
print("area of permeter  :",b)
'''
'''n=int(input("enter the number of rows:"))
for i in range(n,0,-1):
    for i in range(0,i):
        print("*",end=" ")


    print()
'''
'''year=int(input("enter the year u want:"))
if year%4==0 and  year%400==0:
    print("given year is leap year")
else:

    print("given yera are not")
        
'''
'''sum=0
for i in range(0,12,2):
    print(i)
    sum=sum+i
print("sum of number:", sum)

'''
'''n=int(input("enter the numbber:"))
for i in range(2,n+1):
    if n%i==0:
        break

    if i==n:
        print("number is prime")

    else:
        print("number is non prime")
'''






'''n=int(input("enter the  the number " ))

if n%3==0:
    print("number is divisible by 3")
elif n%5==0:
    print("number is divisible by 5")

else:
    print("you enter the wromg number")
   '''









'''a=int(input("enter  the number a:"))
b=int(input("enter the number b:"))

a,b=b,a


print("after the swapping of number a becomes",a)
print("after the swapping number of b becomes",b)
  '''



'''i=1
while(i<=10):
    print(i)
   i+=1
'''


'''




# speed=distance/time
#1 meter =1/1000km
# 1 sec=1/3600 hr

distance=int(input("enter the distance of car in m:"))
D=distance/1000
time=int(input("enter the  time in s: "))
T=time/3600
speed=D/T
print("speed of car in km/hr:",speed)



'''












a=int(input("enter the Distance between Jaunpur to Mumbai in km:"))

b=a*1000
print("Distance between Jaunpur and Mumbai in meter:",b)

c=a*100000 
print("Distance between Jaunpur and Mumbai in centimeter:",c)

d=a* 0.621371192
print(" Distance between Jaunpur and Mumbai in miles",d)









