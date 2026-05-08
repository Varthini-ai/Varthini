a=int(input("enter the tamil mark:"))
b=int(input("enter the english mark:"))
c=int(input("enter the cs mark:"))
d=int(input("enter the physics:"))
total=a+b+c+d
print("the total mark is:",total)
per=(total/400)*100
print("the aggregate of the student is:",per)
if(per>=75):
    print("the grade is distinction")
elif(per>=60 and per<75):
    print("the grade is first division")
elif(per>=50 and per<60):
    print("the grade is second division")
elif(per>=40 and per<50):
    print("the grade is third division")
else:
    print("fail")
