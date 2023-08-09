my_string = 'You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP'
import re

a = re.match('You', my_string)
a = re.match('you', my_string)
type(a)
a = re.match('You', my_string)
a.group()
a = re.match('you', my_string, re.I)
a.group()
a = re.fullmatch('You', my_string)
a = re.match('Python3', my_string)
b = re.search('You', my_string)
b.group()
b = re.search('Python3', my_string)

arp = '22.22.22.1   0   b4:a9:5a:ff:c8:45 VLAN#222     L'
a = re.search(r'(.+?) +(\d) +(.+?)\s{2,}(\w)*', arp)
a.group(1)
a.group(2)
a.group(3)
a.group()

b = re.findall(r'\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}',arp)
print(b)
c = re.findall(r'(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})',arp)
print(c)
d = re.sub(r'\d', '7', arp)
print(d)