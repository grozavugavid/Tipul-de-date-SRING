s=str(input("Introduceti un nume si un prenume:"))
a,b=s.split()
print(a)
print(b)
if(a.title()==a) and (b.title()==b):
    print("Numele introdus este corect")
else:
    print("Numele introdus este gresit")