#  An array of distinct non-negative integers.
# Ex. - statues = [6,2,3,8], the output shouls be, make array consecutive2(statues) = 3.
#  needs statues of sizes 4, 5, and 7.
#  ex. - input : [6,3], output : 2

# list1 = [2,3,6,8,7,1]
# i = 0
# while i<len(list1):
#     j = 0
#     while j<len(list1)-1:
#         if list1[j+1] < list1[j]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
#         j += 1
#     i += 1
# print(list1)

# list1 = [2,3,6,8,10]
# min = list1[0]
# max = list1[0]
# index = 0
# diff= 0
# while index < len(list1)-1 :
#     if (list1[index] < min) :
#         min = list1[index]
#     if (list1[index] > max) :
#         max = list1[index]
        
#     index=index+1
# diff = max - min -1
# print(diff)



list1 = [6,2,3,8,10]
i = 0
while i<len(list1):
    j = 0
    while j<len(list1)-1:
        if list1[j+1] < list1[j]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
        j += 1
    i += 1
# print(list1)

min = list1[0]
max = list1[-1]
index = min
count = 0
while index < max :
    if index not in list1 :
        count = count + 1
    index+=1
print(count)