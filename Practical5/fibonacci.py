#set the first and second places
n1=1
n2=1
#add n1 and n2
#give the value of n2 to n1 and give the value of n3 to n2
#repeat this process by "for" and "i=i+1"
for i in range (3,14):
        n3=n1+n2
        n1=n2
        n2=n3
        i=i+1
print n3
