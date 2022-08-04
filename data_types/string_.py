#a="hello python"
b=("hello world")
c=("my self aswini")
#print(a)
#print(type(a))
#print(dir(b))
#print(a.capitalize())      Hello python
#print(b.capitalize())      Hello world
a="HELLO WORLD"
#print(a.casefold())         hello world
#print(a.center("hai","fly")) 
#center 
#aswini="telugu for telugu"
#new_string=aswini
#print("after hello:", new_string)     after hello: telugu for telugu
aa="how are you"
a1=aa
#print("i am fine:",a1)    #i am fine: how are you
#count  #Return the number of (non-overlapping) occurrences of substring sub in string
b1="telugu for english"
#print(b1.count("telugu"))   result =1

#encode
#print(b1.encode())
#enswith  Returns True if a string ends with the given suffix otherwise returns False
#print(b1.endswith('telugu')) False
#print(b1.endswith('english')) True
#expandtabs Expand tabs in a string replacing them by one or more spaces
a3="i\love\youuuuu"
print("welcome:",end="    ")
print(a3.expandtabs())
print("\t")
#find
r1="welcome to home"
#result=r1.find('to')
#print("substring'welcome'found at index:", result)
print(r1.find('w',3,5))
#formate
print("{},A computer for english." .format("python"))
print("A computer for english {}" .format("haiiii"))
