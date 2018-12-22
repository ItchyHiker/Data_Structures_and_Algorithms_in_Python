
list_of_list = []
for i in range(10):
    sub_list = []
    for j in range(10):
        sub_list.append(j)
    list_of_list.append(sub_list)

result = sum(sum(x) for x in list_of_list)
print(result)

