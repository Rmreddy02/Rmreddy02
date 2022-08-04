data={"name":"aswini","age":25,"college name":"Au","DOB":"04-12-1994"}
data2={"name":["sai","aswini","1234,5"],"age":25,"college name":"Au","DOB":"04-12-1994"}
# print(data)
# print(type(data))
# print(dir(data))
#get method
print(data.get("DOB"))
print(data["DOB"])
# print(data.keys())
# print(data.values())
# print(data.items())
# data.update(data2)
#setdefault
print(data.setdefault("sal",22000))
print(data.setdefault("age",29))
print("16--",data)
print(data.keys())
print(data.values())
#update method
data.update(data2)