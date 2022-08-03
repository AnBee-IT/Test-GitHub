# Liệt kê dữ liệu trong Set => lyLich
lyLich = {"Name" : "AnBee", "Age" : 24}
for key, value in lyLich.items():
	print(key, "=>", value)
print('\n')

# Liệt kê dữ liệu trong Set => thisSet
thisSet = {'apple', 'banana', 'cherry'}
for x in thisSet:
	print(x)
print('\n')


# Đếm số lượng phần tử xuất hiện trong mảng
A = [1, 3, 4, 6, 1, 1, 5, 3, 1, 9, 9, 1]
count = 0
print('A =', A)
for giaTri in A:
	if giaTri == 3:
		count = count + 1
print('Tổng số 3 trong mảng: ', count)


