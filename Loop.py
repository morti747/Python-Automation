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

