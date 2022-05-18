d = int(input("Enter a number :"))
b = 1
a = 0
c = 0
while c <= d:
  c=a+b
  if c<=d:
    a=b
    b=c
    print (c)
  c += 1
