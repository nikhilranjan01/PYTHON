list=[2,4,6,2,4,9,8,8,9]
k=len(list)
list.sort()
i=3
while i<k-1:
    if list[i]==list[i+1]:
        i+=2
    else:
        print(list[i])
        break
    if(i==k-1):
        print(list[i])
