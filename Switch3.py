
```python
import getpass
import sys
import telnetlib
import time

Host="10.10.2.251"

user=raw_input(' Enter User name: ')
password=getpass.getpass()

tn = telnetlib.Telnet(Host)
tn.read_until(b'Username: ')
tn.write(user.encode('ascii') + b'\n')

if password:
    tn.read_until(b'Password: ')
    tn.write(password.encode('ascii')+b'\n')

time.sleep(2)
tn.write(b'enable\n')
time.sleep(2)
tn.write(b'cisco\n')
time.sleep(2)
tn.write(b'config t\n')
time.sleep(2)

tn.write(b'interface g0/0\n')
time.sleep(2)
tn.write(b'switchport trunk encapsulation dot1q\n')
time.sleep(2)
tn.write(b'switchport mode trunk\n')
time.sleep(2)
tn.write(b'exit\n')
time.sleep(2)


tn.write(b'interface g0/1\n')
time.sleep(2)
tn.write(b'switchport mode access\n')
time.sleep(2)
tn.write(b'switchport access vlan 10\n')
time.sleep(2)
tn.write(b'exit\n')
time.sleep(2)

tn.write(b'vtp mode client\n')
time.sleep(2)
tn.write(b'vtp domain morti\n')
time.sleep(2)
tn.write(b'vtp password cisco\n')
time.sleep(2)

tn.write(b'end\n')
tn.write(b'exit\n')
line=tn.read_all()
print (line)

```
