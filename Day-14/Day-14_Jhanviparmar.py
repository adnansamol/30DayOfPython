#day14
n = int(input("Enter the size of list: "))
lst=[]
for i in range(0,n):
    lst.append(int(input("Enter number: ")))
print("List: ",lst)
for i in range(0,len(lst)-1):
    for j in range(0,n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print("Sorted list",lst)
