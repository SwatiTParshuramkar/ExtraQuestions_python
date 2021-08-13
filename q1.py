list1 = [6,2,3,8,10]
i = 0
while i<len(list1):
    j = 0
    while j<len(list1)-1:
        if list1[j+1] < list1[j]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
        j += 1
    i += 1
print(list1)

min = list1[0]
max = list1[-1]
index = min
count = 0
while index < max :
    if index not in list1 :
        count = count + 1
    index+=1
print(count)