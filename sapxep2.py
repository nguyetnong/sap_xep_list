arr=[10, 4, 9,5,7,0,11]


for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]<arr[j]:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            
            
print(arr[-2: ])
        
        
        