'''List
touple
set
dictinary'''

#List
'''a=2
list_a=[a,"VENKY"]
print(type(list_a))
print(len(list_a))
print(list_a[0:2])'''

'''a=3
list_a = [5, "Six", a, 8.2]
print(list_a)
print(list_a[0:4])
for i in list_a:
    print(i)'''

'''a=6
list_a = [5, "Six", a, 8.2]
list_b = [2, list_a]
print(list_b)
print(list_a + list_b)'''

'''for i in range(1,4):
    list_a+=[i]'''

'''a=[123,50,890,50]
a.append(4)
print(a)
a.insert(1,"venky")
a.extend([6,7,"edmond"])
a=a*2
a.remove(50)
a.pop(1)
#a.clear()
a.count(50)
#a.sort()
print(a.count(50))
print(a)'''

'''a=[23,54,72,90]
a.append(60)
print(a)
a.remove(54)
print(a)
print(a[2])
print(a)'''

#Touple

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

#Set

'''a={20,70,60,40,20}
print(a)
b=[45,67,89]
print(set(b))
c="lives in edmond"
print(set(c))
#print(a[2])
a.add(99)
print(a)
a.discard(70)
print(a)
a.discard(7)
print(a)'''


'''a=("edmond","okc","city")
print(a[2])
for i in a:
    print(i)
print(len(a))
print(a[::-1])
#print(tuple(reversed(a)))'''

a= list(map(int, input("Enter a: ").split()))
#a=[20,45,65,70,98]
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
        print((i),end=" ")
print()
b=sorted(a)
print(b)


#dictinary

'''dict_a = {
  "name": "Teja",
  "age": 15 
  }
print(dict_a)
print(dict_a["name"])
print(dict_a["age"])
dict_a["place"]="Hyd"
print(dict_a)
dict_a["thing"]="book"
print(dict_a)
dict_a["thing"]="pen"
print(dict_a)
dict_a["age"]="25"
print(dict_a)
del dict_a["thing"]
print(dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())
print(list(dict_a.keys()))
#dict_a.popitem()
#print(dict_a)
#for key in reversed(dict_a):
 #   print(key,dict_a[key])
b=reversed(dict_a)
print(b)'''






