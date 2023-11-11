list1to10=[]
for i in range(0,10):
    i=i+1
    list1to10.append(i)
print(list1to10)
for i in list1to10:
    if(i%2==0):
     list1to10.remove(i)

print(list1to10)
     


   
