'''Oliver Atkinson'''
name = str(input("What is your name"))
if name == "":
    print("error")
    str(input("What is your name"))
for i in range(0,len(name),2):
    print(name[i+1],end=' ')
