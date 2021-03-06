# Python-Automation
How to configure our network using python scripts.





:star: in this topology, we have a 2 floor appartment with different components, we are going to configure our instruments using python scripts. 
##

![image](images/1.PNG)

##

##
:star: First let's our computer's NIC and IP address: 

```
nano /etc/network/interfaces
```

##
![image](images/2.1.PNG)
##

##
:star: Now let's check connectivity between this computer and the router using : 

```
telnet 10.10.1.254
```

##
![image](images/2.2.PNG)
##

##
:star: Now let's check connectivity between this computer and the internet : 

```
ping cisco.com
```

##
![image](images/2.3.PNG)
##

 


:star: Step 1: Router configuration 

As you can see there's no connection between our inside local network and the internet. so we are using this python script to configure our router, to create several sub-interfaces on the router and tell it to which VLAN they belong to, to create the DHCP pool for these VLANs and to configure NAT, so our users could have access to the internet.
##
:star: You can see all scripts that we'r going to use for this project using ls command:

##
``
ls
``
##
![image](images/2.PNG)
##

##
##

And the script ' router.py` is the only script that we'll use to configure our router using the following command: 

```
python Router.py    
```
```
(python + our script's name)
```

``` python 

import getpass
import sys
import telnetlib
import time

Host="10.10.1.254"

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
tn.write(b'hostname Morti-R\n')
time.sleep(2)



tn.write(b'interface g0/0\n')
time.sleep(2)
tn.write(b'ip nat outside\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'interface g0/1\n')
time.sleep(2)
tn.write(b'no shutdown\n')
time.sleep(2)
tn.write(b'ip nat inside\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'interface g0/1.10\n')
time.sleep(2)
tn.write(b'encapsulation dot1Q 10\n')
time.sleep(2)
tn.write(b'ip address 192.168.10.254 255.255.255.0\n')
time.sleep(2)
tn.write(b'ip nat inside\n')
time.sleep(2)
tn.write(b'no shutdown\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'interface g0/1.20\n')
time.sleep(2)
tn.write(b'encapsulation dot1Q 20\n')
time.sleep(2)
tn.write(b'ip address 192.168.20.254 255.255.255.0\n')
time.sleep(2)
tn.write(b'ip nat inside\n')
time.sleep(2)
tn.write(b'no shutdown\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'interface g0/1.30\n')
time.sleep(2)
tn.write(b'encapsulation dot1Q 30\n')
time.sleep(2)
tn.write(b'ip address 192.168.30.254 255.255.255.0\n')
time.sleep(2)
tn.write(b'ip nat inside\n')
time.sleep(2)
tn.write(b'no shutdown\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'interface g0/1.40\n')
time.sleep(2)
tn.write(b'encapsulation dot1Q 40\n')
time.sleep(2)
tn.write(b'ip address 192.168.40.254 255.255.255.0\n')
time.sleep(2)
tn.write(b'ip nat inside\n')
time.sleep(2)
tn.write(b'no shutdown\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'interface g0/1.50\n')
time.sleep(2)
tn.write(b'encapsulation dot1Q 50\n')
time.sleep(2)
tn.write(b'ip address 192.168.50.254 255.255.255.0\n')
time.sleep(2)
tn.write(b'ip nat inside\n')
time.sleep(2)
tn.write(b'no shutdown\n')
time.sleep(2)

tn.write(b'interface g0/3\n')
time.sleep(2)
tn.write(b'ip nat inside\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'interface g0/2\n')
time.sleep(2)
tn.write(b'ip nat inside\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'access-list 1 permit any\n')
time.sleep(2)
tn.write(b'ip nat inside source list 1 interface g0/0 overload\n')
time.sleep(2)
tn.write(b'ip domain lookup\n')
time.sleep(2)
tn.write(b'ip name-server 192.168.122.1\n')
time.sleep(2)

tn.write(b'ip dhcp pool servers\n')
time.sleep(2)
tn.write(b'network 10.10.3.0 255.255.255.0\n')
time.sleep(2)
tn.write(b'default-router 10.10.3.254\n')
time.sleep(2)
tn.write(b'dns-server 8.8.8.8\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'ip dhcp pool vlan2\n')
time.sleep(2)
tn.write(b'network 192.168.10.0 255.255.255.0\n')
time.sleep(2)
tn.write(b'default-router 192.168.10.254\n')
time.sleep(2)
tn.write(b'dns-server 8.8.8.8\n')
tn.write(b'exit\n')

tn.write(b'ip dhcp pool vlan3\n')
time.sleep(2)
tn.write(b'network 192.168.20.0 255.255.255.0\n')
time.sleep(2)
tn.write(b'default-router 192.168.20.254\n')
time.sleep(2)
tn.write(b'dns-server 8.8.8.8\n')
tn.write(b'exit\n')

tn.write(b'ip dhcp pool vlan4\n')
time.sleep(2)
tn.write(b'network 192.168.20.0 255.255.255.0\n')
time.sleep(2)
tn.write(b'default-router 192.168.20.254\n')
time.sleep(2)
tn.write(b'dns-server 8.8.8.8\n')
tn.write(b'exit\n')

tn.write(b'ip dhcp pool vlan5\n')
time.sleep(2)
tn.write(b'network 192.168.30.0 255.255.255.0\n')
time.sleep(2)
tn.write(b'default-router 192.168.30.254\n')
time.sleep(2)
tn.write(b'dns-server 8.8.8.8\n')
time.sleep(2)
tn.write(b'exit\n')

tn.write(b'end\n')
tn.write(b'exit\n')
line=tn.read_all()
print (line)

```

Let's check this script first in our computer using: 

```
nano Router.py

```
##
![image](images/3.PNG)
##

:star: So let's run it:


##
![image](images/4.PNG)
##
##
![image](images/5.PNG)
##

##
:star: Now you can see that this user can reach the cisco.com, which means that we have access to internet.

##

##

![image](images/7.PNG)
##



Now let's start configuration of our switchs. in this topology, we are using VTP to create our VLANs just in switch 1 with server mode, and we'll create all VLANs called (guest, users and servers) using the following scripts. but remember that we shoudl first configure our VLAN's interface the way that we can reach it remotely. 



##
![image](images/8.PNG)
##

##
![image](images/9.PNG)
##

##
![image](images/10.PNG)
##

:star: Now we can check one more time if we can reach the www.cisco.com & www.google.com or not: 

##
![image](images/11.1.PNG)
##


:star2: Let's check our connection with Switch1: 
##

##
![image](images/11.PNG)
##

Ok! 
let's run our script Switch1.py to configure our switch and create our VLANs using following script:  

```python

import getpass
import sys
import telnetlib
import time

Host="10.10.2.253"

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

tn.write(b'interface range g0/0-2\n')
time.sleep(2)
tn.write(b'switchport trunk encapsulation dot1q\n')
time.sleep(2)
tn.write(b'switchport mode trunk\n')
time.sleep(2)



tn.write(b'vlan 10\n')
time.sleep(2)
tn.write(b"name guest\n")
time.sleep(2)
tn.write(b'exit\n')
time.sleep(2)


tn.write(b'vlan 20\n')
time.sleep(2)
tn.write(b"name user\n")
time.sleep(2)
tn.write(b'exit\n')
time.sleep(2)



tn.write(b'vlan 30\n')
time.sleep(2)
tn.write(b"name servers\n")
time.sleep(2)
tn.write(b'exit\n')
time.sleep(2)

tn.write(b'vtp mode server\n')
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

###
???? this is the result of our python automation: 


##
![image](images/13.PNG)
##

???? there is another way to configue many VLANs using " Loop " feature, here we can use this script as well to create our VLANs and giving them the name according their VLAN number using the following scrip: 


```python 

import getpass
import sys
import telnetlib
import time

Host="10.10.2.253"

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

tn.write(b'interface range g0/0-2\n')
time.sleep(2)
tn.write(b'switchport trunk encapsulation dot1q\n')
time.sleep(2)
tn.write(b'switchport mode trunk\n')
time.sleep(2)


for n in range(2,8):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")


tn.write(b'vtp mode server\n')
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
##
We can also check our configuration using ```show run ``` command. But here I want to show you the status on our VTP using: 

```
show vtp status
```
to check our configuration. 

##
##
![image](images/16.PNG)
##

##
Ok! 
let's run our script Switch1.py to configure our switch and create our VLANs:

##

##
![image](images/14.PNG)
##

:star: 
Let's start configuration on our Switch 2, VTP mode on this switch is going to be the transparent mode, using the following script: 

```python
import getpass
import sys
import telnetlib
import time

Host="10.10.2.252"

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

tn.write(b'interface range g0/0-2\n')
time.sleep(2)
tn.write(b'switchport trunk encapsulation dot1q\n')
time.sleep(2)
tn.write(b'switchport mode trunk\n')
time.sleep(2)

tn.write(b'vtp mode transparent\n')
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

:Star: let's run this scrip: 

##
![image](images/15.PNG)
##

Let's check our status: 


##
![image](images/17.PNG)
##

So if it became part of our VTP domain, it should recieve all VLANs created in switch 1, so let's check it: 

```
show vlan
```


##
![image](images/18.PNG)
##

##
Now, switch3: mode client, and one interface in VLAN 10 to check our access to internet using browser on one of our end point computer: 

##
Let's run the following script: 
##

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


##
![image](images/19.PNG)
##


##
Let's check our VLANs & VTP status: 
##

##
![image](images/20.PNG)
##


##
![image](images/21.PNG)
##

And our access to the www.cisco.com: 

##
![image](images/22.PNG)
##

Now we turn on our Linux GUI  to recieve IP address in vlan 10, and we are going to check our connection to the internet: 

```
ifconfig
```

##
![image](images/23.PNG)
##

let's ping www.cisco.com :
##
![image](images/24.PNG)
##

And finally let's open our browser and open it's website: 

##
![image](images/25.PNG)
##

???? Thank you for following this project
