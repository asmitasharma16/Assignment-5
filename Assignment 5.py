print("*****************************DECISION AND FLOW CONTROL*****************************")
#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter year "))
if((year%100!=0 and year%4==0 )or year%400==0):
    print("Leap year")
else:
    print("Not a leap year")

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length=int(input("enter length "))
breadth=int(input("enter breadth "))
if(length==breadth):
    print("dimensions are of square")
else:
        print("dimensions are of rectangle")

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
age1=int(input("enter age of 1st person "))
age2=int(input("enter age of 2nd person "))
age3=int(input("enter age of 3rd person "))
oldest=-1
youngest=100
print("age of oldest person",end=" ")
if(age1>age2):
         if(age1>age3):
            oldest=age1
         else:
             oldest=age3
elif(age1<age2):
         if(age2>age3):
             oldest=age2
         else:
             oldest=age3
print(oldest)
print("age of youngest person",end=" ")
if(age1<age2):
         if(age1<age3):
            youngest=age1
         else:
             youngest=age3
elif(age1>age2):
         if(age2<age3):
             youngest=age2
         else:
             youngest=age3
print(youngest)

#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 
'''
1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR".
'''
age=int(input("enter age of person "))
sex=input("sex M or F ")
status=input("Marital status y or N ")
if(sex=='F' or sex=='f'):
    print("employee will work only in urban area")
elif((sex=='M' or sex=='m')):
      if(age>=20 and age<40):
          print("Employee can work anywhere")
      elif(age>=40 and age<=60):
        print("Employee will work in urban area only")
      else:
            print("ERROR")
else:
    print("ERROR")

#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.             
n=int(input("Enter the quantity of item "))
cost=int(input("Enter cost of item "))
totalcost=n*cost
if(totalcost>1000):
     print("10% discount applied ")
     totalcost=totalcost-(0.1*totalcost)
print("Total cost ",totalcost)

print("*****************************LOOPS*****************************")

#Q.1- Take 10 integers from user and print it on screen.
integer = [ ]
print('Enter 10 integers')
for i in range(0,10):
    b=int(input("enter integer "))
    integer.append(b)

    
for i in range(0,10):
    print(integer[i])
 
#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.

p='python'
while(True):
    print(p)

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
n=int(input("Enter range of list to make list of integers "))
l1=[]
l2=[]
for i in range (n):
    b=int(input())
    l1.append(b)
print(l1)
for i in range(n):
    a=l1[i]
    l2.append(a*a)
print(l2)

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
n=int(input("Enter range of list to make list containing ints, strings and floats"))
a=[]
ls=[]
lf=[]
li=[]
for j in range (n):
    b=input()
    a.append(b)
print(a)    
for j in range (n):
    if a[j].isdigit():
        i=a[j]
        li.append(i)           
    elif a[j].isalpha():
        s=a[j]
        ls.append(s)
    else:
        f=a[j]
        lf.append(f)
print('List containing integers',li)
print('List containing strings',ls)
print('List containing floats',lf)

#Q.5- Using range(1,101), make a list containing only prime numbers.
l=[ ]
for n in range (1,101):
    prime=True
    for i in range(2,n):
        if(n%i==0):
            prime=False
    if prime:
        l.append(n)
print('list containing prime numbers ',l)        


#Q.6- Print the following patterns:
'''
* 
** 
***
****
'''
for i in range (4):
    for j in range (i+1):
        print('*',end='')
    # ending line after each row using \r    
    print('\r')

#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop. 
n=int(input("Enter range of list"))
l1=[]
for i in range (n):
    b=int(input())
    l1.append(b)
num=int(input("Enter a number to search in list "))
for i in range (n):
    if(l1[i]==num):
        l1.remove(l1[i])
        break;
print(l1)
    


 
              
          

         
         
