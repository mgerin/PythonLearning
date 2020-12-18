# Defining a string on multiple lines, using triple quotes and the line continuation character ( \ )
my_string = '''this\
is\
my\
first\
string'''

# Strings - indexing
a = "Cisco Switch"

a.index("i")

# Strings - character count
a = "Cisco Switch"

a.count("i")

# Strings - finding a character
a = "Cisco Switch"

a.find("sco")

# Strings - converting the case
a = "Cisco Switch"

a.lower()  # lowercase

a.upper()  # uppercase

# Strings - checking whether the string starts with a character
a = "Cisco Switch"

a.startswith("C")

# Strings - checking whether the string ends with a character
a = "Cisco Switch"

a.endswith("h")

# Strings - removing a character from the beginning and the end of a string
a = "   Cisco Switch   "

a.strip()  # remove whitespaces

b = "$$$Cisco Switch$$$"

b.strip("$")  # remove a certain character

# Strings - removing all occurences of a character from a string
a = "   Cisco Switch   "

a.replace(" ", "")  # replace each space character with the absence of any character

# Strings - splitting a string by specifying a delimiter; the result is a list
a = "Cisco,Juniper,HP,Avaya,Nortel"  # the delimiter is a comma

a.split(",")

# Strings - inserting a character in between every two characters of the string / joining the characters by using a delimiter
a = "Cisco Switch"

"_".join(a)

# Additional methods (source: https://www.tutorialspoint.com/python3/python_strings.htm)

capitalize()
# Capitalizes first letter of string.

lstrip()
# Removes all leading whitespace in string.

rstrip()
# Removes all trailing whitespace of string.

swapcase()
# Inverts case for all letters in string.

title()
# Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

isalnum()
# Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

isalpha()
# Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

isdigit()
# Returns true if string contains only digits and false otherwise.

islower()
# Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.

isnumeric()
# Returns true if a unicode string contains only numeric characters and false otherwise.

isspace()
# Returns true if string contains only whitespace characters and false otherwise.

istitle()
# Returns true if string is properly "titlecased" and false otherwise.

isupper()
# Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

# Strings - concatenating two or more strings
a = "Cisco"
b = "2691"

a + b

# Strings - repetition / multiplying a string
a = "Cisco"

a * 3

# Strings - checking if a character is or is not part of a string
a = "Cisco"

"o" in a

"b" not in a

# Strings - formatting v1
"Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4)

# Strings - formatting v2
"Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)
"Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)

# Strings - formatting v3 (f-strings)
a = "2600XM"
b = 2
c = 12.4
f"Cisco model: {a}, {b} WAN slots, IOS {c}"

# Strings - slicing
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

string1[
5:15]  # slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
string1[5:]  # slice starting at index 5 up to the end of the string
string1[:10]  # slice starting at the beginning of the string up to, but NOT including, index 10
string1[:]  # returns the entire string
string1[-1]  # returns the last character in the string
string1[-2]  # returns the second to last character in the string
string1[-9:-1]  # extracts a certain substring using negative indexes
string1[-5:]  # returns the last 5 characters in the string
string1[:-5]  # returns the string minus its last 5 characters
string1[::2]  # adds a third element called step; skips every second character of the string
string1[::-1]  # returns string1's elements in reverse order

# Lists
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]  # creating a list

len(list)  # returns the number of elements in the list

list1[0]  # returns "Cisco" which is the first element in the list (index 0)

list1[0] = "HP"  # replacing the first element in the list with another value

# Lists - methods
list2 = [-11, 2, 12]

min(list2)  # returns the smallest element (value) in the list

max(list2)  # returns the largest element (value) in the list

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

list1.append(100)  # appending a new element to the list

del list1[4]  # removing an element from the list by index

list1.pop(0)  # removing an element from the list by index

list1.remove("HP")  # removing an element from the list by value

list1.insert(2, "Nortel")  # inserting an element at a particular index

list1.extend(list2)  # appending a list to another list

list1.index(-11)  # returns the index of element -11

list1.count(10)  # returns the number of times element 10 is in the list

list2 = [9, 99, 999, 1, 25, 500]

list2.sort()  # sorts the list elements in ascending order; modifies the list in place

list2.reverse()  # reverses the elements of the list

sorted(list2)  # sorts the elements of a list in ascending order and creates a new list at the same time

sorted(list2, reverse=True)  # sorts the elements of a list in descending order and creates a new list at the same time

list1 + list2  # concatenating two lists

list1 * 3  # repetition of a list

# Lists - slicing (works the same as string slicing, but with list elements instead of string characters)
a_list[
5:15]  # slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
a_list[5:]  # slice starting at index 5 up to the end of the list
a_list[:10]  # slice starting at the beginning of the list up to, but NOT including, index 10
a_list[:]  # returns the entire list
a_list[-1]  # returns the last element in the list
a_list[-2]  # returns the second to last element in the list
a_list[-9:-1]  # extracts a certain sublist using negative indexes
a_list[-5:]  # returns the last 5 elements in the list
a_list[:-5]  # returns the list minus its last 5 elements
a_list[::2]  # adds a third element called step; skips every second element of the list
a_list[::-1]  # returns a_list's elements in reverse order