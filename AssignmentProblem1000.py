
lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())

    lst.append(ele)

print("New list : ",lst)
Length= len(lst)

print("Input your target : ")
target = int(input())

for i in range(0,len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print([i,j])

### using function------------------------------------------------------------------------

def tworunningsum(lst,target):
    for i in range(0,len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return([i,j])

lst = [20, 25, 35, 55]

target = 60
print(tworunningsum(lst,target))
