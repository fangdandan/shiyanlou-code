a = 100;
for i in range(a+1) :   
    if(i%7==0):    
        continue
    elif(i%10==7): 
        continue
    elif(i//10==7):   
        continue
    else:
        print('{}\n'.format(i))
