x = int(input("entert your km :"))
x = 0

result = 0
if (x >=5 and x <=50):
    result = 10
    print(result)
elif (x >=51 and x <=100):
    result = 15
    print(result)
elif (x >=101 and x <=300):
    result = 25
    print(result)
elif (x >=301 and x <=500):
    result = 35
    print(result)
elif (x >500):
    result = 45
    print(result)
else :
    print("free")

vat = result * 0.07
bath = result + result * 0.07
print("vat = ",vat)
print("km =",x)
print("bath =",bath)
