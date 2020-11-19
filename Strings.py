a = "Cisco Switch"
print(a.index("i"))
print(a.count("i"))
print(a.find("sco"))
print(a.find("xyz"))
print(a.lower())
print(a.upper())
print(a.startswith("i"))
print(a.startswith("C"))
print(a.endswith("h"))

b = "    Cisco Switch   "
print(b.strip())

c = "$$$Cisco Switch$$$"
print(c.strip("$"))

print(b.replace(" ", ""))

d = "Cisco,Juniper,HP"
print(d.split(","))

print("_".join(a))

a = "Cisco"
b = " Switch"
print(a + b)
print(a * 3)
print("o" in a)
print("b" in a)
print("b" not in a)

sisco = "Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
print(sisco)
sisco = "Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4)
print(sisco)
sisco = "Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4)
print(sisco)

#option 2
sisco = "Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
print(sisco)
sisco = "Cisco model: {2}, {0} WAN slots, IOS {1}".format("2600XM", 2, 12.4)
print(sisco)

#option 3 - f strings
model = "2700XM"
slots = 4
ios = 12.3

sisco = f"Cisco model: {model}, {slots} WAN slots, IOS {ios}"
print(sisco)
sisco = f"Cisco model: {model}, {slots * 2} WAN slots, IOS {ios}"
print(sisco)
sisco = f"Cisco model: {model.lower()}, {slots * 2} WAN slots, IOS {ios}"
print(sisco)

#string slices
string1 = sisco
print(string1[6: 11])
print(string1[6:])
print(string1[:11])
print(string1[-1:])
print(string1[:-1])
print(string1)
