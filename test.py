A = [{'name': 'tom', 'age': 8}, {'name': 'jim', 'age': 18}, {'name': 'wang', 'age': 16}]
age = []  # 提取年龄
for i in range(len(A)):
    age.append(A[i]['age'])
sortage = []  # 排序年龄
for i in range(len(A)):
    sortage.append(min(age))
    age.remove(min(age))
B = []  # 按照年龄去提取字典整体数据放到B数组
for i in range(len(A)):
    for j in range(len(A)):
        if sortage[i] == A[j]['age']:
            B.append(A[j])
print(B)
