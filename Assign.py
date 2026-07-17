'''a=input()
last_letter= a[-1]
if last_letter == "n" and "N":
    print("Ends with n")
else:
    print("Does not end with n")

a=input()
if " " in a:
    print("multiple words")
else:
    print("single word")


a=input()
length=len(a)
if len(a)%2!=0:
    print("middle character")
else:
    print("even length word")

a=int(input())
if a>=500:
    print("give 10% discount")
else:
    print("no discount")


a=int(input())
if a>=500:
    discount=a*10/100
    final_amount= a-discount
    print(final_amount)
else:
    print("no discount")'''

'''ch=input()
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("Vowel")
else:
    print("consonant")'''

'''username=input()
if username=="Admin":
    print("welcome Admin")
else:
    print("Unknown User")'''


'''Temp=int(input())
if Temp>35:
    print("very hot")
elif Temp>=25 and Temp<=35:
        print("pleasant")
else:
      print("cool")'''


'''a=input()
ch=input()
count=a.count(ch)
print(count)'''

'''a=input()
if len(a)<3:
    print(a)
else:
    print("First 3 characters", a[0:3:])
    print("Last 3 characters", a[-3:])'''

'''x=int(input())
x+=5
print(x)
x-=3
print(x)'''

'''a=" Sneha "
print(a.strip(" "))
print(a.startswith("S"))
print(a.endswith("a"))
print(a.upper())
print(a.lower())
print(a.replace("a","@")) 

b=" 9876543210 "
print(b.isdigit)
print(b.strip(" "))
print(b.startswith("9"))
print(b.endswith("0"))
print(b.replace("9","8"))'''

'''a="09-07-2026"
print(a.replace("-","/"))
print(a.startswith("09"))
print(a.endswith("2026"))

b="P-y-t-h-o-n"
print(b[0::2])'''

#List
'''a=[12,25,18,40,25,60,75]
print(a[0])
print(a[-1])
#print(a.append(90))
a.append(90)
print(a)
a.insert(3,30)
print(a)
#a.remove(25)
#print(a)
print(a.pop(4))
print(a.count(25))
print(a[2:5])
a.sort()
print(a)
#Find the index of 60.
b=a.index(60)
print(b)'''

'''a=(7,29,44,56,76)
a[2]
print(a[2])
print(a[2:5])
b=(54,75,89,99)
print(a+b)
print((a+b)*2)
print(44 in a)
print(89 in b)
for i in a:
    print(i)
a=a+(80,)
print(a)'''

#Touple
'''a=(12,25,18,40,25,60,75)
print(a[0])
print(a[-1])
a=a+(90,)
print(a)
print(25 in a)
print(99 in a)
print(a*2)'''

'''a=(12,25,18,40,25,60,75)
print(a)
print(a[0])
print(a[-1])
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(a[::-1])
for i in a:
    if i%2==0:
        print((i),end=" ")'''

a={12,25,18,40,25,60,75}
print(a)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
a.add(86)
print(a)
a.discard(86)
print(a)
for i in a:
    if i%2==0:
        print((i), end=" ")

















      
      





