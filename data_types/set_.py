# # #set 
#data={1,2,3,4,5}
# # #print(type(data))
#print(dir(data))
# # #add method
# # #data.add(8)
# # #print(data)
# # #clear 
# # #data.clear()
# # #data2=data.copy()
# # #print(data2)
# # #print(data)
# # #difference method
# # fruits={"apple","banana","mango","sapota","jackfruit"}
# # company={"google","banana","apple"}
# # cmp1=fruits.difference(company)
# # cmp=company.difference(fruits)
# # print(cmp1)
# # print(cmp)
# # company.difference_update(fruits)
# # fruits.difference_update(company)
# # print(fruits)
# # print(company)
# # # data5={"apple","banana","mango"}
# # # print(data5)
# # # data5.discard("banana")
# # # print(data5)
# # # #intersection
# # # common=fruits.intersection(company)
# # # print(common)
# # # #union
# # # union_data=fruits.union(company)
# # # print(union_data)
# # # print(fruits|company)
# # #discard method
data1={"car","scooty","bus","petrol","van"}
data2={"car","charge","current","petrol"}
# # # data1.discard("scooty")
# # # print(data1)
# # # #intersection method
print(data1.intersection(data2))
# print(data2.intersection(data1))
# print(data2)
data1.intersection_update(data2)
# print(data2.intersection_update(data1))
print(data1)
# print(data2)

#data1={"social media","fb","apple","orange"}
#data2={"fb","amzon","dell","apple","orange"}
#print(data1.difference(data2))
#print(data2.difference(data1))
data1={"social media","fb","apple","orange"}
data2={"fb","amzon","dell","apple","orange"}
#data1.difference_update(data2)
'''
#remove and pop
print(data1)
data1.discard("social media")
print(data1)
# print(data2)               
# print(data2.pop())
# print(data2)  
''' 
'''#symmetric_difference
print(data1)
# print(data1.symmetric_difference(data2))    
data1.symmetric_difference_update(data2)
print(data1)
'''
