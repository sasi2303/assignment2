divby3=[]
print("ODD NUMBERS ARE:")
for i in range(50):
    if(i%2!=0):
      print(i,end=' ')
      if(i%3==0):
        divby3.append(i)
print("\n ODD NUMBERS THAT DIVIDE BY 3 :",divby3)
