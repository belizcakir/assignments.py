
#identity Operator : is

x = y = [1,2,3,4]
z = [1,2,3,4]

print(x==y)
print(x==z)

# print(x is z) #içerikli olsa bile adresleri farklı
# print(x is y)

# membership Operator : in 

a = ["python","javascript"]

print("python2" in a) #çünkü python2 listede yok

email= "deneme.gmail.com"


print("@" in email)