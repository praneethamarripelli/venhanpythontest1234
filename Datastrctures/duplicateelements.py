list = [1,2,3,4,5,6,1,2,6,9,9]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if(list[i]==list[j]):
            print(list[j])