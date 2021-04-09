a=120102
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
if d>e:
        print("d is greater")
else:
        print("e is greater")
X=True
Y=True
Z= (X and not Y) or (Y and not X)
print(Z==True)
W=X!=Y
print(W==Z)
