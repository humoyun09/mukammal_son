#Mukammal son
a=6
s=0 

for i in range(1,a):
    if a % i == 0:
        s = s + i;

if s == a:
    print("true")
else:
    print("fale")