
a=input("menu:\n1.namber**3\n2.ip\n3.dns\n4.dwd\n")
if(a=="1"):
    print(int(input("enter a number:"))**3)
elif(a=="2"):
    list=[]
    list.append(input("enter ip: "))
    list.append(input("enter ip: "))
    list.append(input("enter ip: "))
    list.append(input("enter ip: "))
    print("the ip:\n " + str(list))
elif(a=="3"):
    dict={}
    dict.update({input("enter URL:"):input("enter IP:")})
    dict.update({input("enter URL:"): input("enter IP:")})
    dict.update({input("enter URL:"): input("enter IP:")})
    dict.update({input("enter URL:"): input("enter IP:")})
    print("the DNS is:\n" + str(dict))
elif(a=="4"):
    word=input("enter a word:")
    if(word==word[::-1]):
        print("is polindrom")
    else:
        print("isnt polindrom")
else:
    print("enter 1-4 only!!!!")