a=list(map(int,input("Enter the values: ").split()))
store={
    1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0
    
}

for i in range(1,10):
    for val in a:
        if val%i==0:
            store[i]+=1

print(store)