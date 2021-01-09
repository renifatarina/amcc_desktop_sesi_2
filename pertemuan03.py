list1=[1,2,3,4,5,6,7,8,9]

#print dari list1 pada index
print(list1[2])
print(list1[-3])
print(list1[1:5])
print(list1[1:])
print(list1[:5])

list1[8]=10
print(list1)

del list1[8]
print(list1)

list1.clear()
print(list1)

list1.append("Dekstop")
print(list1)

list1.extend(["Programming","AMCC",2020,2021])
print(list1)

my_tuple=('Hallo sayang')
print(my_tuple[1])
print(my_tuple[:5])
print(my_tuple[6:])

my_tuple=(1,2,3,[6,5])
print(my_tuple[3][0])

my_tuple=(5,6,7)
print(my_tuple)

#del my_tuple
#print(my_tuple)

my_tuple=('Halo sayang')
print(my_tuple.index('s'))

list2=[1,2,3,4,5]
set1=set(list2)
set2={1,2,3,4,5}
print(list2)
print(set1)
print(set2)

set2.add(6)
print(set2)

set2.update([6,7,8,9])
print(set2)

set2.discard(7)
set2.discard(7)
print(set2)

#bakal error pas diprint
#set2.remove(8)
#set2.remove(8)
#print(set2)

set2.clear()
print(set2)

set3={10,11,12,13,14,15}
set4={21,22,23,24,25,10}

print(set3|set4)
print("atau")
print(set3.union(set4))

dict1={1:"Salsabila",2:"Klaten",3:19}
print("Hai namaku", dict1[1])
print("Asalku dari", dict1.get(2))

dict1[4]="Informatika"
print("Aku dari jurusan", dict1[4])
print(dict1)

del dict1[3]
print(dict1)