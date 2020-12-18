list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

print(len(list1))
print(list1[1])
print(list1[-2])
list1[2] = "HP"
print(list1)

list2 = [-11, 12, 2]
print(min(list2))
print(max(list2))

list3 = ["a", "b", "c"]
print(min(list3))
print(max(list3))
#print(min(list1)) - this will throw an error: TypeError: '<' not supported between instances of 'int' and 'str'
list1.append(1000)
print(list1)

del list1[4]
print(list1)
print(list1.pop(0))
print(list1)
list1.remove("Juniper")
print(list1)
list1.insert(2, "Nortel")
print(list1)
list1.extend(list2)
print(list1)
print(list1.index(-11))
list1.append(10)
print(list1)
print(list1.count(10))

list2.append(10)
list2.append(25)
list2.append(5000)
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)
print(sorted(list2))
list2.sort()
print(list2)
print(sorted(list2, reverse=True))
print(list1 + list2)
print(list2 * 3)